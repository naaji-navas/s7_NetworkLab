import socket
import threading

# Create a socket for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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
                            client.send(
                                f"{username}: {message}".encode("utf-8"))
                            found = True
                            break
                        except Exception as e:
                            print(
                                f"Error sending message to {recipient}: {str(e)}")

            if not found:
                client_socket.send(
                    f"User '{recipient}' does not exist.".encode("utf-8"))

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
    client_thread = threading.Thread(
        target=handle_client, args=(client_socket,))
    client_thread.start()


# Import the socket and threading modules.
# Create a new TCP socket object for the server.
# Set the socket option SO_REUSEADDR to 1 to allow the socket to be reused immediately after it is closed.
# Bind the socket to the IP address 127.0.0.1 and port number 1234.
# Set the maximum number of queued connections to 500.
# Create an empty dictionary to store connected clients and their usernames.
# Create a new lock object to synchronize access to the dictionary.
# Define a function broadcast() to send a message to all connected clients except the sender.
# Define a function handle_client() to handle a client's connection.
# Receive the username from the client and add the client's socket and username to the dictionary of connected clients.
# Broadcast a message to all connected clients to announce that a new client has joined the chat.
# Receive messages from the client and split them into a recipient and message.
# If the recipient is "exit", break out of the loop to allow the client to change the recipient.
# Search for the recipient in the dictionary of connected clients and send the message to the recipient if found.
# If the recipient is not found, send an error message to the client.
# If an error occurs while sending a message, print an error message and remove the client from the dictionary of connected clients.
# When the client disconnects, remove the client from the dictionary of connected clients and broadcast a message to all connected clients to announce that the client has left the chat.
# Start a new thread to handle each client's connection.
# Repeat steps 17-18 for each new client that connects to the server.
##
