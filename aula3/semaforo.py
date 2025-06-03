import threading
s = threading.Semaphore(3) #semáforo com limite de 3 threads

def Acesso(thread_id):
    print(f"thread {thread_id} tentando acessar o recurso")
    with s:
        print(f"Thread {thread_id} acessou o recurso")
        threading.Event().wait(1)
        print(f"Thread {thread_id} liberou o recurso")

threads = [threading.Thread(target = Acesso, args = (i,)) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()

print(f"encerrando")