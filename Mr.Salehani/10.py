def percent_to_get_to(start, target):
    return (target-start)/start

def biensafi(price, post, target_percentage):
    final = (price + post) / (1-(target_percentage/100))
    return int(percent_to_get_to(price, final) * 100)

price = int(input("price: "))
post = int(input("post: "))
target_percentage = int(input("off: "))
print(biensafi(price, post, target_percentage))