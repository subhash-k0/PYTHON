from numpy import *

arr1 = array([
                [1,2,3,12,11,10],
                [4,5,6,7,8,9]

          ])

arr2 =arr1.flatten()
arr3 =arr2.reshape(3,4)
print(arr1)
print(arr2)
print(arr3)
print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)
print(arr2.size)

arr4 =arr2.reshape(2,2,3)
print(arr4)
m = matrix(arr1)
print(m)

n= matrix('1 2 3 5 ; 4 5 6 7')
print(n)

mn= matrix('1 2 3; 5  4 5; 6 7 10')
mn2= matrix('1 2 3; 5  4 5; 6 7 10')
print(mn)
print(diagonal(mn))
print(mn.min())
print(mn.max())

add = mn+mn2
print(add)
print(mn * mn2)
