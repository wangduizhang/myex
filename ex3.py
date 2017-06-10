#!/usr/bin/python
#_*_coding:utf-8_*_
#将某文件内容写入新建的文件
#这个功能的就是复制粘贴？
from sys import argv
script,filename = argv

readname = raw_input("请输入你要读取的文件名：")

txt = open(readname)

a = txt.read()

target = open(filename,'w')

target.truncate()

target.write(a)

target.close()