#!/usr/bin/python
#_*_coding:utf-8_*_
#生成器练习：生成素数
#我的v1.0：

def genPrimes1():
	num = 2
	while True:
		for i in range(2,num+1):
			if num == 2:
				yield 2
				num += 1				
			elif num % i == 0:
				num += 1
				break
			elif num % i != 0 and num-1 == i:
				yield num
				num += 1
				break

#改改
def genPrimes2():
	num = 1
	while True:
		num += 1
		for i in range(2,num+1):
			if num == 2:
				yield 2							
			elif num % i == 0:
				break
			elif num % i != 0 and num-1 == i:
				yield num
				break




#老师的

def genPrimes():
	primes = []   # primes generated so far
	last = 1      # last number tried
	while True:
		last += 1
		for p in primes:
			if last % p == 0:
				break
		else:
			primes.append(last)
			yield last
######注释：当for语句中没有执行break的话，遍历完for语句，就会执行else语句 但是如果中间执行了break语句，跳出for循环，那么不会执行else语句。