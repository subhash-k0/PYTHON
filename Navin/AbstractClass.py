#ABC-> abstract Base Classes
#Abstract class does not support by default
#can't make Object of Abstract class

from abc import ABC, abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self):
        # print("Running")
        pass

class Laptop(computer):    #if method id not define it give Error
    def process(self):
        print("its running")

# class whiteboard(computer):
#     def write(self):
#         print("its writing")
        

class Programmer:
    def work(self, com):
        print("solving Bugs")
        com.process()        

# com = computer()
# com.process()

com1 = Laptop()  
com1.process()

# comp2 = whiteboard()

prog1 = Programmer()
prog1.work(com1)
# prog1.work(comp2)   # give error if dont have process() method