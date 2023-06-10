f_name = "ansh"
l_name = "barakoti"
# sentence = "My name is {} {}".format(f_name, l_name)
# print(sentence)

# sentence = f"My name is {f_name.upper()} {l_name.upper()}"
# print(sentence)

person = {"name": "Ansh", "age": 23}
# sentence = "My name is {} and i m {} years old". format(person["name"], person["age"])
# print(sentence)
sentence = f"my name is {person['name']} and I am {person['age']} years old"
print(sentence)


calculation = f'4 times 11 is equal to {4*11}'
print(calculation)

for n in range(1,11):
    number = f'The value is {n:03}'
    print(number)
    
pi = 3.14159265
number1 =  f'Pi is equal to {pi:.4f}'
print(number1)


from datetime import datetime
birthday = datetime(1982, 2, 3)
dob = f'Arjun has a birthday on {birthday:%B %d, %Y}'
print(dob)


    