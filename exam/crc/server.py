import socket
import pickle
key = '1101'
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address=('127.0.0.1',6000)

server_socket.bind(server_address)

server_socket.listen(5)

client_socket,client_address = server_socket.accept()
print("Server is up and listening")


def xor(a,b):
  result = ''
  for i in range(1,len(b)):
    if(a[i]==b[i]):
      result+='0'
    else:
      result+='1'
  return result

def mod2div(key,msg):
  length = len(key)
  pick = msg[0:length]
  while(length <len(msg)):
    if(pick[0] == '1'):
      pick = xor(pick,key) + msg[length]
    else:
      pick = xor(pick,'0'*length) + msg[length]
  if(pick[0] == '1'):
    pick = xor(pick,key) 
  else:
    pick = xor(pick,'0'*length) 
  print(pick)
  return pick
mod2div('1101','100100000')


 



msg = (client_socket.recv(1024).decode())

server_socket.close()
client_socket.close()