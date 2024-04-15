l = int(input("please input side length:"))

left = []
for s in range(l-1):
    left.append("*" * l)
left.append("*" * l)

right = []
for s in range(l-1):
    if s == 0:
        right.append("*" * l)
    else:
        right.append("*" + ((l - 2) * " ") + "*")
right.append("*" * l)

for f, t in zip(right, left):
    print(t + '\t' + f)

