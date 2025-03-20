import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import threading
import time

def processar_pagina(url, palavra, url_inicial, resultados, urls_visitados, lock):
    """
    Processa uma única página da web, verificando a presença da palavra e extraindo links.
    """
    with lock:
        if url in urls_visitados:
            return
        urls_visitados.add(url)
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        conteudo = soup.get_text().lower()
        palavra_encontrada = palavra.lower() in conteudo
        
        with lock:
            resultados[url] = palavra_encontrada

        # Extrai links e retorna uma lista de URLs completas
        links = [urljoin(url_inicial, link['href']) for link in soup.find_all('a', href=True)]
        return [link for link in links if link.startswith(url_inicial)]
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")
        return []

def buscar_palavra_com_threads(url_inicial, palavra, profundidade_maxima=3):
    """
    Realiza a busca da palavra utilizando threads para processar múltiplas páginas simultaneamente.
    """
    urls_visitados = set()
    resultados = {}
    lock = threading.Lock()
    
    def worker(urls, profundidade):
        if profundidade > profundidade_maxima:
            return
        threads = []
        novas_urls = []
        
        for url in urls:
            thread = threading.Thread(target=lambda q, u: q.extend(processar_pagina(u, palavra, url_inicial, resultados, urls_visitados, lock) or []), args=(novas_urls, url))
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()
        
        if novas_urls:
            worker(novas_urls, profundidade + 1)
    
    worker([url_inicial], 1)
    return resultados

if __name__ == "__main__":
    url_inicial = input("Digite a URL inicial do site (ex.: https://www.exemplo.com): ")
    palavra = input("Digite a palavra a ser buscada: ")
    
    # Mede tempo de execução com threads
    inicio = time.time()
    resultados = buscar_palavra_com_threads(url_inicial, palavra)
    fim = time.time()
    
    print("\nResultados da busca:")
    for url, encontrada in resultados.items():
        status = "Encontrada" if encontrada else "Não encontrada"
        print(f"{url}: Palavra '{palavra}' {status}")
    
    print(f"\nTempo de execução com threads: {fim - inicio:.2f} segundos")
