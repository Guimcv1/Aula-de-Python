import json
import os

class Livro:
    def __init__(self, id, nome, autor, dt, categoria):
        self.__id = id
        self.__nome = nome
        self.__autor = autor
        self.__dt = dt
        self.__categoria = categoria,

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,n_id):
        self__id = n_id

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,n_nome):
        self__nome = n_nome
    
    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self,n_autor):
        self__autor = n_autor
    
    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self,n_categoria):
        self__categoria = n_categoria
    
    @property
    def dt(self):
        return self.__dt
    
    @dt.setter
    def dt(self,n_dt):
        self__dt = n_dt

    def cadastrar(self):
        lista = {
            'Id do Livro' : self.__id,
            'Nome do Livro' : self.__nome,
            'Autor do Livro' : self.__autor,
            'Data do Livro' : self.__dt,
            'Categoria do Livro' : self.__categoria
        }
        return lista

class Biblioteca(Livro):
    def __init__(self, id, nome, autor, dt, categoria):
        super().__init__(id, nome, autor, dt, categoria)

    def salvar(self):

        def carregar():
            if os.path.exists('Aulas/Aula_11/json.json'):                                     
                with open('Aulas/Aula_11/json.json', "r", encoding="utf-8") as f:             
                    try:
                        return json.load(f)                                 
                    except json.JSONDecodeError:                            
                        return []
                return []
            
        final = carregar()
        final.append(self,a)

        with open('Aulas/Aula_11/json.json', "w", encoding="utf-8") as f:               
            json.dump(final, f, indent=2, ensure_ascii=False)          

    def listar(self):
        def carregar():
            if os.path.exists('Aulas/Aula_11/json.json'):                                     
                with open('Aulas/Aula_11/json.json', "r", encoding="utf-8") as f:             
                    try:
                        return json.load(f)                                 
                    except json.JSONDecodeError:                            
                        return []
                return []
        print('oi')
        lista_livros = carregar()
        print(lista_livros)

        

    

a = Biblioteca(2,2,2,2,2)
print(a)
a.cadastrar()
a.salvar()
a.listar()

"""livro123 = Biblioteca(1, 'snome', 'sautor', 'sdata', 'scategoria')
livro4 = livro123.cadastrar()
print(livro4)
livro123.listar()"""