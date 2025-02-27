import threading
import time

def tarefa():
    print("Inicio...")
    time.sleep(5)
    print("Fim...")

# Bloco princila(MAIN)

thread = threading.Thread(target = tarefa)
thread.start() # Iniciar a thread
thread.join() # Aguardar a conclusão da thread
print("Thread principal finalizada")