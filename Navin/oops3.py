class computer:

    def __init__(self):
        self.name = "Navin"
        self.age =28

    def update(self):
        self.age = 30    

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False
                  

c1 = computer()
c2 = computer()

print(id(c1), id(c2))

c1.name = "Rahul3"
c1.age = 20

# if c1==c2:
#     print('They are same')      not work

if c1.compare(c2):
    print('exectly same')
else:
    print('different')        

# c1.update()

print(c1.name)
print(c2.name)