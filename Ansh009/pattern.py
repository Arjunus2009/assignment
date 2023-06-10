def ansh():
    for i in range(1,6):
        for j in range (1, i+1):
            print("* ", end=" ")
        print()
ansh()
print("="*50)
for i  in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

print("="*50)
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
        
print("="*50)
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
print("="*50)
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

print("="*50)
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print("="*50) 
x=5  
for i in range(1,6):
    for k in range(1,x+1):
        print(end=" ")
    for j in range(1,i+1):   
        print("*",end=" ")
    print()
    x=x-1
x=1
for i in range(5,0,-1):
    for k in range(1,x+1):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    x=x+1
print("*"*50)

n = int(input("Enter of rows:-"))
k=0
for i in range(n):
    k=k+i
m=n+k
for i in range (n):
    for j in range(i+1):
        print(format(m,"<3"),end=" ")
        m=m-1
    print()
    
        