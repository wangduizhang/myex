#!/usr/bin/python
#_*_coding:utf-8_*_
#面向对象编程
#__init__初始化以最后一次调用为初始
#而其他方法的继承以第一个集成为初始
class A(object):
	def __init__(self):
		self.a = 1
	def x(self):
		print "A.x"
	def y(self):
		print "A.y"
	def z(self):
		print "A.z"

class B(A):
	def __init__(self):
		A.__init__(self)
		self.a = 2
		self.b = 3
	def y(self):
		print "B.y"
	def z(self):
		print "B.z"

class C(object):
	def __init__(self):
		self.a = 4
		self.c = 5
	def y(self):
		print "C.y"
	def z(self):
		print "C.z"

class D(C, B):
	def __init__(self):
		C.__init__(self)
		B.__init__(self)
		self.d = 6
	def z(self):
		print "D.z"

print D().z()