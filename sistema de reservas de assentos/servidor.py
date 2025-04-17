import socket
import threading

# Lista de 100 assentos (False = disponível, True = reservado)
assentos = [False] * 100
lock = threading.Lock()

def formatar_assentos():
    visual = ""
    for i in range(100):
        status = "XX" if assentos[i] else f"{i+1:02}"
        visual += f"[{status}] "
        if (i + 1) % 10 == 0:
            visual += "\n"
    return visual

def lidar_com_cliente(conn, addr):
    print(f"Cliente conectado: {addr}")
    conn.sendall("Bem-vindo ao sistema de reserva de assentos!\n".encode())

    while True:
        try:
            conn.sendall("Digite os números dos assentos que deseja reservar (ex: 1,2,3) ou 'sair': ".encode())
            dados = conn.recv(1024).decode().strip()

            if not dados or dados.lower() == 'sair':
                break

            numeros = [int(n) for n in dados.split(',') if n.isdigit()]
            reservados = []
            ja_ocupados = []
            com_erro = []

            with lock:
                for n in numeros:
                    if 1 <= n <= 100:
                        if not assentos[n - 1]:
                            assentos[n - 1] = True
                            reservados.append(n)
                        else:
                            ja_ocupados.append(n)
                    else:
                        com_erro.append(n)

            resposta = ""
            if reservados:
                resposta += f"Assentos reservados com sucesso: {', '.join(map(str, reservados))}\n"
            if ja_ocupados:
                resposta += f"Já estavam ocupados: {', '.join(map(str, ja_ocupados))}\n"
            if com_erro:
                resposta += f"Números inválidos: {', '.join(map(str, com_erro))}\n"

            resposta += "\nEstado atual dos assentos:\n" + formatar_assentos()
            conn.sendall(resposta.encode())
        except:
            break

    print(f"Cliente desconectado: {addr}")
    conn.close()

def iniciar_servidor():
    host = 'localhost'
    porta = 12345
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen(5)
    print("Servidor iniciado. Aguardando conexões...")

    while True:
        conn, addr = servidor.accept()
        thread = threading.Thread(target=lidar_com_cliente, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    iniciar_servidor()
