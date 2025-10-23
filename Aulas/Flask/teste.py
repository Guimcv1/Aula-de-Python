from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Rota para renderizar o HTML
@app.route('/')
def index():
    return render_template('index.html')

# Rota para enviar dados em JSON
@app.route('/dados')
def dados():
    data = {"nome": "João", "idade": 25, "cidade": "Brasília"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
