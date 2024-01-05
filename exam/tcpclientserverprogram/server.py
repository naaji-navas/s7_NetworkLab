import socket


def is_prime(num):
  if num <= 1:
    return False
  for i in range(2, num):
    if num % i == 0:
      return False
  return True


def main():
  server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  
  # define the server host and port
  host = '127.0.0.1'
  port = 12345
  
  # now bind the socket to the host and the port
  server_socket.bind((host, port))
  
  # listen for incoming connections
  server_socket.listen(5)
  print('Server is listening on port:', port)
  
  
  while True: # this while is for accepting multiple connections
    # accept connection from client
    client_socket, client_address = server_socket.accept()
    
    # recive the data from the client
    data = client_socket.recv(1024).decode()
    #chek if the data is a prime number
    
    if is_prime(int(data)):
      print('The number', data, 'is a prime number')
      client_socket.send('True'.encode())
    else:
      print('The number', data, 'is not a prime number')
      client_socket.send('False'.encode())
    client_socket.close() # close the connection with the client
    
  server_socket.close() # close the server socket
  
if __name__ == '__main__':
  main()
  
  