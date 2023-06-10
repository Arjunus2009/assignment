# p = int(input("Enter a principal amount:-"))
# r= int(input("Rate of interest:-"))
# t= int(input("Enter a time for loan period:-"))
# total = p*r*t/100
# print(f"total amoun:-", total)
      
print("-"*50)


# pattern
for i in range(1,9):
    for  j in range(1,i+1):                         
        print(j,end="")
    print()    


    """
    WAP to calculate factorial number;
    """
def ansh():   
    a = int(input("Enter a number:-"))

    f = 1
    for i in range(1,a+1):
        f=f*i 
    print("Factorial value is : ",f) 
ansh()
