N = int(input("Please enter N:"))

c = 2

while N!=0:
    for i in range (2,c):
        if c%i==0:
            break
    
    else:
        print(c, end=" ")
        N -=1
    c +=1
print()

#This code is in reference to the video tutorial of YouTube channel Geek Rishu, retrieved from: https://www.youtube.com/watch?v=2Xj9jwxd9Zg