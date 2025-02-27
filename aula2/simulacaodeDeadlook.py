#espera infinita
import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def T1():
    print("t1: tentando adquirir lock 1")
    lock1.acquire()
    print("T1: lock1 adquirido, tentando adquirir lock2")
    time.sleep(1)
    lock2.acquire()
    print("t1: lock2 adquirido")
    lock2.release()
    lock1.release()
    print("t1: Finalizada")
    
def T2():
    print("t2: tentando adquirir lock 1")
    lock2.acquire()
    print("T2: lock1 adquirido, tentando adquirir lock1")
    time.sleep(1)
    lock1.acquire()
    print("t2: lock2 adquirido")
    lock1.release()
    lock2.release()
    print("t2: Finalizada")
    
t1 = threading.Thread(target = T1)
t2 = threading.Thread(target = T2)
    
t1.start()
t2.start()

t1.join()
t2.join()