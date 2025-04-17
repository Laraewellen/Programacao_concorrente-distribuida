import socket
import threading

assentos = [False] * 100
lock = threading.Lock()

def mostrar_assentos():
    return "\n".join([f"Assento {i+1}: {'Livre' if not ocupado else 'Reservado'}"
                      for i, ocupado in enumerate(assentos)])

def lidar_com_cliente(conn, addr):
    print(f"🟢 Cliente conectado: {addr}")
    try:
        while True:
            prompt = (
                "\nDigite 'ver' para ver os assentos,\n"
                "ou números dos assentos separados por vírgula para reservar (ex: 10,12),\n"
                "ou 'sair' para sair:\n"
            )
            conn.sendall(prompt.encode())

            dados = conn.recv(1024).decode().strip()
            if not dados:
                break

            if dados.lower() == "ver":
                print(f"[{addr}] solicitou visualização dos assentos")
                estado = mostrar_assentos()
                conn.sendall((estado + "\n").encode())

            elif dados.lower() == "sair":
                print(f"[{addr}] encerrou a conexão")
                break

            else:
                try:
                    assentos_desejados = list(map(int, dados.split(",")))
                    print(f"[{addr}] tentou reservar os assentos: {assentos_desejados}")

                    with lock:
                        sucesso = True
                        for a in assentos_desejados:
                            if a < 1 or a > 100 or assentos[a - 1]:
                                sucesso = False
                                break

                        if sucesso:
                            for a in assentos_desejados:
                                assentos[a - 1] = True
                            mensagem = "✅ Reserva confirmada.\n"
                            print(f"[{addr}] reserva confirmada para os assentos: {assentos_desejados}")
                        else:
                            mensagem = "❌ Falha na reserva. Verifique se os assentos estão disponíveis ou válidos.\n"
                            print(f"[{addr}] falha ao reservar os assentos: {assentos_desejados}")

                    conn.sendall(mensagem.encode())

                except ValueError:
                    erro = "❗ Entrada inválida. Use apenas números separados por vírgula.\n"
                    conn.sendall(erro.encode())
                    print(f"[{addr}] enviou entrada inválida: {dados}")

    finally:
        conn.close()
        print(f"🔴 Cliente desconectado: {addr}")

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("localhost", 12345))
    servidor.listen()
    print("🚀 Servidor iniciado. Aguardando conexões...\n")

    while True:
        conn, addr = servidor.accept()
        print(f"🔗 Conexão estabelecida com {addr}")
        threading.Thread(target=lidar_com_cliente, args=(conn, addr), daemon=True).start()

iniciar_servidor()
