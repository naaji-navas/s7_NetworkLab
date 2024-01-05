import socket

def is_prime(num):
  if num <= 1:
    return False
  for i in range(2, num):
    if num % i == 0:
      return False
  return True


# create a socket object
server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# here we used socket.AF_INET for IPv4 and socket.SOCK_DGRAM for UDP
# define the server host and port
host = '127.0.0.1'
port = 12345

# now bind the socket to the host and the port
server_socket.bind((host,port))
server_socket.listen(5)
print('Server is listening on port:', port)

while True:
  data , client_address = server_socket.recvfrom(1024)
  if is_prime(int(data)):
    print('The number', data, 'is a prime number')
    server_socket.sendto('True'.encode(),client_address)
  else:
    print('The number', data, 'is not a prime number')
    server_socket.sendto('False'.encode(),client_address)
  server_socket.close() # close the connection with the client
  