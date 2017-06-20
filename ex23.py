# _*_coding:utf-8

def laceStringd(s1, s2):
    """
    s1,s2 交替连接(迭代实现)
    """ 
    a = 1
    result = ''
    for i in range(len(s1+s2)):
        if a % 2 != 0:
            result += s1[0]
            s1 = s1[1:len(s1)]
            a += 1
            if len(s1) == 0:
                result += s2
        elif a % 2 == 0:
            result += s2[0]
            s2 = s2[1:len(s2)]
            a += 1
            if len(s1) == 0:
                return result + s1


def laceStringd1(s1, s2):
    """
    s1,s2 交替连接(递归实现)
    """ 
    if len(s1) == 0 and len(s1) != len(s2):
        return s2
    elif len(s2) == 0 and len(s1) != len(s2):
        return s1
    elif len(s1) == len(s2) and s1 == 0:
        return None
    else:
        return s1[0] + laceStringd(s2,s1[1:len(s1)])


def laceStringd2(s1, s2):
    """
    s1,s2 按顺序连接
    """ 
    if len(s1) == 0 and len(s1) != len(s2):
        return s2
    elif len(s2) == 0 and len(s1) != len(s2):
        return s1
    elif len(s1) == len(s2) and s1 == 0:
        return None
    else:
        if s1[0] <= s2[0]:
            return s1[0] + laceStringd(s1[1:len(s1) + 1], s2)
        elif s1[0] > s2[0]:
            return s2[0] + laceStringd(s1, s21[1:len(s1) + 1])

s1 = 'abcd'
s2 = 'efghi'
print laceStringd(s1, s2)