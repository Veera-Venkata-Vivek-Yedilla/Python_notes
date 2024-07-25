# *args
def multiply(a,b,*args):
    mul=a*b
    for num in args:
        mul=mul*num
    return mul
print(multiply(1,2,3,4,5))

# **Kwargs
def tell_arguments(**kwargs):
    for key,value in kwargs.items():
        print(key+":"+value)
tell_arguments(arg1="veera",arg2="venkata",arg3='vivek')