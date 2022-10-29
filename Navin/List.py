nums=[1,2,3,4,5,6,]
print(nums)

print(nums[2])
print(nums[3])
print(nums[-1])
print(nums[-3])
print(nums[3:])
print(nums[3:-1])

name= ['navin', 'kiran', 'john']
print(name)
print(name[1])
print(name[2])
print(name[0])

values=[9.5, 'navin', 25]
print(values[0])
print(values[1])
print(values[2])

all = [nums, name, values]
print(all)
print(all[1])
nums.append(25)
print(nums)
nums.insert(2,34)
print(nums)
nums.remove(6)
print(nums)
nums.pop(1)
print(nums)
nums.pop()
print(nums)
del nums[2:]
print(nums)
nums.extend([4,5,6,7])
print(nums)
print(min(nums))
print(max(nums))
print(sum(nums))
nums.sort()
print(nums)