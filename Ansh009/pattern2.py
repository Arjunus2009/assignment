#STRING PATTERN
string = input("Enter the string:-")
length = len(string)
for row in range(length):
    for col in range(row+1):
        print (string[col],end=" ")
    print()
length=+length+1
        
num = int(input("Enter the number of rows:-"))
for i in range(1,num+1):
    for j in range(1,num-i+1):
        print(end=" ")
    for j in range(i,0,-1):

        print(j,end="")
    for j in range(2,i+1):
        print(j,end="")
              
    print()
num=+num+1   
        
      