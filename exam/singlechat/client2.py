import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_address=('127.0.0.1',5000)

client_socket.connect(server_address)


while True:
  message=input("CLient :")
  client_socket.send(message.encode())
  
  data = client_socket.recv(1024).decode()
  print(f"Server: {data}")
  
  client_socket.close()
  
  
