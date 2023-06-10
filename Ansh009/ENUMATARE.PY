# way 1
my_list = ["apples", "pears", "oranges", "fruits"]
count = 0
for element in my_list:
    print(element)
    if count == 1:
        print("Count is 1")
    count += 1
print("*"*50)
#way 2
for x in range(len(my_list)):
    print(my_list[x])
    if x == 1:
        print("X is 1")
# best way to use enumarate in python
print("*"*50)
my_list = ["apples", "pears", "oranges", "fruits"]
for x,abc in enumerate(my_list):
    print(x, abc)
    
num = (1,2,3,4,5)
for i , count in enumerate(num):
    print(i,num)
    
    
name = {"arjun", "ram", "shyam"}
for i,  record in enumerate(name):
    print(i,record)
    
    
characters = ["ansh", "chanda", "ramesh","govinda",
              "ansh", "nitesh", "laxman","mira",
              "srijana", "samyog","niyod","ansh"]
character_map = {character:[] for character in set(characters)}
print(character_map)

for index, character in enumerate(characters):
    character_map[character].append(index)
print(character_map)

