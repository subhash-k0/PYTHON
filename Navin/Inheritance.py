class A:
    def feature(self):
        print("Feature 1 Working")

    
    def feature2(self):
        print("Feature 2 Working")    

class B():
    
    def feature3(self):
        print("Feature 3 Working")

    
    def feature4(self):
        print("Feature 4 Working")    
class C(B):
    
    def feature5(self):
        print("Feature 5 Working")

class D(A,C,B):
    
    def feature6(self):
        print("Feature 6 Working")


a1 = A()

a1.feature()
a1.feature2()

b1 = B()

c1 = C()
c1.feature5()
# c1.feature()

d1 = D()
d1.feature()
d1.feature2()
d1.feature3()
d1.feature4()
d1.feature5()
d1.feature6()