# In the name of Allah

# getting number from user
number = int(input())

# define a function that calculate the nth number of fiboischi
def fiboi(nu):
    s = nu
    n = 1
    jam = n + s
    zarb = n * s
    j = jam + zarb
    s = n
    n = j
    return j

i = 0
# cheking if the number is a member of fibischi
while True:
    if number < fiboi(i):
        print(False)
        break
    elif number == fiboi(i):
        print(True)
        break
    i += 1

