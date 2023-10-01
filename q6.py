def percent_to_get_to(start, target):
    return (target-start)/start

def calculate_min_percent(n, z):
    desired_profit = n/100
    buy_money = z * 0.99 # account for 1% tax on buying
    target_money = (z + desired_profit) / 0.99  # account for 1% tax on selling
    global_profit_needed = percent_to_get_to(buy_money, target_money)
    return global_profit_needed * 100

n = int(input("enter N: "))
z = int(input("enter Z: "))

print(round(calculate_min_percent(n, z), 2))

