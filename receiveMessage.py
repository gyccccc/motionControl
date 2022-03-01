import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("192.168.1.152", 11111))
count = 0
while 1:
    data = s.recv(4096)
    print(data)
    count = count+1
    print(count)
