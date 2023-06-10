

name = ("ansh", "shanta","nitesh")
comp = ("apple", "dell", "facebook")
#zipped = list(zip(name, comp))
zipped = zip(name, comp)
for (a,b) in zipped:
    print(a,b)
#print(zipped)


x= [1,2,3,4]
y = [1,1,3,7,9]
for i in range(min(len(x),len(y))):
    if x[i]==y[i]:
        print("same")
    else:
        print("Not same")
        
#with zip
x= [1,2,3,4]
y = [1,1,3,7,9]
print(list(zip(x,y)))


# other way with zip
x= [1,2,3,4]
y = [1,1,3,7,9]
for i ,j in zip(x,y):
    if i==j:
        print("Same")
    else:
        print("Not same")


    