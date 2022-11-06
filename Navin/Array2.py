from numpy import *

arr = array([1,2,3,4,5,6],int)
arr = array([1,2,3,4,5,6])
print(arr)
print(arr.dtype)
print(type(arr))

arr = array([1,2,3,4,5,6],float)
print(arr)
print(arr.dtype)
print(type(arr))

# way to creating Array
# -> array()
# -> linspace()
# -> logspace()
# -> arange()
# -> zeros()
# -> ones()

ar = linspace(0,16,10)
print(ar)

a=arange(1,15,2)
print(a)

am = logspace(1,40,5)
print(am)
print('%.2f' %am[0])

az = zeros(5)
print(az)

ao = ones(5)
print(ao)

ao1 = ones(5,int)
print(ao1)