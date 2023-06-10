def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
print(factorial(5))
print(factorial(7))


def add(n):
    if  n == 1:
        return 1

    else:
        return n+ add(n-1)
print(add(5))
      

    

def fibonacci(n):
    if n <= 0:
        print("Invalid input! Please provide a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test the function
number = 8
print("Fibonacci series:")
for i in range(1, number + 1):
    print(fibonacci(i), end=" ")
print()

