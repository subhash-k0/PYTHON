from unicodedata import numeric


# # numeric
#      -int
#      -float
#      -complex
#      -bool
#      -none

num1 = 5
num2 =4.5
num3 = 4+4j
num4 = 6
print(type(num1), type(num2), type(num3) )

# num1 = 6.7
print(type(num1))
print(num1/num2)
print(num1+num2)
print(num1+num4)
print('40+55')
num5 = int(num2)
print(type(num5), num5)

num6 = complex(num1,num2)
print(type(num6), num6)

num7 = complex(num1)
print(type(num7), num7)

n = 7>9
print(type(n), n)
print(int(True))
print(bool(True))
print(complex(True))
print(int(False))
print(float(True))

str ='navin'
print(type(str), str)

print(range(10))
r = range(0 ,10)
print(r)


print(list(range(10)))
print(list(range(0 ,10 ,2)))
print(list(range(0 ,10 ,2)))
print(type(list(range(10))))

d ={'navin':'samsung','rahul':'iphone','kiran': 'onepluse'}
print(type(d), d)
print(d['rahul'])
print(d.values())
print(d.get('kiran'))