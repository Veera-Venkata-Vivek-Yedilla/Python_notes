# is, is not

# Memory location of a and b are same
a = 5
b = 5
print(id(a))        # Output: 140713649568312
print(id(b))        # Output: 140713649568312
print(a is b)       # Output: True
print(a is not b)   # Output: False

# Memory locations are different
c = 5
d = '5'
print(id(c))        # Output: 140713649568312
print(id(d))        # Output: 140713649629384
print(c is d)       # Output: False
print(c is not d)   # Output: True


# Memory locations are different
x = 4
y = 6
print(id(x))        # Output: 140713615489560
print(id(y))        # Output: 140713615489624
print(x is y)       # Output: False
print(x is not y)   # Output: True