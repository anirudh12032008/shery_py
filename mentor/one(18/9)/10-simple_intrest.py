# Question - Accept the Principle amount, time & rate of interest and calculate the Simple Interest

principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time (in years): "))
rate_of_interest = float(input("Enter the rate of interest (in percentage): "))

simple_interest = (principal * time * rate_of_interest) / 100
end_balance = principal + simple_interest
print(f"Simple Interest: {simple_interest} ")
print(f"End Balance: {end_balance}")
