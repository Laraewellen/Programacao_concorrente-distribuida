import socket
import threading

assentos = [False] * 100  # False = disponível, True = reservado
lock = threading.Lock()

def handle_client(conn, addr):
    print(f"[CONEXÃO] Cliente conectado: {addr}")
    try:
        while True:
            conn.sendall("Digite os números dos assentos para reservar (ex: 1,2,3), ou 'sair': ".encode())
            data = conn.recv(1024).decode().strip()
            if not data or data.lower() == 'sair':
                break

            try:
                pedidos = [int(n.strip()) for n in data.split(',')]
                reservados = []

                with lock:
                    for assento in pedidos:
                        if 1 <= assento <= 100 and not assentos[assento - 1]:
                            assentos[assento - 1] = True
                            reservados.append(assento)

                if reservados:
                    conn.sendall(f"Assentos reservados com sucesso: {reservados}\n".encode())
                    print(f"[RESERVA] Cliente {addr} reservou: {reservados}")
                else:
                    conn.sendall("Nenhum assento foi reservado. Todos já estavam ocupados.\n".encode())
            except Exception as e:
                conn.sendall("Entrada inválida. Tente novamente.\n".encode())
    finally:
        conn.close()
        print(f"[DESCONECTADO] Cliente {addr} desconectado.")

def main():
    host = '127.0.0.1'
    port = 12345
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[INICIADO] Servidor ouvindo em {host}:{port}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()
