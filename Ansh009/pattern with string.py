str1 = "NO"
print_n = [[" " for i in range(0,6)]for j in range(0,6)]
print_o = [[" " for i in range(0,6)] for j in range(0,6)]


#Code for N
for row in range(0,6):
    for col in range(0,6):
        if col==0 or col==5 or row==col:
            print_n[row][col] = "*"
            
            
# code for O
for row in range(0,6):
    for col in range(0,6):
        if ((row==0 or row==5)and (col!=0 and col!=5))or ((col==0 or col==5)and (row!=0 and row!=5)):
            print_o[row][col] = "*"
            
for i in range(0,6):
    for j in range(0,6):
        print(print_n[i][j],end="")
    print(end="  ")
    for j in range(0,6):
        print(print_o[i][j], end="")
    print()
            
            
            