def solve_gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def solve_equation(a, b, c):
    # Check if the equation has a unique solution or not
    gcd = solve_gcd(a, b)

    if c % gcd == 0:
        return float("inf")
    else:
        return 0

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
print(solve_equation(a, b, c))