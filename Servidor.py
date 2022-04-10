import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 80))
server.listen()

print("Aguardando conexão...")

conexao, endereco = server.accept()

print("Conectado em", endereco)

while True:
    dados = conexao.recv(2048)
    if dados:        
        conexao.sendall(dados)
        