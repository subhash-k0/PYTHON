nums = [12,16,18,21,25,30,40]

for num in nums:
    if num%5 ==0:
        print(num)
        

for num in nums:
    if num%5 ==0:
        print(num)
        break
    else:
        print('not found')

for num in nums:
    if num%5 ==0:
        print(num)
        break
else:
    print('not found')