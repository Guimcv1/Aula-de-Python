import timg

def exibir_imagem_timg(caminho_imagem):
    renderer = timg.Renderer()
    renderer.load_image(caminho_imagem)
    renderer.set_size(80, 40)  # Ajuste a resolução
    renderer.render(timg.ASCIIMethod)  # Pode ser timg.ASCIIMethod ou timg.BlockMethod

# Exemplo de uso
exibir_imagem_timg(r"c:\Users\GuilhermeMartinsCoel\Desktop\Python\Aula-de-Python\Todos-os-Codigos\Testes\Captura de tela 2025-09-01 084320.png")