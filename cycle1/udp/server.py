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
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# define the server address and port address
host = '127.0.0.1'
port = 12345

# Bind the socket to the server address and port
server_socket.bind((host, port))

print("Socket is listening...")

while True:
    # Receive numbers from the client
    numbers_str, client_address = server_socket.recvfrom(1024)
    numbers = list(map(int, numbers_str.decode().split(',')))

    # Find prime numbers among the received numbers
    prime_numbers = [num for num in numbers if is_prime(num)]
    prime_numbers_str = ','.join(map(str, prime_numbers))

    # Send prime numbers back to the client
    server_socket.sendto(prime_numbers_str.encode(), client_address)
    
    # Close the server socket
    server_socket.close()
    