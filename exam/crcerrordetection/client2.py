import socket
KEY = "1001"
def xor(a, b):
    result = []
    for i in range(1, len(a)):
        if a[i] == b[i]:
            result.append("0")
        else:
            result.append("1")
    return "".join(result)
  
def mod2div(data):
  cipher_len = len(KEY)
  cipher = data[0:cipher_len] # 