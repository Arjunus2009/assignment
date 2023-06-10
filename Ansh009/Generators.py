def square_numbers(nums):
    result = []
    for i in  nums:
        result.append(i*i)
    return result
my_nums = square_numbers([1,2,3,4,5])
print(my_nums)

# with generators


def square_numbers(nums):
    #result = []
    for i in  nums:
        yield(i*i)  # yield is called generator
    #return result
my_nums = square_numbers([1,2,3,4,5])
print (next(my_nums))
print (next(my_nums))
print (next(my_nums))
print (next(my_nums))
print (next(my_nums))

print("&"*50)
def square_numbers(nums):
    #result = []
    for i in  nums:
        yield(i*i)  # yield is called generator
    #return result
my_nums = square_numbers([1,2,3,4,5])
for num in my_nums:
    print (num)
    


