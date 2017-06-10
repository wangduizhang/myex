#!/usr/bin/ python
#_*_coding:utf-8_*_
#将你的内容写入一个文件
from sys import argv
script,filename = argv

print "正在打开文件。。。"
target = open(filename,"w")

print "创建文件完成"
target.truncate()

print "现在请告诉我你想插入的内容："

line1 = raw_input("ine1:")
line2 = raw_input("ine2:")

print "我正在将你的内容写入文件"
target.write(line1+'\n'+line2+"\n")
print '去查看你的文件吧。'
target.close()