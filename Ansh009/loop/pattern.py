def ansh():
    for i in range(1, 6):
        for j in range(1, i+1):
            print("* ", end=" ")
        print()


ansh()
print("="*50)
for i in range(5, 0, -1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

print("="*50)
for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("="*50)
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
print("="*50)
for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end=" ")
    print()

print("="*50)
for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("="*50)
x = 5
for i in range(1, 6):
    for k in range(1, x+1):
        print(end=" ")
    for j in range(1, i+1):
        print("*", end=" ")
    print()
    x = x-1
x = 1
for i in range(5, 0, -1):
    for k in range(1, x+1):
        print(end=" ")
    for j in range(1, i+1):
        print("*", end=" ")
    print()
    x = x+1

print("="*50)
for i in range(65, 70):
    for j in range(65, i+1):
        print(chr(j), end=" ")
    print()

print("="*50)
for i in range(65, 70):
    for j in range(65, i+1):
        print(chr(i), end=" ")
    print()

print("="*50)
for row in range(0, 6):
    for column in range(0, 7):
        if (row == 0 and column % 3 != 0) or (row == 1 and column % 3 == 0) or (row-column == 2) or (row+column == 8):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("="*50)
num = int(input("Enter the Number:-"))
n = num//2
for i in range(0,n):
    for j in range(n-i-1):
        print(" ",end =" ")
    for j in range(i+1):
        print("* ",end=" ")
    if num%2==0:
        for j in range(2*(n-i-1)):
            print(" ",end="")
    else:
        for j in range(2*(n-i-1)+1):
            print(" ",end="")
    for j in range(i+1):
        print("*  ",end="")
    print()
    
for i in range(num,0,-1):
    for j in range(num-i):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print("* ",end=" ")
    print()
        
ansh() # cann call anywhere because it a fuction

