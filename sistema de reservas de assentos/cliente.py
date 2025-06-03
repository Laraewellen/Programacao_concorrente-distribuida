import socket

def iniciar_cliente():
    host = 'localhost'
    porta = 12345

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host, porta))

    while True:
        prompt = cliente.recv(1024).decode()
        print(prompt)

        entrada = input("> ")
        cliente.sendall(entrada.encode())

        if entrada.lower() == 'sair':
            break

        resposta = cliente.recv(4096).decode()
        print(resposta)

    cliente.close()

if __name__ == "__main__":
    iniciar_cliente()
