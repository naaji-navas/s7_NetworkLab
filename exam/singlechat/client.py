import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 12345)

client_socket.connect(server_address)

while True:
  message = input("Client: ")
  client_socket.send(message.encode())
  
  if message == "exit":
    print("Client has exited the chat")
    break
  else:
    data = client_socket.recv(1024).decode()
    data= input("server :")
    client_socket.send(data.encode())
  
  
client_socket.close()
