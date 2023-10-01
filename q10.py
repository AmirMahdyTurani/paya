# reading the data from user
m = int(input("Please Enter the price of stuff: "))
x = int(input("How much does posting it cost for you: "))
n = int(input("Enter the off percentage(%): "))

# calculating the benefit percentage with math operations
total_price = m + x
interest = 100 - n

benefit = (total_price * 100) / interest

percentage = (benefit / m) * 100

benefit_percentage = percentage - 100

# print the output
print(benefit_percentage)