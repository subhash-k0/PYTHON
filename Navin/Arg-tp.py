def add(a,b):   # a,b -> Formal Argument
    c=a+b
    print(c)

add(5,6)          #5,6 -> Actual Argument

# position
# Keyword
# Default
# Variable Length

def person(name, age=18):  # Default value
    print(name)
    print(age)
    print(age-5)

# person('navin', 20)  #position
# person(20,'navin')  #position

person(name='navin', age=20) #keyword

def sum(*b):
    c = 0

    for i in b:
        c = c+i

    print(c)    
    
sum(5,6,34,78)