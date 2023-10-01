def calculate_max(remainings: list):
    remainings = sorted(remainings)

    total_time = 0
    initial_speed = 3 / len(remainings)
    while len(remainings):
        speed_increase = (3 / len(remainings)) / initial_speed

        for i in range(len(remainings)):
            remainings[i] = remainings[i] / speed_increase

        remove_time = remainings[0]
        total_time += remove_time
        for i in range(len(remainings)):
            remainings[i] -= remove_time

        while len(remainings) and int(remainings[0]) == 0:
            remainings.pop(0)
    
    return int(total_time)


n = 3
remaining = []
for i in range(n):
    remains = int(input(str(i+1) + ": "))
    remaining.append(remains)
print(calculate_max(remaining))
