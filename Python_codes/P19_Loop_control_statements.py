# 01 Break
count=1
while count<=10:
    print(count)
    count += 1
    if count==4:
        break
print("out from loop")

# 02 continue(for loop)
n=int(input("enter a number:"))
for i in range(n):
    if i==3:
        continue
    print(i)
print("out from loop")


# 03 continue(while loop)
n=int(input("enter a number:"))
while n<10:
    n += 1
    if n==6:
        continue
    print(n)
print("out from loop")

# 04 pass
number=int(input("enter a number:"))
while number<=5:
    print(number)
    number += 1
    if number==2:
        pass
print("out from loop")
