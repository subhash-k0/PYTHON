print("telusko\n"*8)

i=1
while i<=5:
    print("telusko")
    print(i)
    i=i+1

i=5
j=1
while(i>=1):
  print('telusko')
  print(j)
  while(j<=4):
    print('Rocks')
    j=j+1
  i=i-1


#line mmaching is important other wise it will take infinite Loop
i=1
j=1
while(i<=5):
  print('telusko',end=" ")
#   print(j)
  while(j<=4):
     print('Rocks',end=" ")
     j=j+1
  i=i+1


i=1
while(i<=5):
  print('telusko',end=" ")
  j=1
  while(j<=4):
     print('Rocks',end=" ")
     j=j+1
  i=i+1
  print()
