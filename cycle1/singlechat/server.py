import socket

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the socket options
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to a specific IP and port
server_socket.bind((IP, PORT))

# Listen for incoming connections
server_socket.listen()

# Accept a single client connection
client_socket, client_address = server_socket.accept()

# Receive the client's username
username = client_socket.recv(1024).decode('utf-8')

print(f'{username} has connected.')

while True:
    # Receive a message from the client
    message = client_socket.recv(1024).decode('utf-8')

    # If the message is empty, the client has disconnected
    if not message:
        print(f'{username} has disconnected.')
        break

    # Print the message and send it back to the client
    print(f'{username}: {message}')
    
    # Get a message from the server
    server_message = input('Server: ')

    # Send the message to the client
    client_socket.send(server_message.encode('utf-8'))