#!/usr/bin/python
#_*_coding:utf-8_*_
#将指定文件的内容写入指定文件,源文件内容清除，可建立新文档
def get_file(from_):
	txt = open(from_).read()
	return txt

def writ_file(to,from_):
	w_file = open(to,'w').write(get_file(from_))
	

print "请输入你要获取的文件："
from_file = raw_input(">>>")

txt = get_file(from_file)

#无用的一句
if txt == None:
	print "获取文件失败！请确认你输入的文件名！"
else :
	print "获取文件成功！"
#

print "请输入你要写入的文件："
to_file = raw_input(">>>")

writ_file(to_file,from_file)

print "写入成功"



	