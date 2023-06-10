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


# syntax= y= [append_expression> for item initerable]
y= [item*2 for item in x]
print(y)

list1=[1,4,2,7,9]
list2 = [ansh*3 for ansh in list1]
print(list2)


l = [10,20,30,50,60]
t = len(l)
for n in range(t):
    print(l[n])
    