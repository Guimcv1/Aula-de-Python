from flask import Flask

# 1. Cria uma instância da aplicação Flask
# __name__ é o nome do módulo Python atual.
app = Flask(__name__)

# 2. Define uma rota (a URL que aciona a função)
# '/' é a rota raiz (página inicial)
@app.route('/')
def hello_world():
    # 3. A "view function": o que é retornado quando a rota é acessada
    return 'Olá, Mundo!'