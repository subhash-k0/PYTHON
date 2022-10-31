x=int(input("How many candies you must "))

# i=1
# while i<=x:
#     print("candy")
#     i+=1

i=1
av=10
while i<=x:
    if i>av:
        print('out of stock')
        break
    print("candy")
    i+=1
print('bye')    

for i in range(1,100):

    if (i%3==0 and i%5==0):
      continue
    print(i)

    for i in range(1,101):

        if(i%2!=0):
            pass
        else:
            print(i)
