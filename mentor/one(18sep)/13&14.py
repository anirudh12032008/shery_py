# Question - Accept the gender from the user as char and print the respective greeting message
gender = input("Enter your gender ('M'/'m' for male or 'F'/'f' for female): ")



if gender == 'M' or gender == 'm':
    print("Good Morning Sir")
elif gender == 'F' or gender == 'f':
    print("Good Morning Mam")
else:
    print("Invalid input. Please enter 'M'/'m' for male or 'F'/'f' for female.")
