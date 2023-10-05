m = int(input("Please enter the value of m: "))


def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)


def comb(n, r):
    top = fact(n)
    bottom = fact(r) * fact(n - r)
    return top // bottom


def calculate(m):
    max = 0
    for i in range(m + 1):
        for j in range(m + 1):
            if (i == 0 and j == 0) or (i == m and j == m):
                continue
            x = comb(i + j, j) * comb((2 * m) - (i + j), m - j)
            if x > max:
                max = x
    return max


print(calculate(m))
