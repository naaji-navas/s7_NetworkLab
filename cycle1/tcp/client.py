import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_address = ('127.0.0.1', 12345)

# Connect to the server
client_socket.connect(server_address)


try:
    input_numbers = input("Enter numbers seperated by space :")
    numbers = list(map(int, input_numbers.split()))
    numbers_str = ','.join(map(str, numbers))
    client_socket.send(numbers_str.encode())

    # Receive prime numbers from the server
    prime_numbers_str = client_socket.recv(1024).decode()
    prime_numbers = list(map(int, prime_numbers_str.split(',')))
    print(f"Prime numbers received from server: {prime_numbers}")
except socket.error as err:
    print(f"Socket error: {err}")
finally:
    # Close the socket
    client_socket.close()
    
    
    


# 1. Create a socket object
# 2. Define the server address and port
# 3. Connect to the server
# 4. Receive numbers from the user
# 5. Send numbers to the server
# 6. Receive prime numbers from the server
# 7. Close the socket

