m = int(input("Please Enter coeff: "))
print()

if m == 0:
    print("*"*3)
    exit(0)

if m < 0:
    x = "*"
    for i in range(-m+3):
        print(x)
        x = " " + x
        for j in range(-m-1):
            print()

if m > 0:
    for i in range(m+3, 0, -1):
        x = (" " * i) + "*"
        print(x)
        x = i * " " + "*"
        for j in range(m-1):
            print()
