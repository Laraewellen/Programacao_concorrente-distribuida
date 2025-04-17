import socket

def main():
    host = '127.0.0.1'
    port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    try:
        while True:
            msg = client.recv(1024).decode()
            if not msg:
                break
            print(msg)
            entrada = input("> ")
            client.sendall(entrada.encode())
            resposta = client.recv(1024).decode()
            print(resposta)
            if entrada.lower() == 'sair':
                break
    finally:
        client.close()

if __name__ == "__main__":
    main()
