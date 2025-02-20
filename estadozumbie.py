import psutil

def listar_processos_zumbis():
    zumbis = []
    for processo in psutil.process_iter(['pid', 'name', 'status']):
        if processo.info['status'] == psutil.STATUS_ZOMBIE:
            zumbis.append(processo.info)
    return zumbis

zumbis = listar_processos_zumbis()

if zumbis:
    print("Processos Zumbis:")
    for zumbi in zumbis:
        print(f"PID: {zumbi['pid']}, Nome: {zumbi['name']}")
else:
    print("Nenhum processo zumbi encontrado.")
