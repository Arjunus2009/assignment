a = 50
def show():
    x = 10
    print(a) # 50
    print(x) # 10
show()
#print("x:",x) #NameError: name 'x' is not defined
print("Global variable:",a)
print("#"*50)

i = 0
def my_function():
    a = i+1
    print("My function:-", a) # 1
my_function()

print("#"*50)
i = 0
def my_function():
    i = 10
    i = i+1
    print("My function:-", i) # 11
my_function()
