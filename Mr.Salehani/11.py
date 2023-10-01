requests = []

done = False
print("Welcome, enter each request to process, enter X to stop")
while not done:
    name = input("Enter requester's name: ")
    if name.lower() == "x":
        break 

    living = input("Enter their current city: ").lower()
    if living == "x":
        break 

    destination = input("Enter their destination: ").lower()
    if destination == "x":
        break 
    
    requests.append((name, living, destination))
    print("Added ", name, "for processing...")
    print()

print("\nProcessing...\n\n")

if len(requests):
    valids = []
    queued = []
    for request in requests.copy():
        name, living, dest = request

        for q_request in queued:
            qname, qliving, qdest = q_request
            if dest ==  qliving and living == qdest:
                valids.append(request)
                requests.remove(request)
                valids.append(q_request)
                queued.remove(q_request)
                break 
        
        if request in requests:
            queued.append(request)
    
    for valid in valids:
        name, living, dest = valid
        print(name, "is free to go to", dest + "!")
    
    for rejected in queued:
        name, living, dest = rejected
        print("request for moving to", dest, "by", name, "rejected...")
    

else:
    print("No info to process")
