from heapq import merge


data = {1:'Navin',2:'Karn',4:'Harsh'}
print(type(data), data)
print(data[2])
print(data[(2)])

print(data.get(1))
print(data.get(3,'Not Found'))
print(data.get(1,'Not Avil'))

keys = ['Navin','Kiran','Harsh']
values= ['Python','Java','Js']
data1 = dict(zip(keys,values))
data2 = set(zip(keys,values))
data3 = set(merge(keys,values))
print(data3)
print(data1)
print(data2)
print(type(data),type(data2))
print(data1['Navin'])

data1['Navin'] = 'html'
print(data1)


prog = {'JS':'Atom','CS':'VS','Python':['Pycharm','Suublime'], 'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}

print(type(prog), prog)
print(prog['JS'])
print(prog['Python'])
print(prog['JS'][1])
print(prog['Python'][1])

print(prog['Java'])
print(prog['Java']['JEE'])



