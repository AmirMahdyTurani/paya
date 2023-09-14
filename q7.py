# In the name of Allah

# getting inormation from user
m = int(input("Please Enter coeff: "))

# to make the outpot prettier :)
print()

# if the coefficient is 0 we will have a horizental line
if m == 0:
    print("*"*3)
    exit(0)

# negative numbers
if m < 0:
    x = "*"
    for i in range(-m+3):
        print(x)
        x = " " + x
        for j in range(-m-1):
            print()

# positive number
if m > 0:
    for i in range(m+3, 0, -1):
        x = (" " * i) + "*"
        print(x)
        x = i * " " + "*"
        for j in range(m-1):
            print()
