import psutil

def obter_memoria_processo(pid):
    try:
        processo = psutil.Process(pid)  
        memoria_fisica = processo.memory_info().rss / (1024 * 1024)  
        memoria_virtual = processo.memory_info().vms / (1024 * 1024)  
        return memoria_fisica, memoria_virtual
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        return None, None

# Definir o PID como 0
pid = 0  

memoria_fisica, memoria_virtual = obter_memoria_processo(pid)

if memoria_fisica is not None:
    print(f"Processo PID {pid}:")
    print(f"Memória Física (RSS): {memoria_fisica:.2f} MB")
    print(f"Memória Virtual (VMS): {memoria_virtual:.2f} MB")
else:
    print(f"Não foi possível acessar o processo com PID {pid}. Ele pode ser um processo do sistema ou protegido.")
