class student:

    school = 'Telusko'

    def __init__(self,m1,m2,m3):
        self.m1 =  m1
        self.m2 =  m2
        self.m3 =  m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    def get_m1(self):
        return self.m1

    def set_m1(self, value):
        self.m1 = value
    
    @classmethod      #Decorators
    def info(cls):
        return cls.school        

    @staticmethod
    def info2():
        print('This is class')    

s1 = student(34,47,32)
s2 = student(89,32,12)

print(s1.avg())
print(s2.avg())

print(student.info())

student.info2()

# Accessor Methods
# Mutator Methods