import math
n = int(input())
def f(n):
    if n == 0:
        return 9
    else:
        return 1/57 * f((n-1))**2 - math.tan(f(n-1))
f1 = f(n)
print("f({})=".format(n),'%.3e'%(f1))