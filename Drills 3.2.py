N = int(input("Enter N: "))
print (N)

row_count = 3
col_count = 5

if N%2==1 and N>0:
    for i in range(0, row_count):
        for j in range(0, col_count):
            if j%2==1:
                print("_", end="")
            if j%2==0:
                print("*", end="")
            else:
                print(" ", end="")
        print("")