import socket
import numpy as np

def mod2div(divident, divisor):
    quotient = np.bitwise_and(int(divident, 2), int(divisor, 2))
    return format(quotient, 'b')

def decode_data(data, key):
    l_key = len(key)
    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)
    return remainder

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 12345)
server_socket.bind(server_address)

server_socket.listen(5)
print("Server is waiting for client request")

while True:
    client_socket, client_address = server_socket.accept()
    print("Connection from", client_address)
    
    data = client_socket.recv(1024).decode()
    print("Data from client", data)

    key = "1001"

    ans = decode_data(data, key)
    print("Remainder is", ans)

    temp = "0" * (len(key) - 1)

    if ans == temp:
        print("No error")
        client_socket.send(("Thank you. Data received " + data + " with no error").encode())
    else:
        print("Error")
        client_socket.send("Error in data".encode())

    client_socket.close()
