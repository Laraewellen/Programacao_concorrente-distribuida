import threading
import time

#variavel global (acessada por todas as threads)

Contador = 0

lock  = threading.Lock() #bloqueio

def incrementar():
    global Contador
    for _ in range(1000):
        lock.acquire() #acessar o recurso(variavel)
        try:
            Contador = Contador + 1
        finally:
            lock.release() #liberar o recurso(variavel)
threads = []

for i in range (10):
    thread = threading.Thread(target = incrementar)
    threads.append(thread) 
    thread.start()

for thread in threads:
    thread.join()
    
print(f"Contador: {Contador}")