#_*_coding:utf-8


def hb(l1,l2):
    l3 = []
    for i in l1:
        for j in l2:
            l3.append(i+j)
    return l3


def  del_(l):
    index = 0
    if not ('+' in l or '-' in l):
        return int(l[0])
    else:
        for i in l:
            if i == '+':
                return int(l[:index]) + del_(l[index+1:])
            elif i == '-':
                return int(l[:index]) - del_(l[index+1:])            
            index += 1

l = ['1','2','3','4','5','6','7','8','9']
l2 = []
for n in l:
    if n == '9':
        l2.append(n)
        break
    l2.append(n)
    for o in ['+','-',]:
        l2.append(n + o)
l3 = []
for i in hb(hb(hb(l2[0:3],l2[3:6]),hb(l2[6:9],l2[9:12])),hb(hb(l2[12:15],l2[15:18]),hb(l2[18:21],l2[21:24]))):
    l3.append(i+'9')

for i in l3:
    s = del_(i)
    if s == 100:    
        print "%s = %d" % (i,100)



        
    