import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_address=('127.0.0.1',5000)
server_socket.bind(server_address)
server_socket.listen(5)
print(f"Server is up and listeing on {server_address}")


while True:
  clinet_socket,client_address = server_socket.accept()
  message=clinet_socket.recv(1024).decode()
  
  if(message=='exit'):
    print("client has disconnected")
    break
  else:
    print(f"Client: {message}")
    data = input("Server :")
    clinet_socket.send(data.encode())
  clinet_socket.close()
server_socket.close()