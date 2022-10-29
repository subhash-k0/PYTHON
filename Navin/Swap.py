"""Swap 1st method"""

from tempfile import tempdir


a,b = 5,6
print(a)
print(b)
temp = a
a = b
b= temp
print(a)
print(b)
print('\n')

#2nd method
a ,b= 10, 20
print(a)
print(b)
a=a+b
b=a-b
a=a-b
print(a)
print((b),'\n')

#3rd method
a ,b= 100, 200
print(a)
print(b)
a=a^b
b=a^b
a=a^b
print(a)
print((b),'\n')

#4th method
a,b =500, 350
print(a)
print(b)
a,b =b,a
print(a)
print(b)