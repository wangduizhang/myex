#!/usr/bin/python
#_*_coding:utf-8_*_
#函数：最大公约数


def gcd(a, b):
	m = min(a, b)
	while a % m != 0 and b % m != 0:
		m -= 1
		return m