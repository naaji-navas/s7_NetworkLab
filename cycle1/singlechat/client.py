import socket

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((IP, PORT))

# Send the client's username to the server
username = input("Enter your username: ")
client_socket.send(username.encode('utf-8'))

while True:
    # Get a message from the user
    message = input(f'{username}: ')

    # Send the message to the server
    client_socket.send(message.encode('utf-8'))

    # Receive the message back from the server
    message = client_socket.recv(1024).decode('utf-8')

    # Print the message
    print(f'Server: {message}')