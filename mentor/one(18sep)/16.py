# Question -  Accept name and age from the user. Check if the user is a valid voter or not.
    #   Vaid - Hello Sheryank, You are a valid voter.
    #   Invalid - Sorry Shery, you can't cast the vote.
    # Print after how many years the user will be eligible and include real life conditions
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if 1 <= age <= 200:
    if age >= 18:
        print(f"Hello {name}, you are a valid voter.")
    else:
        print(f"Sorry {name}, you can't cast the vote.")
        years_until_eligible = 18 - age
        print(f"You will be eligible to vote in {years_until_eligible} years.")
else:
    print("Invalid age. Please enter a valid age between 1 and 200.")

