x = int(input("Please enter an integer:"))
y = int(input("Please enter another integer:"))
z = int(input("Please enter a third integer:"))

odd = True
if x%2==0:
    odd = False

odd = True
if z%2==0:
    odd = False

odd = True
if y%2==0:
    odd = False

if odd:
    max = x
    if y > max:
        max = y
    if z > max:
        max = z
    print(max, "is the greatest")
else:
    print("None of them are odd.")