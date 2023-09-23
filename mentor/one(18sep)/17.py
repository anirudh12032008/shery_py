# Question -  Accept the parameters and calculate the Compound Interest & print it on STDOUT .
def calc_compound(principal, rate, time):
    CI = principal * ((1 + rate / 100) ** time) - principal
    return CI

principal_input = int(input("Enter the principal amount: "))
rate_input = int(input("Enter the rate of interest (in percentage): "))
time_input = int(input("Enter the time period (in years): "))

CI = calc_compound(principal_input, rate_input, time_input)

print("The compound interest is:", round(CI, 2))
