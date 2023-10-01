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
    if req_dict[name] == (None, None):
        continue
    if (des, org) in req_dict.values():        
        print(f"{name} can move succesfully.")
        req_dict[name] = (None, None)
        for name2 in req_dict:
            if req_dict[name2] == (des, org):
                print(f"{name2} can move succesfully.")
                req_dict[name2] = (None, None)
                break
    else:
        print(f"{name} can not move.")