import threading
import time

def saudacao(nome, tempo):
    print(f"olá, {nome}")
    time.sleep(tempo)
    print(f"tchau, {nome}")

A= thread = threading.Thread(target=saudacao, args = ("Lara", 6))
B= thread = threading.Thread(target=saudacao, args = ("Julia", 2))
A.start()
B.start()
A.join()
B.join()

print ("Thread principal encerrada")