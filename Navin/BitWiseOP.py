"""Complement(~) -> tild operator
and(&)
or(|)
XOR(^)
Left shift(<<)
Right shift(>>)
"""

print(~12) # (~ 0 =1) (~1 = 0)
#( ~) convert binary in 1's compliment

print(12 & 13)     # 12 -> 00001100
                   # 13 -> 00001101
                   # ans = 00001100


print(12|13)  # similar to &

# #xOR , 0 0 =0
#        0 1 =1    if both are defrent then get 1
#        1 0 =1     or odd no. of 1 then get 1 
#        1 1 =0
print(12^1)
print(12^13)
print(25^30)

print(10<<2)  # 1010.0000 after <<shift 101000.00 =40
print(10>>2)  # 1010.0000 after >>shift 10.10 =2