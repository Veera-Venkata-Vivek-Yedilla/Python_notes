# Nested if, else

height=int(input("What is your height in feet? "))
if height>=3:
    print("can ride")
    age=int(input("What is your age? "))
    if age<12:
        print("Ticket cost is 150 Rs")
    elif age<=18:
        print("Ticket cost is 250 Rs")
    else:
        print("Ticket cost is 500 Rs")
else:
    print("can't ride")