l = int(input("Please input side length:"))

for s in range(l):
    print(" " * (l-s), "*" * (2*s + 1))
for s in range(l-2, -1, -1):
    print(" " * (l-s), "*" * (2*s + 1))
