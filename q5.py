def fact(n):
    if (n == 1 or n == 0):
        return 1
    if n == 2:
        return 2
    return n * fact(n-1)

m = int(input("Please Enter the value of m:"))

TABLE = m**2

for i in range(TABLE-2):
    pass