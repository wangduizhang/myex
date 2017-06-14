#!/usr/bin/python
#_*_coding:utf-8_*_
#麦乐鸡只有6，9，20块套餐
def McNuggets(n):
	for a in range(0,11):
		for b in range(0,11):
			for c in range(0,11):
				if 6 * a + 9 * b + 20 * c == int(n):
					return 'True, %s, %s, %s' % (a, b, c)


for i in range(1,100):
	if  McNuggets(i):
		print i, McNuggets(i)
					