import socket

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num//2 + 1): 
        if num % i == 0:
            return False
    return True

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
host = '127.0.0.1'
port = 12345

# Bind the socket to the server address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)
print("Socket is listening...")

while True:
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Receive numbers from the client
    numbers_str = client_socket.recv(1024).decode()
    numbers = list(map(int, numbers_str.split(',')))

    # Find prime numbers among the received numbers
    prime_numbers = [num for num in numbers if is_prime(num)]
    prime_numbers_str = ','.join(map(str, prime_numbers))

    # Send prime numbers back to the client
    client_socket.send(prime_numbers_str.encode())

    # Close the client socket
    client_socket.close()



# 1. Create a socket object
# 2. Define the server address and port
# 3. Bind the socket to the server address and port
# 4. Listen for incoming connections
# 5. Accept a connection from a client
# 6. Receive numbers from the client
# 7. Find prime numbers among the received numbers
# 8. Send prime numbers back to the client
# 9. Close the client socket
# 10. Close the server socket
