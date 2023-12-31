# In the name of Allah

# Reading data from user
a, b, c = map(int, input("Please Enter the value of a, b, c: ").split())

# calculate the data
delta = (b**2) - 4 * a * c


# solve the equality
def solve_the_eq(a, b, c):
    if delta > 0:
        x1 = (-b + ((delta) ** 0.5)) / (2 * a)
        x2 = (-b - ((delta) ** 0.5)) / (2 * a)
        return x1, x2
    elif delta < 0:
        print("Rishe nadarad.")
    else:
        return (-b + (delta) ** 0.5) / (2 * a)


# find the maximum of two number
def max(a, b):
    return a if a > b else b


# find the minimum of two number
def min(a, b):
    return a if a < b else b


# count the positive results
def count():
    x1, x2 = solve_the_eq(a, b, c)
    max_x = max(x1, x2) - 0.1 if max(x1, x2) % 1 == 0 else max(x1, x2)
    min_x = min(x1, x2) + 0.1 if min(x1, x2) % 1 == 0 else min(x1, x2)
    count = int(max_x) - int(min_x)
    if x1 / x2 < 0:
        count += 1
    return count


# if the delta is positive
if delta > 0:
    count = float("inf") if a > 0 else count()
# if delta is negative
elif delta < 0:
    count = float("inf") if a > 0 else 0
# if delta is 0
else:
    count = float("inf") if a > 0 else 1

print(count)
