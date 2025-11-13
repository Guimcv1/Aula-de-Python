// script.js
const checkBtn = document.getElementById('checkBtn');
const reportBtn = document.getElementById('reportBtn');
const refreshBtn = document.getElementById('refreshBtn');
const clearBtn = document.getElementById('clearBtn');
const latInput = document.getElementById('lat');
const lonInput = document.getElementById('lon');
const output = document.getElementById('output');
const cards = document.getElementById('cards');
const mapImg = document.getElementById('mapImg');
const mapCaption = document.getElementById('mapCaption');

function log(msg){
  const t = new Date().toLocaleTimeString();
  output.textContent += `[${t}] ${msg}\n`;
  output.scrollTop = output.scrollHeight;
}

async function fetchData(){
  const lat = latInput.value.trim();
  const lon = lonInput.value.trim();
  if(!lat || !lon){ log('Preencha latitude e longitude'); return; }

  log(`Solicitando dados para ${lat}, ${lon}...`);
  try{
    const res = await fetch(`/api/monitor?lat=${encodeURIComponent(lat)}&lon=${encodeURIComponent(lon)}`);
    if(!res.ok) throw new Error('Erro no servidor');
    const data = await res.json();
    renderData(data);
    log('Dados recebidos e renderizados.');
  }catch(err){
    log('Erro: ' + err.message);
  }
}

function renderData(data){
  cards.innerHTML = '';

  // Card: Weather (temperatura, umidade, descrição)
  const weatherCard = document.createElement('div'); weatherCard.className='card';
  weatherCard.innerHTML = `<h3>Tempo</h3>
    <p><strong>${data.weather.summary}</strong></p>
    <p>Temp: ${data.weather.temp}°C — Umidade: ${data.weather.humidity}%</p>`;
  cards.appendChild(weatherCard);

  // Card: Ondas
  const waveCard = document.createElement('div'); waveCard.className='card';
  waveCard.innerHTML = `<h3>Ondas</h3>
    <p>Altura: ${data.waves.height ?? '—'} m</p>
    <p>Swell: ${data.waves.swell ?? '—'}</p>`;
  cards.appendChild(waveCard);

  // Card: Consequências / risco
  const riskCard = document.createElement('div'); riskCard.className='card';
  riskCard.innerHTML = `<h3>Risco / Consequências</h3>
    <p>${data.risk.summary}</p>`;
  cards.appendChild(riskCard);

  // Map preview (simples: static map via OpenStreetMap / Mapbox - aqui usamos uma tile estática do OpenStreetMap via url de terceiros)
  const lat = latInput.value.trim(), lon = lonInput.value.trim();
  // nota: para produção considere usar mapas com API key (Mapbox/Google) ou gerar tiles no backend
  mapImg.src = `https://static-maps.yandex.ru/1.x/?ll=${lon},${lat}&size=600,300&z=8&l=map&pt=${lon},${lat},pm2rdm`;
  mapCaption.textContent = `Preview em ${lat}, ${lon}`;

}

// abrir nova aba (relatório mais detalhado no backend)
reportBtn.addEventListener('click', () => {
  const lat = latInput.value.trim(), lon = lonInput.value.trim();
  if(!lat || !lon){ log('Preencha latitude e longitude antes de abrir relatório'); return; }
  const url = `/report?lat=${encodeURIComponent(lat)}&lon=${encodeURIComponent(lon)}`;
  const w = window.open(url, '_blank', 'noopener,noreferrer');
  if(w) log('Relatório aberto em nova aba.');
  else log('Falha ao abrir nova aba (bloqueador de pop-ups?).');
});

checkBtn.addEventListener('click', fetchData);
refreshBtn.addEventListener('click', fetchData);
clearBtn.addEventListener('click', () => {
  latInput.value=''; lonInput.value=''; cards.innerHTML=''; output.textContent=''; mapImg.src=''; mapCaption.textContent='';
  log('Limpo.');
});

// auto-fill exemplo (opcional)
latInput.value = '-23.5489'; lonInput.value = '-46.6388';