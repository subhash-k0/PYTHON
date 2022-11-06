from array import *

Arr = array('i',[])

n= int(input("Enter the lenghtof the Array = "))

for i in range(n):
    x = int(input("Enter the Element = "))
    Arr.append(x)
print(Arr)

val = int(input("Enter the search item = "))

for e in Arr:
    if e==val:
        print("yes")
        break
    print(Arr.index(val))
print("not available")