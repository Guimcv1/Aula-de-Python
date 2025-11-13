# app.py
from flask import Flask, request, jsonify, render_template_string, send_file
import os
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# --- CONFIG: usar variáveis de ambiente ---
OWM_APIKEY = os.getenv('OWM_APIKEY')           # OpenWeatherMap key
STORMGLASS_KEY = os.getenv('STORMGLASS_KEY')   # StormGlass key (opcional)
# NDBC: muitas vezes não exige key, usa endpoints públicos.

@app.route('/api/monitor')
def api_monitor():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    if not lat or not lon:
        return jsonify({'error':'lat/lon required'}), 400

    # 1) OpenWeather: obter tempo atual (temp, humidity, description)
    weather = fetch_openweather(lat, lon)

    # 2) StormGlass (ou fallback NDBC): obter wave height
    waves = fetch_waves(lat, lon)

    # 3) Analisar 'riscos' básicos: por exemplo, se waves.height > 2.5m e temp baixo => alerta
    risk = assess_risk(weather, waves)

    response = {
        'weather': weather,
        'waves': waves,
        'risk': risk
    }
    return jsonify(response)

def fetch_openweather(lat, lon):
    if not OWM_APIKEY:
        return {'error':'No OWM key configured'}
    try:
        # Usando One Call (exemplo) - ajuste para One Call 3.0 se desejar
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={OWM_APIKEY}&lang=pt'
        r = requests.get(url, timeout=8)
        r.raise_for_status()
        j = r.json()
        return {
            'temp': j.get('main',{}).get('temp'),
            'humidity': j.get('main',{}).get('humidity'),
            'summary': j.get('weather',[{}])[0].get('description','')
        }
    except Exception as e:
        return {'error': str(e)}

def fetch_waves(lat, lon):
    # Tenta StormGlass primeiro (preciso de chave); se não, tenta NDBC ou retorna vazio
    if STORMGLASS_KEY:
        try:
            url = 'https://api.stormglass.io/v2/weather/point'
            params = {'lat': lat, 'lng': lon, 'params':'waveHeight,swells','source':'noaa'}
            headers = {'Authorization': STORMGLASS_KEY}
            r = requests.get(url, params=params, headers=headers, timeout=8)
            r.raise_for_status()
            j = r.json()
            # extrair primeiro horário disponível
            hours = j.get('hours', [])
            if hours:
                first = hours[0]
                # stormglass pode oferecer vários campos; simplificamos
                height = None
                swell = None
                if 'waveHeight' in first and first['waveHeight']:
                    # pode ser dict por fonte; pegar valor numérico
                    wh = first['waveHeight']
                    if isinstance(wh, dict):
                        # pegar valor from first key
                        try:
                            height = list(wh.values())[0]
                        except:
                            height = None
                if 'swells' in first and first['swells']:
                    try:
                        swell = first['swells']
                    except:
                        swell = None
                return {'height': height, 'swell': swell}
            return {'height': None}
        except Exception as e:
            # fallback
            pass

    # Fallback: consultar NDBC (exemplo simplificado) - NDBC oferece arquivos e JSON feed de estações
    try:
        # aqui um exemplo: usar API pública CBIBS/NOAA (varia por região)
        # se você tiver uma estação específica, substitua station id
        # Exemplo: recuperar dados mais próximos não trivial — aqui apenas retorno vazio
        return {'height': None}
    except Exception as e:
        return {'error': str(e)}

def assess_risk(weather, waves):
    # regra simples: se ondas > 2.5m -> risco alto; se umidade muito alta -> alerta adicional
    try:
        h = None
        if isinstance(waves, dict):
            h = waves.get('height')
        if h is None:
            return {'summary':'Dados de onda indisponíveis — verifique fontes.'}
        h = float(h)
        parts = []
        if h >= 2.5:
            parts.append('Alto risco de ondas grandes — atenção a estruturas costeiras e banhistas.')
        elif h >= 1.5:
            parts.append('Risco moderado de ondas.')
        else:
            parts.append('Ondas dentro do esperado.')
        hum = weather.get('humidity') if isinstance(weather, dict) else None
        if hum and isinstance(hum,(int,float)) and hum > 90:
            parts.append('Umidade muito alta — atenção a condições de chuva e visibilidade reduzida.')
        return {'summary': ' '.join(parts)}
    except Exception as e:
        return {'summary': 'Erro no cálculo de risco: ' + str(e)}

# Rota simples para relatório (HTML). Você pode renderizar um template com gráfico/PDF.
@app.route('/report')
def report():
    lat = request.args.get('lat'); lon = request.args.get('lon')
    if not lat or not lon:
        return "Parâmetros lat e lon são necessários", 400
    # opcional: chamar /api/monitor internamente para montar relatório completo
    data = requests.get(request.url_root + f'api/monitor?lat={lat}&lon={lon}').json()
    # gerar HTML simples (em produção use templates)
    html = f"""
    <html><head><meta charset='utf-8'><title>Relatório — {lat},{lon}</title></head>
    <body style='font-family:Arial; padding:20px'>
      <h1>Relatório — {lat}, {lon}</h1>
      <h2>Tempo</h2><p>{data.get('weather')}</p>
      <h2>Ondas</h2><p>{data.get('waves')}</p>
      <h2>Risco</h2><p>{data.get('risk')}</p>
      <p>Gerado em servidor. Aqui você pode gerar PDF (wkhtmltopdf / weasyprint) ou manter como página web.</p>
    </body></html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)