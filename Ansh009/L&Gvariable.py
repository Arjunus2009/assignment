def fun1():
    n = 5
    print("n value is",n)
def fun2():
    n =10
    print("n value is", n)
    fun1()
fun2()

# global variable:
n = 10
def fun3():
    print(n)
def fun4():
    n= 20
    print(n)
    fun3()
fun4()