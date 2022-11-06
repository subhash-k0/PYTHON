
def person(name, **data):
    print(name)
    # print(data)
    for i,j in data.items():   #items is reserv
        print(i,j)
  


person('navin',age=28,city='Mumbai',mob =9882716)    

