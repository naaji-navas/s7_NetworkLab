import socket
import sys


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_host = '127.0.0.1'
server_port = 12345

client_socket.connect((server_host, server_port))
print('Connected to server on port:', server_port)

input_number = input('Enter a number: ')
client_socket.send(input_number.encode())

data = client_socket.recv(1024).decode()
print('Is prime:', data)
