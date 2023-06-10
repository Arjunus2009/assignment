
def add(a, b):
    return a+b
print(add(5,9))


# same thig in lambda
add_number = lambda a,b : a+b
print(add_number(5,6))

mul_num = lambda x, y: x * y
print(mul_num(5, 6))


hyp = lambda p, b : (p**2 + b**2)**0.5
print(hyp(3,4))

sq_cube = lambda x: x**2 if x%2==0 else x**3
print(sq_cube(2))
print(sq_cube(3))

#lambda with zero arguments

hello_world = lambda: "hello world"
print(hello_world())