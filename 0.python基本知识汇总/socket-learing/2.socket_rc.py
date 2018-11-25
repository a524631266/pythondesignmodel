from socket import socket,AF_INET,SOCK_DGRAM


socket = socket(family=AF_INET,type=SOCK_DGRAM)
# 183.156.105.130
socket.bind(("localhost",8002))
while True:
    data,iphost = socket.recvfrom(1024)
    print(data.decode("utf-8"),iphost)