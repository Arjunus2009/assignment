# create a function  to return double of a number if it is even and triple if it is add


def double_or_triple(number):
    if number % 2 == 0:  # check if number is even
        return number * 2
    else:
        return number * 3
result = double_or_triple(17)
print(result)
print(double_or_triple(18))

def odd_even(num):
    if num %2 == 0:
        return"even"
    else:
        return "odd"
result = odd_even(20)
print(result)