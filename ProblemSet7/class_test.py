#_*_coding:utf-8
class testfather(object):
	"""docstring for testfather"""
	def __init__(self, name):
		self.name = name
	def print_(self):
		print self.name

class testson(testfather):
	"""docstring for testson"""
	def print_(self):
		print self.name