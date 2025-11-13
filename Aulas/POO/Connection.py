from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
# Criar uma conexão
SQLALCHEMY_DATABASE_URI = "mysql://3c571c1b794a48358fc2258c2b5ade29:Gm7856cv12@mysql.shardatabases.app:3306/database"

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    connection = engine.connect()
    print("Conexão com o banco feita com sucesso!")
except Exception as e:
    print("Erro ao conectar com o banco", e)

Base = declarative_base()





"""
motor = create_engine("mysql://3c571c1b794a48358fc2258c2b5ade29:Gm7856cv12@mysql.shardatabases.app:3306/database")

#Definir uma tabela

from sqlalchemy import column, Integer, String
from sqlalchemy.orm import declarative_base

# Clase base das Tabelas
Base = declarative_base()

#Criando uma tabela chamada "Usuario"
class Usuario(Base):
    __tablename__ = "Usuario"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = column(Integer)

Base.metadata.create_all(motor)

# inserir os dados no Banco

from sqlalchemy.orm import sessionmaker

#criando uma sessão 
Session = sessionmaker(bind=motor)
Session = Session()

#Criando um novo usuario
novo_usuario = Usuario(nome="Alice", Idade=30)

#Adicionando e salvando no banco
Session.add(novo_usuario)
Session.commit()

#Consuta de dados
# Buscar todos os usuarios

usuarios = Session.query(usuarios).all()

for usuario in usuarios:
    print(usuario)"""