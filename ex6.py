#!/usr/bin/python
#_*_coding:utf-8_*_
#分别使用range和while求和

a = int(raw_input("a = "))
b = int(raw_input("b = "))

ws = 0
fors = 0

#while部分
'''
while a <= b:
	ws += a
	a += 1
	
print "while求和 %d" % ws 
'''	 

for n in range(a,b+1):
	fors += n   

print "for求和 %d" % fors
