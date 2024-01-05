import socket
import pickle
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('127.0.0.1',9001)

client_socket.connect(server_address)


msg= input("Enter the message")
#key generation

p=11
q=7
n=p*q
phi_n = (p-1) * (q-1)
e=7
d=pow(e,-1,phi_n)


encryption_key = pickle.dumps((e,n))
client_socket.send(encryption_key)
client_socket.send(msg.encode())
encrypted_msg= client_socket.recv(1024).decode()
print(f"Encrypted message is {encrypted_msg}")
decrypted_msg=pow(int(encrypted_msg),d,n)
print(f"Decrypted message :{decrypted_msg}")

client_socket.close()

