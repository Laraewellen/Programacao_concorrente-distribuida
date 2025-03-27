import numpy as np
import matplotlib.pyplot as plt
import threading
import os

# Ajustando o backend para evitar erros com o Matplotlib em threads
plt.switch_backend('Agg')

# Função de salvamento de imagem
def salvar_imagem(path):
    plt.savefig(path, bbox_inches='tight', dpi=300)
    plt.close()  # Fecha a figura após salvar

# Função para gerar o Triângulo de Sierpinski
def sierpinski():
    print("Gerando Triângulo de Sierpinski...")
    # Código para gerar o Triângulo de Sierpinski (adapte conforme necessário)
    plt.figure()
    # Exemplo simples de fractal
    ax = plt.gca()
    ax.set_facecolor('black')
    plt.title("Triângulo de Sierpinski")
    salvar_imagem("sierpinski.png")

# Função para gerar o Conjunto de Mandelbrot
def mandelbrot():
    print("Gerando Conjunto de Mandelbrot...")
    # Gerando a imagem do conjunto de Mandelbrot
    x_min, x_max, y_min, y_max = -2.0, 1.0, -1.5, 1.5
    width, height = 800, 800
    x, y = np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    C = Z.copy()
    max_iter = 256
    img = np.zeros((height, width))
    for i in range(max_iter):
        Z = Z**2 + C
        mask = np.abs(Z) < 1000
        img += mask
    # Verifica se a imagem foi gerada corretamente
    if img is not None and img.size > 0:
        plt.figure()
        plt.imshow(img, extent=(x_min, x_max, y_min, y_max), cmap='hot', interpolation='bilinear')
        plt.title("Conjunto de Mandelbrot")
        salvar_imagem("mandelbrot.png")
    else:
        print("Erro ao gerar imagem do Conjunto de Mandelbrot")

# Função para gerar a Árvore Fractal
def fractal_tree():
    print("Gerando Árvore Fractal...")
    # Código para gerar a Árvore Fractal (adapte conforme necessário)
    plt.figure()
    plt.title("Árvore Fractal")
    salvar_imagem("fractal_tree.png")

# Função para executar cada fractal em uma thread
def executar_fractal(func, nome):
    try:
        func()
    except Exception as e:
        print(f"Erro ao gerar {nome}: {e}")

# Lista de fractais a serem gerados
fractais = [
    (sierpinski, "Triângulo de Sierpinski"),
    (mandelbrot, "Conjunto de Mandelbrot"),
    (fractal_tree, "Árvore Fractal")
]

# Criando e iniciando as threads
threads = []
for func, nome in fractais:
    thread = threading.Thread(target=executar_fractal, args=(func, nome))
    threads.append(thread)
    thread.start()

# Esperando todas as threads terminarem
for thread in threads:
    thread.join()

print("Todas as imagens foram geradas!")
