#udp user
from socket import *


host = 'localhost'
post = 3992
buffsize = 1024

addr = (host,post)
user_post = socket(AF_INET,SOCK_DGRAM)

while True:
    data = raw_input("char:")
    user_post.sendto(data,addr)
    data,addadd = user_post.recvfrom(buffsize)
    if not data:
        break
    print data

user_post.close()
