from socket import socket,AF_INET,SOCK_DGRAM


socket = socket(family=AF_INET,type=SOCK_DGRAM)

socket.bind(("localhost",8003))
while True:
    info = input("输入信息:")
    socket.sendto(info.encode("utf-8"),("localhost",8002))
