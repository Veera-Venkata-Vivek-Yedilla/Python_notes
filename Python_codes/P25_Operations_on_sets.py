# isdisjoint, issubset

set_1={"vivek","chinnu","madhu"}
set_2={"chinnu","ganesh","prasanna"}
set_3={"ram","teja","charan"}
print(set_1.isdisjoint(set_2))  # output: False
print(set_1.issubset(set_2))    # output: False
print(set_1 <= set_2)           # output: False

set_1={"vivek","chinnu","madhu"}
set_2={"chinnu","ganesh","prasanna","vivek","madhu"}
print(set_1.isdisjoint(set_2))  # output: False
print(set_1.issubset(set_2))    # output: True

set_1={"vivek","chinnu","madhu"}
set_2={"teja","ganesh","prasanna"}
print(set_1.isdisjoint(set_2))  # output: True
print(set_1.issubset(set_2))    # output: False

# issubset and issuperset are vice versa
set_1={"vivek","chinnu","teja","madhu","ganesh","prasanna"}
set_2={"teja","ganesh","prasanna"}
print(set_1.issuperset(set_2))  # output: True
print(set_2.issuperset(set_1))  # output: False

print(set_3)
set_3.clear()
print(set_3)    # set(): empty set




