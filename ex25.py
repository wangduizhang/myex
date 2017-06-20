#_*_coding:utf-8

#麦乐鸡
def McNuggets(n):
	r = False
	for a in range(0,11):
		for b in range(0,11):
			for c in range(0,11):
				if 6 * a + 9 * b + 20 * c == int(n):
					r = True
	return r


print McNuggets(220)


#代码改错

def fixedPoint(f, epsilon):
    """
    f: a function of one argument that returns a float
    epsilon: a small float
  
    returns the best guess when that guess is less than epsilon 
    away from f(guess) or after 100 trials, whichever comes first.
    """
    guess = 1.0
    for i in range(100):
        if abs(f(guess) - guess) < epsilon:
            return guess
        else:
            guess = f(guess)
    return guess


def sqrt(a):
    def tryit(x):
        return 0.5 * (a/x + x)
    return fixedPoint(tryit, 0.0001)

#调用函数内部的函数

def babylon(a):
    def test(x):
        return 0.5 * ((a / x) + x)
    return test

def sqrt2(a):
    return fixedPoint(babylon(a), 0.0001)

print sqrt2(20)