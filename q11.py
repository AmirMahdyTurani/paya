reqs = []

print("Please Enter (Fullname, origin, dest):")
while True:
    req = input()
    if req == "q":
        break

    reqs.append(req)


req_dict = dict()

for req in reqs:
    name, org, des = req.split()
    req_dict[name] = (org, des)

print("-"*25)

for  name ,(org, des) in req_dict.items():
    if (des, org) in req_dict.values():
        for name2 in req_dict.keys():
            if req_dict[name2] == (des, org):
                print(f"{name} can move succesfully from {org} to {des} beacuse of {name2} who wants to move from {des} to {org}")
                req_dict[name2] = ("used.", "used.")
    else:
        print(f"{name} can not move beacuse no one have not wanted to move from {des} to {org}.")