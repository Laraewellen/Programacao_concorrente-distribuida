from PIL import Image
from tkinter import Tk, filedialog
import threading

def processar_faixa(imagem, imagem_pb, faixa_inicio, faixa_fim):
    largura = imagem.width
    for y in range(faixa_inicio, faixa_fim):
        for x in range(largura):
            r, g, b = imagem.getpixel((x, y))
            luminancia = int(0.299 * r + 0.587 * g + 0.114 * b)
            imagem_pb.putpixel((x, y), luminancia)

def converter_para_preto_e_branco_threads():
    try:
        root = Tk()
        root.withdraw()

        caminho_imagem = filedialog.askopenfilename(
            title="Selecione uma imagem",
            filetypes=[("Imagens", "*.jpg *.jpeg *.png *.bmp *.gif"), ("Todos os arquivos", "*.*")]
        )

        if not caminho_imagem:
            print("Nenhuma imagem foi selecionada.")
            return

        imagem = Image.open(caminho_imagem)
        imagem = imagem.convert("RGB")  # Garante que a imagem esteja no modo RGB
        largura, altura = imagem.size
        imagem_preto_branco = Image.new("L", (largura, altura))

        num_threads = 4  # Número de threads a serem utilizadas
        faixas = [(i * (altura // num_threads), (i + 1) * (altura // num_threads)) for i in range(num_threads)]
        faixas[-1] = (faixas[-1][0], altura)  # Garante que a última faixa cubra toda a imagem

        threads = []
        for faixa_inicio, faixa_fim in faixas:
            thread = threading.Thread(target=processar_faixa, args=(imagem, imagem_preto_branco, faixa_inicio, faixa_fim))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        caminho_saida = filedialog.asksaveasfilename(
            title="Salvar imagem em preto e branco",
            defaultextension=".jpg",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("Todos os arquivos", "*.*")]
        )

        if not caminho_saida:
            print("Operação de salvamento cancelada.")
            return

        imagem_preto_branco.save(caminho_saida)
        print(f"Imagem convertida com sucesso! Salva em: {caminho_saida}")

    except Exception as e:
        print(f"Erro ao processar a imagem: {e}")

if __name__ == "__main__":
    converter_para_preto_e_branco_threads()