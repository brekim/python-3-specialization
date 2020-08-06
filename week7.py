# Author: Brett Kim

global_var = 1

def hello(name, count):
    local_var = 1
    greeting = "Hello {}!\n".format(name)
    print(greeting*(count * local_var))

def square(number):
    return number * number

hello("Wendy", square(3))

def sum_of_list(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum

def sum_of_squares(lst):
    sum = 0
    for i in lst:
        sum += square(i)
    return sum

# sum is local

br = [2, 4, 6, 8]
print(sum_of_list(br))
print(sum_of_squares(br))