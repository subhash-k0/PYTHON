def greet():
    print('Hello')
    print('Good Morning')

greet()
greet()

def add(x,y):
    c= x+y
    d = x-y
    # print(c)
    return c,d

x,y = int(input('enter')) ,  int(input('enter'))
print(x+y)
re, re1 = add(9,8)
print(re, re1)
print(add(8,7))
