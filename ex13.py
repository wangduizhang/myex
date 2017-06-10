#!/usr/bin/python
#_*_coding:utf-8_*_
#在函数内对列表使用del时，函数改变了传递的列表
#归并排序的写法，我自己与老师的



def bingui(a1,a2,a3):
	if len(a1) == 0:
		a3.append(a2)
		return a3
	elif len(a2) == 0:
		a3.append(a1)
		return a3
	else:
		if a1[0] <= a2[0]:
			a3.append(a1[0])
			del a1[0]
			return bingui(a1, a2, a3) 
		else:
			a3.append(a2[0])
			del a2[0]
			return bingui(a1, a2, a3) 
			

def merge(a1,a2):
	i = 0
	j = 0
	result = []
	while i < len(a1) and j <len(a2):
		if a1[i] <= a2 [i]:
			result.append(a1[i])
			i += 1
		else:
			result.append(a2[j])
			j += 1
	while i <len(a1):
		result.append(a1[i])
		i += 1
	while j <len(a2):
			result.append(a2[j])
			i += 1
	return result




a = [21,156,48,44,121,85,2,8,45,121,45,1212,484,1,48,21,454,121,4,12,4,2,4,21,4,12,12,44,84]
n = len(a)/2
a1 = sorted(a[0:n])
a2 = sorted(a[n:len(a)])
a3 = []


print merge(a1, a2)
print bingui(a1, a2, a3)