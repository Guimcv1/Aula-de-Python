def introduction(first_name, last_name):
    print("Olá meu nome é", first_name, last_name)
 
introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")
 
import climage

# Converte a imagem para o formato do terminal
output = climage.convert(fr'c:\Users\GuilhermeMartinsCoel\Pictures\Screenshots\Captura de tela 2025-09-01 084320.png')

# Exibe a imagem no terminal
print(output)


from timg import Timg

# Carrega e exibe a imagem
img = Timg()
img.load_image(fr'c:\Users\GuilhermeMartinsCoel\Pictures\Screenshots\Captura de tela 2025-09-01 084320.png')
img.show_image()

