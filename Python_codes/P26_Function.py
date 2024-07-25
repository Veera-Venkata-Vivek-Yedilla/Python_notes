# def function with print
def add2numbers(a, b):
    print(f"a+b={a+b}")
add2numbers(2,3)

# def function with return
def add2numbers(a,b):
    return a+b
sum1 = add2numbers(5,11)
print(sum1)

def add3numbers(a, b, c=1):
    print(a+b+c)
add3numbers(2,5)
add3numbers(2,5,3)