import sys

print(sys.getrecursionlimit())
# print(sys.getrecursionlimit(2000))  if want to change limit

i =0
def greet():   # maximuum recurtion is 1000times by Default
    global i
    i+=1
    print('hello', i)
    greet()
    

greet() 