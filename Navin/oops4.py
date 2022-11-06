# variable
#->instance variable
#->class[Static] variable

class car:

    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = "BMW"

c1 = car()
c2 = car()

c1.mil = 8

car.wheels = 5

print(c1.com, c1.mil , c1.wheels)
print(c2.com, c2.mil , c2.wheels)
