# In the name of Allah

number = int(input())

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
while True:
    if number < fiboi(i):
        print(False)
        break
    elif number == fiboi(i):
        print(True)
        break
    i += 1

