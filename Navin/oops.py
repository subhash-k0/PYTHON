class computer:

    def config(self):
        print("i5 , 16gb, 1Tb")


comp1 = computer()        
comp2 = computer()

computer.config(comp1)
computer.config(comp1)

comp1.config()
comp2.config()