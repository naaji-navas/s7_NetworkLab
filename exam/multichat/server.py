#server
import socket
import threading

clients = {}  # Dictionary to store client sockets and names

def handle_client(client_socket, client_name):
    global clients
    try:
        while True:
            message = client_socket.recv(1024).decode()
            if message.lower() == "exit":
                print(f"Client {client_name} exited the chat.")
                break

            print(f"Message from {client_name}: {message}")

            # Broadcast the message to all other clients
            for name, socket in clients.items():
                if name != client_name:
                    try:
                        socket.send(f"{client_name}: {message}".encode())
                    except:
                        # Remove the client if unable to send the message
                        del clients[name]
                        print(f"Client {name} disconnected.")
                        break
    except:
        # Remove the client if an error occurs
        del clients[client_name]
        print(f"Client {client_name} disconnected.")

    # Close the connection
    client_socket.close()

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address=('127.0.0.1',12345)


# Bind the socket to the server address and port
server_socket.bind(server_address)

print("Server is listening...")

# Listen for incoming connections
server_socket.listen()

try:
    while True:
        # Accept a new client connection
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Get the client name
        client_name = client_socket.recv(1024).decode()

        # Add the client to the dictionary
        clients[client_name] = client_socket

        # Notify all clients about the new connection
        for name, socket in clients.items():
            if name != client_name:
                try:
                    socket.send(f"{client_name} joined the chat.".encode())
                except:
                    # Remove the client if unable to send the message
                    del clients[name]
                    print(f"Client {name} disconnected.")

        # Start a new thread to handle the client
        threading.Thread(target=handle_client, args=(client_socket, client_name)).start()
finally:
    # Close all client connections
    for name, socket in clients.items():
        socket.close()

    # Close the server socket
    server_socket.close()
