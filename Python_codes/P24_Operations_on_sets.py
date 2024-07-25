# Union, intersection, difference, symmetric_difference
set_1={"vivek","chinnu","madhu"}
set_2={"chinnu","ganesh","prasanna"}
set_3={"ram","teja","charan"}

# 01 union: all elements in set_1 and set_2 without duplicates
print(set_1.union(set_2))
print(set_1 | set_2)    # Union( | )
print(set_1.union(set_2,set_3))
print(set_1 | set_2 | set_3)
print(set_1.union(("vivek","vicky")))
set_1.update(set_2)
print(set_1)

# 02 intersection ( & ) : Common elements between sets
set_1={"vivek","chinnu","madhu"}
set_2={"chinnu","ganesh","prasanna"}
set_3={"ram","teja","charan"}
print(set_1.intersection(set_2))
print(set_1 & set_2)
print(set_1.intersection(set_2,set_3))

# 03 difference
print(set_1.difference(set_2))  # {'madhu'.'vivek'}
print(set_1-set_2)

# 04 symmetric_difference: it returns the element in set_1 and set_2, but not in both
print(set_1.symmetric_difference(set_2))
print(set_1 ^ set_2)
print(set_1 ^ set_2 ^ set_3)



