a, b, c = map(int, input("Please Enter Times: ").split()) # getting the numbers from user

# calculate the how much time of download remaining
sum = a + b + c
time = sum / 3

# print the output
print(time)