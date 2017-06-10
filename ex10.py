#!/usr/bin/python
#_*_coding:utf-8_*_
def lenRecur(aStr):
	if aStr == '':
		return 0
	else:
		return 1+lenRecur(aStr[1:])

s = raw_input('>')
print lenRecur(s)