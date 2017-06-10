#!/usr/bin/python
#_*_coding:utf-8_*_
#欧几里得算法，辗转相除，求两数最大公约数
def gcd(a, b):
	if a % b == 0:
		return b
	else:
		return gcd(b, a % b)
	print b		