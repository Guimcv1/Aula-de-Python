<<<<<<< HEAD
from ascii_art import ascii_art
# Load an image
image_path = "Todos-os-Codigos/Testes/Captura de tela 2025-09-01 084320.png"
with open(image_path, "rb") as f:
   image_data = f.read()
# Convert the image to ASCII art
ascii_data = ascii_art(image_data)
# Display the ASCII art in the terminal
print(ascii_data)
=======
import timg

def exibir_imagem_timg(caminho_imagem):
    renderer = timg.Renderer()
    renderer.load_image(caminho_imagem)
    renderer.set_size(80, 40)  # Ajuste a resolução
    renderer.render(timg.ASCIIMethod)  # Pode ser timg.ASCIIMethod ou timg.BlockMethod

# Exemplo de uso
exibir_imagem_timg(r"c:\Users\GuilhermeMartinsCoel\Desktop\Python\Aula-de-Python\Todos-os-Codigos\Testes\Captura de tela 2025-09-01 084320.png")
>>>>>>> 675609c1e16924cdcfc59caa3ded69266d767794
