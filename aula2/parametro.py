import threading
import time

def saudacao(nome, tempo):
    print(f"olá, {nome}")
    time.sleep(tempo)
    print(f"tchau, {nome}")

thread = threading.Thread(target=saudacao, args = ("Lara", 6))
thread.start()
thread.join()

print ("Thread principal encerrada")