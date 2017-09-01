#udp reserve
from socket import *
from time import ctime

host = ''
post = 3992
buffsize = 1024

useraddr = (host,post)

perserver = socket(AF_INET,SOCK_DGRAM)
perserver.bind(useraddr)

while True:
	data,addr = perserver.recvfrom(buffsize)
	perserver.sendto(("[%s]%s"%(ctime(),data)),addr)
perserver.close()

