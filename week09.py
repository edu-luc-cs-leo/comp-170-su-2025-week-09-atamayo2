def factorial(n):
    """Computes recursively n! = 1 * 2 * ... * (n-1) * n
    """
    if n == 0:
        # Base case, 0! is by definition 1
        result = 1
    else:
        # Recursive case: n! = (n-1)! * n
        result = n * factorial(n-1)
    return result

def fibonacci(n):
    """Computes recursively the Fibonacci sequence
    F(n) = F(n-1) + F(n-2)
    for n > 2, with initial conditions F(1) = 1 and F(2) = 2
    """
    if n == 1 or n == 2:
        # Base case
        result = n
    else:
        # Recursive case
        result = fibonacci(n-1) + fibonacci(n-2)
    return result

# ITERATIVE VERSIONS OF ASSIGNMENT METHODS

def sum_of_digits_iterative(n):
    sum = 0
    while n > 1:
        # Obtain the last digit to add to sum. The last digit is always the remainder of
        # the integer division by base of the number system in use (here: 10).
        sum += n % 10 
        # Remove the last digit. This can be done by integer division of the number with
        # its number base (here: 10). For exampe 24 // 10 = 2 (and thus 4 is gone!)
        n //= 10
    # Done
    return sum + n

def count_occurrences_iterative(data_list, target):
    count = 0
    # Iterate over the input list
    for i in range(len(data_list)):
        # Check if current list item matches target value
        if data_list[i] == target:
            # If it does, increment the counter
            count += 1
    # Done
    return count


# WRITE YOUR CODE BELOW

# RECURSIVE SUM OF DIGITS

def sum_of_digits(n: int, base: int = 10) -> int:
    """Computes the sum of digits for a number recursively."""
    if n < base:
        result = n
    else:
        result = (n % base) + sum_of_digits(n // base, base)
    return result
# end method

# Test sum_of_digits
print("\nTesting sum_of_digits (recursive)")
print(sum_of_digits(11))   
print(sum_of_digits(12)) 
print(sum_of_digits(21))   
print(sum_of_digits(1))    
print(sum_of_digits(2))    
print(sum_of_digits(22))  


# RECURSIVE COUNT OCCURRENCES

def count_occurrences(source: list[int], target: int) -> int:
    """Counts how many times a target value appears in the list recursively."""
    if source:
        occurrence = 1 if source[0] == target else 0
        result = occurrence + count_occurrences(source[1:], target)
    else:
        result = 0
    return result
# end method count_occurrences

# Test count_occurrences with  list
my_list = [11, 12, 21, 1, 2, 22]

print("\nTesting count_occurrences (recursive)")
print(count_occurrences(my_list, 11)) 
print(count_occurrences(my_list, 2))   
print(count_occurrences(my_list, 5))   
print(count_occurrences(my_list, 22))  
print(count_occurrences(my_list, 99))  


# Reflection- 
# i was not able to submit homework 8 last week so i do not have a reflection on it. However i did struggle
# a bit when trying to write the code. I was not getting the right outcome which kept having me
# erase and start over. I did it very last minute so i definitely should have given myself more time on it.