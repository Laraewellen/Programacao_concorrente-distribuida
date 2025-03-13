# servidor_data_hora.py
import socket
from datetime import datetime

def iniciar_servidor():
    # Configuração do servidor
    HOST = '127.0.0.1'  # Endereço local
    PORT = 65432  # Porta para comunicação

    # Criando o socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))  # Associa o socket ao endereço e porta
        s.listen()  # Habilita o servidor para aceitar conexões
        print(f"Bom dia! Sev: {HOST}:{PORT}")

        while True:
            # Aguarda uma conexão
            conn, addr = s.accept()
            with conn:
                print(f"Conectado por {addr}")
                while True:
                    # Recebe dados do cliente
                    data = conn.recv(1024)
                    if not data:
                        break

                    # Verifica se o cliente pediu a data e hora
                    if data.decode().strip().lower() == "data e hora":
                        # Obtém a data e hora atuais
                        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        resposta = f"Data e hora atual: {agora}"
                        conn.sendall(resposta.encode())  # Envia a resposta ao cliente
                    else:
                        conn.sendall(b"Mensagem invalida")

if __name__ == "__main__":
    iniciar_servidor()
