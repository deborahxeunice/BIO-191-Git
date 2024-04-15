age = int(input("Please enter your age:"))

if age <= 15:
    parent = int(input("Does your parent have a fishing license? (Press 1 for Yes and 0 for No):"))
    print(parent)

    if parent == 1:
        print("You are legal to fish in MN.")
    else:
        print("You are NOT legal to fish in MN.")
    
else:
    license = int(input("Do you have a fishing license? (Press 1 for Yes and 0 for No):"))
    print(license)

    if license == 1:
        print("You are legal to fish in MN.")
    else:
        print("You are NOT legal to fish in MN.")