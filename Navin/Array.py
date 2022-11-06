#  'b'     (signed char)                   int  1
# 'B'     (unsigned char)                  int  1
# 'u'     (PY_UNICODE )      (unicode character)                   1
# 'h'     (signed char)                    int  1
# 'H'     (signed char)                    int  1
# 'i'     (signed char)                    int  1
# 'I'     (signed char)                    int  1
# 'l'     (signed long)                    int  1
# 'L'     (unsigned long)                  int  1
# 'f'     (float)                          int  1
# 'd'     (double)                         int  1

from array import *

# vals = array('I',[5,9,-8,4,2])
vals = array('i',[5,9,-8,4,2])

print(vals)
print(vals.buffer_info())
print(vals.typecode)
# print(vals.__sizeof__)

# print(vals.reverse())
print(vals[1])

for i in range(5):
  print(vals)
  print(vals[i])

for i in range(len(vals)):
  print(vals)
  print(vals[i])

for i in vals:
  print(i)
  print(vals)

  newArr = array(vals.typecode, (a for a in vals))
  print('newArr is ',newArr)
  i=0
  while i<len(newArr):
    print(newArr[i])
    i+=1