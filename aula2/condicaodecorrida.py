import threading
import time

#variavel global (acessada por todas as threads)

Contador = 0

def incrementar():
    global Contador
    for _ in range(5000): #reduzido o n de irerações por thread
        V = Contador
        time.sleep(0.001) #atraso artificial para aumentar a chance de colisões
        Contador = V + 1
threads = []

for i in range(50):
    t = threading.Thread(target = incrementar)
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()

print(f"Valor final: {Contador}")
        