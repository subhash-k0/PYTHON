# Dynamic Typing

class PyCharm:

    def execute(self):
        print('Compiling')
        print('Running')

class MyEditor:

    def execute(self):
        print('Spell Check')        
        print('Convention Check')        
        print('Compiling')        
        print('Running')        

class Laptop:

    def code(self, ide):
        ide.execute()

# ide = PyCharm()        
ide = MyEditor()        

lap1 = Laptop()
lap1.code(ide)