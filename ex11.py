#!/usr/bin/python
#_*_coding:utf-8_*_
#二分法查找字符串中是否含有某字符，并打印
def isIn(char,aStr):
	if aStr == '':
		return False
	if len(aStr)==1:
		if char==aStr[0]:
			return True
		else:
			return False
	midd= len(aStr)/2
	if len(aStr)%2<>0:
		if char == aStr[midd]:
			return True
		else:
			return isIn(char, aStr[:midd]) or isIn(char, aStr[midd:])
	else:
		return isIn(char, aStr[:midd]) or isIn(char, aStr[midd:])
	
	
char = raw_input('char:')
aStr = raw_input('aStr:')
print isIn(char, aStr)