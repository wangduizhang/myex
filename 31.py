#_*_coding:utf-8

#这是一个tcp服务器

from socket import *
from time import ctime

host = ''
post = 3956
buffsize = 1024
USERadd = (host,post)

perserver = socket(AF_INET,SOCK_STREAM)
perserver.bind(USERadd)
perserver.listen(3)

while True:
    tcpcilsock,addr = perserver.accept()
    while True:
        print "ok.."
        data = tcpcilsock.recv(buffsize)
        if not data:
            break
        tcpcilsock.send("[%s]%s"%(ctime(),data))
    tcpcilsock.close()
perserver.close()


