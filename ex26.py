#_*_coding:utf-8

def for_(l):
    s = 0
    for i in l:
        s += i
    return s
def while_(l):
    ll = len(l)
    index = 0
    s = 0
    while index < ll:
        s += l[index]
        index += 1
    return s


def dd(l,ll):
    if ll == 0:
        return l[0]
    else:
        return l[ll] + dd(l,ll-1)



#入口
l = []
while 1:
    """
    try:
        num = int(raw_input('你的数字:'))
    except ValueError as e:
        break
    l.append(num)
    """
    l= [1,2,3,4,5,6,7,8,9]
    ll = len(l)

    print "for:%d  whlie:%d  递归:%d" %(for_(l),while_(l),dd(l,ll-1))
    break



    
