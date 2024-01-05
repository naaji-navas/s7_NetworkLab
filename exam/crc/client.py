import socket
import pickle
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('127.0.0.1',6000)

client_socket.connect(server_address)


msg= input("Enter the  string to check the error using crc :")
client_socket.send(msg.encode())


client_socket.close()

