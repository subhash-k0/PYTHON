from numpy import *

arr= array([1,2,3,4,5])
arr1= array([6,2,3,4,5])

arr2 = arr*5
print(arr+6)
print(arr)
print(arr2)

arr3 = arr+arr1+arr2
print(arr3)

print(sin(arr))
print(cos(arr))
print(tan(arr))
print(log(arr))
print(sqrt(arr))
print(sum(arr))
print(min(arr))
print(max(arr))
print(concatenate([arr,arr1]))

#//copying Array
 
Ar = array([2,6,8,1,3])
Ar2 = Ar
print(Ar) 
print(Ar2) 
print(id(Ar)) 
print(id(Ar2)) 

Ar3 =Ar.view()               #shalow copy
print(Ar3)
print(id(Ar3))                 
                               
Ar[1]=7                               
print(Ar)                   
print(Ar2)

Ar4= Ar.copy()           #Deep Copy
print(Ar4)