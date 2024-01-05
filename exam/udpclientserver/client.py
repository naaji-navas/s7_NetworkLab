import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 12345)

client_socket.connect(server_address)
print('Connected to server on port:', server_address[1])

input_number = input('Enter a number: ')
client_socket.send(input_number.encode())

data= client_socket.recv(1024).decode()
print('Is prime:', data)
client_socket.close()
