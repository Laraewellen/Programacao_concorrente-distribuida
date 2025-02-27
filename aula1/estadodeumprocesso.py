import psutil

def obter_estado_processo(pid):
    try:
        processo = psutil.Process(pid)  
        estado = processo.status()
        return estado
    except psutil.NoSuchProcess:
        return "Processo não encontrado"
    except psutil.AccessDenied:
        return "Sem permissão para acessar o processo"
    except psutil.ZombieProcess:
        return "Processo zumbi"

# Solicita o PID ao usuário
pid = int(input("Digite o PID do processo: "))

estado = obter_estado_processo(pid)

print(f"Estado do processo {pid}: {estado}")
