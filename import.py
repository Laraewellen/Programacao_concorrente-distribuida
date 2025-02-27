import threading
import time

def tarefa():
    print("Início...")
    time.sleep(2)
    print("fim")
    
    thread= threading.Thread(target= tarefa)
    thread.start() #iniciar 
    thread.join() #aguardar a conclusão para inciar o codg fonte
    print("Thread principal finalizada")
    