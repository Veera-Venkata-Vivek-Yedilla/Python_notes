# 01 Global scope
global_var=15
def my_function():
    print(global_var)
print(global_var)   # output: 15

# 02 Local scope
def my__function():
    local_var = 25
    print(local_var)
my__function()       # output: 25

# 03 Global + Local
global_var = 15
def my__function():
    local_var=25
    print(global_var+local_var)
my__function()       # output: 40
print(global_var)   # output: 15
# print(local_var)
# output: NameError: name 'local_var' is not defined.

