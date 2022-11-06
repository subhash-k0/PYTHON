f= open('Navin/MyData','r')

print(f.read())
print(f.readline(), end ="")
print(f.readline(4))

f= open('Navin/MyData','a')
f= open('Navin/MyData','rb')


f1 = open('MyData2','r')

# f1.write("something")

print(f1)

# f2 = open("Navin/MyData.txt",'r')
# print(f2.read())
# f2 = open("Navin/MyData.txt",'w')
# f2.write('my new data')

f2 = open("Navin/MyData.txt",'a')
f2.write('write with function')
f2 = open("Navin/MyData.txt",'r')
print(f2.read())

# for data in f1:
#     print(data)


for data in f2:
    f.write(data)    