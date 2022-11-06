num = [7,8,9,5]

# print(num[3])

# for i in num:
#     print(i)

it = iter(num)  #iter -> convert list into iterator
print(it)    

print(it.__next__())
print(it.__next__())

print(next(it),'\n')

class Topten:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self 

    def __next__(self):

        if self.num <= 10:
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration


values = Topten()

# print(next(values))

for i in values:
    print(i)