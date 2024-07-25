set_1={-6,1,2,0,"v",-5,1,2}
print(set_1)
print(type(set_1))
set_2={}
print(type(set_2))  # dict
set_3=set()
print(type(set_3))  # set

# print(set_1[0])
# Type error: Sets are Unordered collection of items

set_1.add(10)
print(set_1)
set_1.add((58,59,60))
print(set_1)
set_1.remove(-5)
print(set_1)
set_1.discard(2)
print(set_1)
set_4={12,15,16,-12,10,25,28,25}
print(set_4)
set_4.pop()     # Remove number randomly
print(set_4)
set_4.clear()   # empty set
print(set_4)





