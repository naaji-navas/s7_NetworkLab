import socket
import threading

# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server_socket.bind(("127.0.0.1", 1234))
server_socket.listen(500)

# Dictionary to store connected clients and their usernames
connected_clients = {}
client_lock = threading.Lock()

# Function to broadcast a message to all clients
def broadcast(message, sender=None):
    with client_lock:
        for client, _ in connected_clients.items():
            if client != sender:
                try:
                    client.send(message.encode("utf-8"))
                except Exception as e:
                    print(f"Error sending message to a client: {str(e)}")
                    client.close()
                    del connected_clients[client]

# Function to handle a client's connection
def handle_client(client_socket):
    try:
        # Receive the username from the client
        username = client_socket.recv(1024).decode("utf-8")
        with client_lock:
            connected_clients[client_socket] = username
        broadcast(f"{username} has joined the chat.")

        while True:
            message = client_socket.recv(1024).decode("utf-8")
            recipient, message = message.split(':', 1)

            if recipient.lower() == 'exit':
                break  # Client wants to change recipient

            found = False
            with client_lock:
                for client, client_username in connected_clients.items():
                    if client_username == recipient:
                        try:
                            client.send(f"{username}: {message}".encode("utf-8"))
                            found = True
                            break
                        except Exception as e:
                            print(f"Error sending message to {recipient}: {str(e)}")

            if not found:
                client_socket.send(f"User '{recipient}' does not exist.".encode("utf-8"))

    except Exception as e:
        print(f"Error: {str(e)}")

    finally:
        with client_lock:
            if client_socket in connected_clients:
                username = connected_clients[client_socket]
                del connected_clients[client_socket]
                broadcast(f"{username} has left the chat.")
                client_socket.close()

# Main server loop
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
