# 1
count=1
while count<=4:
    print(count)
    count += 1
print("out from loop")

# 2
number=int(input("enter a number(-1 to quit):"))
while number != -1:
    print(number)
    number = int(input("enter a number(-1 to quit):"))
else:
    print("in else block")
print("out from loop")


# 3
count=5
while count>0:
    print(count)
    count -= 1
else:
    print("else block")
print("out from loop")


# 4
total=0
number=int(input('enter a number:'))
while number != 0:
    total += number
    number = int(input("enter a number:"))
print("total is:",total)




