#!/usr/bin/env python
#_*_coding:utf-8_*_
#读取一个文件的内容
from sys import argv

script, filename = argv

txt = open(filename)
print txt.read()
input()
