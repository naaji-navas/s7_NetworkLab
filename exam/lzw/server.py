import socket
import pickle
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address=('127.0.0.1',9003)

server_socket.bind(server_address)

server_socket.listen(5)
print("Server is up and listening")

client_socket,client_address = server_socket.accept()



def compress(msg):
  table={chr(i):i for i in range(256)}
  print(table)
  code=256
  output_codes=[]
  p=msg[0]
  for i in range(len(msg)):
    if(i<len(msg)-1):
      c=msg[i+1]
    if(p+c in table):
      p=p+c
    else:
      output_codes.append(table[p])
      table[p+c]=code
      code+=1
      p=c
      c=' '
  output_codes.append(table[p])
  print(output_codes)
# compress(msg)
msg = (client_socket.recv(1024).decode())
print(f"The data recived is {(msg)}")
compress(msg)

server_socket.close()
client_socket.close()