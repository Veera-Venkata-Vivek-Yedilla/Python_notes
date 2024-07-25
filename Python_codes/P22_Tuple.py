tuple1=(5,8,-2,"vivek",True,9,12,15)
print(tuple1)
print(tuple1[5])
print(tuple1[1:6])
print(tuple1[::2])  # start:stop:step

tuple2=(25,26,27,28,29,30)
tuple3=(35,36,37,38,39,40)
tuple4=(tuple2,tuple3)
print(tuple4)
print(tuple4[1])

# length
print(len(tuple3))
print(len(tuple4))

# print(max(tuple1)) # error, tuple1 contains 'str' and 'int
print(max(tuple2))
print(max(tuple3))

# tuple1[0]=13
# TypeError: 'tuple' object does not support item assignment

# index
print(tuple3.index(39))

print(tuple2)
print(list(tuple2))
