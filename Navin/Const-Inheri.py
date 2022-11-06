#construction in inheritance
# note - super alway left to right / top to down (method revolution order)

class A:

    def __init__(self):
        print("in A Init")

    def feature(self):
        print("Feature 1 Working")

    
    def feature2(self):
        print("Feature 2 Working")    

class B():

    def __init__(self):
        super().__init__()
        print("in B Init")

    
    def feature3(self):
        print("Feature 3 Working")        

    
    def feature4(self):
        print("Feature 4 Working")    

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C Init")        


a1 = A()
a1.feature()

b1 = B()
b1.feature3()

c1 = C()