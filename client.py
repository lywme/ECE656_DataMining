import socket
import sys
import pickle

obj=socket.socket()
obj.connect(('127.0.0.1',8888))
ret_bytes=obj.recv(1024)
ret_str=str(ret_bytes,encoding='utf-8')
print(ret_str)
print('Please input the corresponding Options to do DataMining:')
print('1> Rating Trend')
print('0> Exit')
while True:
    inp=input('Please input your choice:')
    if inp=='0':
        obj.sendall(bytes('0', encoding='utf-8'))
        obj.close()
        break
    elif inp=='1':
        obj.sendall(bytes(inp,encoding='utf-8'))
        while True:
            ret_bytes = obj.recv(1024)
            received
            if ret_bytes:
                received = received+ret_bytes
            else:
                break
        recdata=pickle.loads(received)
        print(recdata)
        obj.sendall(bytes('got it',encoding='utf-8'))
        # ret_bytes = obj.recv(1024)
        # ret_str = str(ret_bytes, encoding='utf-8')
        # xlen = int(ret_str)
print('Good Bye')
obj.close()