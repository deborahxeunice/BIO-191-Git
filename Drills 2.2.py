age = int(input("Please enter your age:"))
citizen = int(input("Are you a natural born U.S. citizen? (Press 1 for Yes and O for No):"))
resident = int(input("How many years have you resided in the U.S.?:"))
eligible = True

if age < 35:
    eligible = False

if citizen == 0:
    eligible = False

if resident < 14:
    eligible = False

if eligible:
    print("You can run for president of USA.")

else:
    print("You CAN'T run for president of USA.")


