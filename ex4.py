#!/usr/bin/python
#_*_coding:utf-8_*_
#文件写入同一个新建文件
fname1 = raw_input('请输入你要合并的第一个文件：')
fname2 = raw_input('请输入你要合并的第二个文件：')
print '你要合并的文件是 %r 和 %r ？' % (fname1,fname2)
print '确认请点击回车键，否则Ctrl+z 退出。'
raw_input('>')
print '正在获取您的文件...'
file1 = open(fname1)
file2 = open(fname2)
txt1 = file1.read()
txt2 = file2.read()
print '获取文件内容成功！'
fname = raw_input('请输入你要生成的新文件名：')
newfile = open(fname,'w')
newfile.truncate()
newfile.write(txt1+"\n"+txt2)
print "你的文件生成成功，快去查看吧。"
newfile.close()
file1.close()
file2.close()