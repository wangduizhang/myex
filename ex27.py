def con(l1,l2):
    l3 = []
    s = True
    if len(l1) > len(l2):
        l = len(l2)
    else:
        l = len(l1)
        s = False
    for i in range(l):
        l3.append(l1[i])
        l3.append(l2[i])
        index = i
    index += 1
    if s:
        for i in range(len(l1) - index):
            l3.append(l2[index])
            index += 1
    else:
        for i in range(len(l2) - index):
            l3.append(l2[index])
            index += 1      

    return l3


l1 = [1,2,3]
l2 = ['a','b','c','d','e']
print "%s" % con(l1,l2)