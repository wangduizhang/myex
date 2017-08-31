def maxmax(l):
    index = 0
    s = ''
    l2 = []
    for i in range(len(l)):
        l2.append(i)
    while index < len(l):
        max = 0
        for i in l:
            ii = str(i)
            if ii in l2:
                continue;
            if str(i)[0] > max:
                max = ii[0]
                l2[index] = ii
        index += 1
    for i in l2:
        s += str(i)
    s = int(s)
    return s


l = [50,2,1,9]
print "%s" % maxmax(l)

