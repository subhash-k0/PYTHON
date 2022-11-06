a,b = 5,6
print(a+b)
print(int.__add__(a,b))
print(int.__sub__(a,b))
print(int.__mul__(a,b))

x,y = 'Hello','World'
print(str.__add__(x,y))

class student:

    def __init__(self, m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):
        m1 = self.m1 +other.m1   
        m2 = self.m2 +other.m2
        s3 = student(m1,m2)  
   
        return s3

    def __gt__(self,other):
        r1 = self.m1 + other.m1
        r2 = self.m2 + other.m2
        if(r1>r2):
            return True

    def __str__(self):
        # return self.m1, self.m2       
        return '{} {}'.format(self.m1, self.m2) 

s1 = student(58,69)
s2 = student(60,10)

s3 = s1 + s2
print(s3.m1)
print(s3.m2)

if s1 > s2:
    print('s1 wins')
else:
    print('s2 wins')    

a=10
print(a)
# print(s1)      it show Address of s1
print(a.__str__())
print(s1.__str__())
print(s2)