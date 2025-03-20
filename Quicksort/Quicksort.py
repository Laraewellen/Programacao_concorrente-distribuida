import random
import threading
import time
import heapq

# Função para ordenar uma sublista
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right)

# Função para dividir a lista e ordenar usando múltiplas threads
def threaded_quicksort(arr, num_threads=4):
    if len(arr) < num_threads:
        num_threads = len(arr)  # Evitar mais threads do que elementos

    tamanho_sublista = len(arr) // num_threads
    sublistas = [arr[i * tamanho_sublista: (i + 1) * tamanho_sublista] for i in range(num_threads)]
    sublistas[-1].extend(arr[num_threads * tamanho_sublista:])  # Adiciona o restante à última sublista

    threads = []
    resultados = []

    lock = threading.Lock()

    def ordenar_sublista(sublista):
        resultado = quicksort(sublista)
        with lock:
            resultados.append(resultado)  # Protegido contra concorrência

    # Criando e iniciando as threads
    for i in range(num_threads):
        thread = threading.Thread(target=ordenar_sublista, args=(sublistas[i],))
        threads.append(thread)
        thread.start()

    # Aguardando todas as threads terminarem
    for thread in threads:
        thread.join()

    # Mesclando os resultados das sublistas ordenadas
    return list(heapq.merge(*resultados))  # Merge eficiente

# Função para gerar números aleatórios
def gerar_numeros_aleatorios(n=100, min_val=1, max_val=200):
    return [random.randint(min_val, max_val) for _ in range(n)]

# Função para medir tempo de execução
def medir_tempo_execucao(func, *args):
    inicio = time.time()
    resultado = func(*args)
    fim = time.time()
    return resultado, fim - inicio

if __name__ == "__main__":
    numeros = gerar_numeros_aleatorios(10000, 1, 100000)

    print("Primeiros 10 números antes da ordenação:", numeros[:10])

    # Ordenação com threads
    numeros_ordenados, tempo_com_threads = medir_tempo_execucao(threaded_quicksort, numeros, 4)

    print("Primeiros 10 números após a ordenação:", numeros_ordenados[:10])
    print(f"Tempo de execução com threading: {tempo_com_threads:.6f} segundos")

    # Comparação com sorted
    numeros_ordenados_sem_threads, tempo_sem_threads = medir_tempo_execucao(sorted, numeros)

    print(f"Tempo de execução sem threads (usando sorted): {tempo_sem_threads:.6f} segundos")
