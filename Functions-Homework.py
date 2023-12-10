# 1.Write a Python function that checks whether a passed string is palindrome or not.
def is_palindrome(x):
    forward = str(x).replace(" ", "")
    backward = ""
    for i in forward:
        backward = i + backward
    if forward == backward:
        return (f'{x} is a palindrome')
    else:
        return (f'{x} is not a palindrome')


# 2.Write a Python function that takes a number as a parameter and checks if the number is prime or not
def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return (f'{x} is not a prime number')
        else:
            return (f'{x} is a prime number')
    else:
        return (f'{x} is not a prime number')


# 3.Write a Python function to check whether a number is in a given range.
def test_range(n, start_range, end_range):
    if n in range(start_range, end_range+1):
        return f'{n} is within the range'
    else:
        return f'{n} is outside the given range'


# 4.Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial(x):
    if x > 0:
        factorial = 1
        for i in range(1, x+1):
            factorial = factorial * i
        return f'the factorial of {x} is {factorial}'
    elif x == 0:
        return 'the factorial of 0 is 1'
    else:
        return 'this function does not calculate the factorial of negatives numbers'


# 5.Write a Python program to reverse a string.
def reverse_str(x):
    reversed = ""
    for i in x:
        reversed = i + reversed
    return reversed


# 6.Write a Python function to sum all the numbers in a list.
def sum_all(list):
    sum = 0
    for i in list:
        sum += i
    return sum


# 7.Write a Python function to find the Max of three numbers.
def max_of_three(a, b, c):
    if (a >= b) and (a >= c):
        max = a
    elif (b >= a) and (b >= c):
        max = b
    else:
        max = c
    return max
