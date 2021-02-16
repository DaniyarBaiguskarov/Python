import math
n = int(input())
m = int(input())
a = 0
b = 0
for i in range (1, n + 1):
    for j in range (1, m + 1):
        a = a + (9 * i**4 + 41 * j**5 - 36)
        b = b + (math.exp(j) - j**4)
f = a / 91 - b
print("f({},{})=".format(n, m),'%.3e'%(f))