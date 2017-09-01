#_*_coding:utf-8
#这是一个tcp客户端

from socket import *

host = 'localhost'
post = 3956
datasize = 1024
useraddr = (host,post)

tcpclisock = socket(AF_INET,SOCK_STREAM)
tcpclisock.connect(useraddr)

while True:
	data = raw_input('字符：')
	if not data:
		break
	tcpclisock.send(data)
	data = tcpclisock.recv(datasize)

	if not data:
		break
	print data

tcpclisock.close()
