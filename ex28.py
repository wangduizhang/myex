#_*_coding:utf-8

def bb(n):
    a1 = 0
    a2 = 1
    l = [0,1]
    index = 2
    while len(l) < n:
        l.append(a1+a2)
        a1 = a2
        a2 = l[index]
        index += 1
    if n == 1:
        return [0]
    return l

n = 1000
print"前%d位:%s"%(n,bb(n))