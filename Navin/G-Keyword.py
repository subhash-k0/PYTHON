a= 10

def something():
    a=20            #local variable
    b=13
    print(a,b)

print(a)  #here it print global varible a=10    
# print(b)   not work becoz b is local variable

a=10
def somr():

    print("in fun ", a)  #call global variable

#how to modify global variable in function

a=10
def s():
    global a
    a=15
    print('in function ', a)

s()  #if not call value is not modify
print(a)


# to use global and local variable in same function

a =10
print(id(a))

def gl():
    a=9

    x=globals()['a']
    print(id(x))
    print('in funct ',a)
    globals()['a'] = 15