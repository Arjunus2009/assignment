def simple_interest(p,t,r):
    return (p*t*r)/100

print(simple_interest(100000, 5, 10))

def sum(a,b):
    return(a+b)
print(sum(100, 200))

def divide(a,b):
    return(a/b)
print(divide(500, 5))


def greet(firt_name, last_name):
    print(f"hi {firt_name} {last_name}")
    print("welcome to board")
#greet("Arjun" ,"Barakoti")
greet("Ansh", "Barakoti")

def get2(name):
    return f"hi {name}"
messgae = get2("Shanta")
print(messgae)

def increment(number, by):
    return number + by
result = increment(10, 2)
print(result)


# def decrement(number, by):
#     return number - by
# print(decrement(100, 10))

#write a program# that acepet two number and returns sum of the sqaure of them
def sum_square(num1,num2, num3=0):
    a = num1**2
    b = num2**2
    c = num3**2
    return a+b+c
print(sum_square(3,4))

#write a program that accept any number of argument and return sum of them
