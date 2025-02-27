import threading
import time

def tarefa():
    print("Início...")
    time.sleep(5)
    print("fim...")
    
    #bloco principal (main)
tA = threading.Thread(target=tarefa)
tB = threading.Thread(target=tarefa)
    
tA.start()
tB.start()
tA.join()
tB.join()
    
print("Thread principal finalizasa!")