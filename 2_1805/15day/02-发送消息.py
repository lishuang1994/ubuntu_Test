from socket import *
s = socket(AF_INET,SOCK_DGRAM)#创建一个udp的套接字
s.sendto("往后余生,心里温柔是你".encode("gb2312"),("192.168.43.9",8888))
s.close()
