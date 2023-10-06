import socket
import threading

# Create a socket for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Replace with the server's IP address
client_socket.connect(("127.0.0.1", 1234))

# Function to send messages to the server


def send_message():
    username = input("Enter your username: ")
    client_socket.send(username.encode("utf-8"))

    while True:
        recipient = input("Enter the recipient's username : ")
        if recipient.lower() == 'exit':
            client_socket.send("exit:".encode("utf-8"))
            break

        message = input("Enter your message: ")

        client_socket.send(f"{recipient}:{message}".encode("utf-8"))

# Function to receive messages from the server


def receive_messages():
    while True:
        message = client_socket.recv(1024).decode("utf-8")
        print(message)


# Create two threads for sending and receiving messages
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_messages)

send_thread.start()
receive_thread.start()
