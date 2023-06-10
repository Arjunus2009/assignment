

def sum_numbers(first,  *other):
    return first**2 + sum([item**3 for item  in other])
print(sum_numbers(2,3,4))
print(sum_numbers(5,3,4))

# list_1 = [x * 2 for x in range(1,11)]
# print(list_1)  #[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

number = [1,2,3,4,5]
for y in number:
    if y == 4:
        break
    print(y)
    
fruits = ["apple", "banana","cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally Finishe")
    
price = 50
txt = "The price is {:.2f} dollars"
print(txt.format(price))
	
 