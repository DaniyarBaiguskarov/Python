import math
x=int(input())
y=int(input())
z=int(input())
f=9 * (x**4)+41 * (y**5)-36+((math.exp(y) - z**6)**0.5)/((z**7 - y**8)**0.5) - (abs(z) - math.exp(y))/(abs(x) - 12 * (z**4))
print("f({},{},{})=".format(x,y,z),'%.3e'%(f))