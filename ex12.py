#!/usr/bin/python
#_*_coding:utf-8_*_
#求曲线与坐标轴围成的面积
def f(x):
    y = x*x
    return y


def radiationExposure(start, stop, step):
    exact = float(stop-start)/step
    result = 0
    for i in range(step):
        area = exact * max(f(start+exact),f(start+exact))
        result += area
        start += exact        
    return result

print radiationExposure(5, 10,1000000)