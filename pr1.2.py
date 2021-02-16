import math
x=int(input())
if (x < 28):
    f = x**3 + x**8 + 30
if (28 <= x < 46):
    f = 56 * x**2 - math.log(x) - 58
if (46 <= x < 85):
    f = x - x**6 + 91
if (85 <= x < 167):
    f = x**5 + math.exp(x) - 71
if (x >= 167):
    f = math.exp(x**6 + math.log(x) + (x**8)/53 + 27)
print("f({}) =".format(x),'%.3e'%(f))