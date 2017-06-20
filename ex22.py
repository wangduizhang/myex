def cifang(b,result):
        num  = 1
        for i in range(result):
            num *=  b
        return num
def mylog(x,b,result = 1):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    def cifang(b,result):
        num  = 1
        for i in range(result):
            num *=  b
        return num
    if cifang(b, result) == x:
        return result
    elif cifang(b, result) > x:
        return result - 1
    elif cifang(b,result) < x:
        return mylog(x, b, result+1)

print mylog(27, 3, result=1)