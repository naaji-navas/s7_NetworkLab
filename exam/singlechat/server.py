import socket

# program for implementing single chat server

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# define the port and host
server_address = ('127.0.0.1', 12345)

# bind the socket to the server
server_socket.bind(server_address)

server_socket.listen(5)
print("Server is up and listening to the port 12345")

while True:
  client_socket, client_address = server_socket.accept()
  print("Connected to ", client_address)
  
  # now recieve the data from the client
  
  data = client_socket.recv(1024).decode()
  
  if data == "exit":
    print ("Client has exited the chat")
    break
  else:
    print("Client: ", data)
    message = input("Server: ")
    client_socket.send(message.encode())
  
  client_socket.close()
  
server_socket.close()