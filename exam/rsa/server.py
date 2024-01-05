import socket
import pickle
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address=('127.0.0.1',9001)

server_socket.bind(server_address)

server_socket.listen(5)
print("Server is up and listening")

client_socket,client_address = server_socket.accept()

key = client_socket.recv(1024)
e,n=pickle.loads(key)

msg=client_socket.recv(1024).decode()

print(f"Server recieved the message to be encrypted : {msg}")
#encryption
encrypted_msg=pow(int(msg),e,n)

print(f"Encrypted message:{encrypted_msg}")
client_socket.send(str(encrypted_msg).encode())

server_socket.close()
client_socket.close()