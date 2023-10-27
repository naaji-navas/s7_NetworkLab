import socket


def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)


def mod2div(divident, divisor):
    pick = len(divisor)
    tmp = divident[0:pick]

    while pick < len(divident):

        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + divident[pick]

        else:
            tmp = xor('0' * pick, tmp) + divident[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    checkword = tmp
    return checkword


def decodeData(data, key):
    l_key = len(key)

    appended_data = data + '0' * (l_key - 1)
    remainder = mod2div(appended_data, key)

    return remainder


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")

PORT = 12345

s.bind(('', PORT))

print(f"socket binded to %s" % (PORT))

s.listen(5)
print("socket is listening")

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    print("Receiving data...")
    data = c.recv(1024)

    print(" Recivied encoded in binary format : ", data.decode())

    if not data:
        break

    key = "1001"
    ans = decodeData(data.decode(), key)
    print("Remainder after decoding is->" + ans)

    temp = "0" * (len(key) - 1)
    if ans == temp:
        c.send(b"THANK you Data ->" + data + b" is correct")
    else:
        c.send(b"Bad Data ->" + data + b" is incorrect")
    c.close()
