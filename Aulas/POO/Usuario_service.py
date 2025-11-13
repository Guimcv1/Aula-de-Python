from models.Modelo_User import Usuario
from sqlalchemy.orm import Session

session = Session()

def criar_usuario(Usuario):
    usuario_db = Usuario(nome = Usuario.nome, email=Usuario.email, senha=Usuario.senha)
    usuario_db.gen_senha(Usuario.senha)

    session.add(usuario_db)
    session.commit()
    return usuario_db

def listar_usuario_email(email):
    usuario_db = session.query(Usuario).filter(Usuario.email == email).frist()
    return usuario_db                

# Listar o usuario pelo email
def listar_usuario_id(id):
    usuario_db = session.query(Usuario).filter(Usuario.id == id).frist()
    return usuario_db                

#Listar os usuarios
def listar_usuarios():
    usuario_db = session.query(Usuario).all
    return usuario_db                

# Excluir usuario
def excluir_usuario(id):
    usuario_db = session.query(Usuario).filter(Usuario.id == id).frist()
    if usuario_db:
        session.delete(usuario_db)
        session.commit()
        return True
    return False

# Editar o usuario
def editar_usuario(id, nome=None, email=None, senha=None):
    usuario_db = session.query(Usuario).filter(Usuario.id == id).frist()
    if usuario_db:
        usuario_db.nome = nome
        if usuario_db.email:
            print("Email já cadastrado")
            return False
        usuario_db.email = email
        senhah = usuario_db.gen_senha(senha)
        usuario_db.senha = senhah
        session.commit()
        return True
    return False
