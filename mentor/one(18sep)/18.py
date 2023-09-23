# Question - Accept a day number between 1-7 and print the corresponding dayname
day = int(input("Enter a day number (1-7): "))

if day == 1:
    print("Day name: Monday")
elif day == 2:
    print("Day name: Tuesday")
elif day == 3:
    print("Day name: Wednesday")
elif day == 4:
    print("Day name: Thursday")
elif day == 5:
    print("Day name: Friday")
elif day == 6:
    print("Day name: Saturday")
elif day == 7:
    print("Day name: Sunday")
else:
    print("Invalid input. Please enter a day number between 1 and 7.")
