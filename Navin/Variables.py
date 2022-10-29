x = 2
y = 222

print(x,y,x+y,x*y,y/x,y**x,y%x)

print(x**3,)

name ='''hello 
  duniya'''

name2= r"my world\nhome"
print(name ,name2, name+name2)

name3= 'rocks'
print(name3[2])
print(name3[0])
print(name3[1])
print(name3[-1])
print(name3[-2])
print(name3[0:2])
print(name3[1:4])
print(name3[:4])
print(name3[1:])
print(name3[3:10])
print(name3[1:6:2])

name4 = 'youtube'
print(name4[0:3])
print(name4[3:10])
# name4[0:3]='my'
# print(name4)   this will not work(string in python is immtable)

print('my '+name4[0:3])
print('my '+name4[3:])
print(len(name4))
print(type(name4))
