# Question -  Accept the parameters and calculate the Compound Interest & print it on STDOUT .
def calc_CI(principal, rate, time):
    CI = principal * ((1 + rate / 100) ** time) - principal
    return CI

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in percentage): "))
time = float(input("Enter the time period (in years): "))

CI = calc_CI(principal, rate, time)

print("The compound interest is:", round(CI, 2))
