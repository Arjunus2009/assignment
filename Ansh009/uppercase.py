a = ["arjun","ansh","shanta"]
for i in a:
    print(i.upper())
    
a = ["arjun","ansh","shanta"]
b = [i.upper()for i in a]
print(b) 

print("*"*50)
x = [1,2,3,4,5]
#y=[]
#y.append(2)
#y.append(4)
#y.append(6)
#y.append(8)
#y.append(10)
y = []
#print(y)
for item in x:
    y.append(item * 2)
print(y)
    
#a slop of a line is given by an equation y =0.5X+1
# please find out the points when the values ar x are 2,4,6,8,10

x = [2,4,6,8,10,18,142,173]
#y =0.5*x+1
y = []
for item in x:
    y_value = ((item,0.5 * item+1))
    y.append(y_value)
print(y)


