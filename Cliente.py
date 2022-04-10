import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(("127.0.0.1", 80))
server.send(str.encode("info"))
dado = server.recv(2048)
print("Mensagem recebida:", dado.decode())
