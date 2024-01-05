import socket
import pickle
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address=('127.0.0.1',9002)

server_socket.bind(server_address)

server_socket.listen(5)
print("Server is up and listening")

client_socket,client_address = server_socket.accept()

data = (client_socket.recv(1024).decode())
print(f"The data recived is {(data)}")
binary_array = [int(bit) for bit in data]
print (binary_array)

p1=0
p2=1
p4=0
d7=binary_array[0]
d6=binary_array[1]
d5=binary_array[2]
d3=binary_array[3]

p1 = d3 ^ d5 ^ d7
p2 = d3 ^ d6 ^ d7
p4 = d5 ^ d6 ^ d7
print("Hamming code is :")
hamming_array=[d7,d6,d5,p4,d3,p2,p1]

print(hamming_array)







server_socket.close()
client_socket.close()