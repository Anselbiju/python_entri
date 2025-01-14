# Exercise 1: (score : 2) Create a function that takes in three arguments, two of which are optional. The first argument should be a required positional argument, 
# the second argument should be a keyword argument with a default value of 10, and the third argument should be a keyword argument with a default value of None. 
# The function should print the sum of the first two arguments if the third argument is None, and print the product of all three arguments if the third argument is not None. 

# Exercise 2: (score : 2) Write a function that takes in a list of strings and returns a new list with only the strings that have a length greater than or equal to 5. 
# Exercise 3: (score : 2) Write a Python program to evaluate a given mathematical expression using the eval() function. expression = "3 * 5 + 2" 
# Exercise 4: (score : 2) Write a Python program to filter out the prime numbers from a given list of integers using the filter() function.
# Exercise 5: (score : 2) Write a Python program to convert a list of strings to uppercase using the map() function.


# EXcercise 1
# def calculate(first, second=10, third=None):
#     if third is None:
#         print("Sum : " , first + second)
#     else:
#         print("Product : ", first * second * third)    

# calculate(1,2,3)
# calculate(1,0,3)
# calculate(1,2)

#Excercise 2
# def filter_long_strings(strings):
#     return [string for string in strings if len(string) >= 5]
# list_1 = ["apple", "cat", "banana", "dog", "elephant"]
# result = filter_long_strings(list_1)
# print(result)  

#Excercise 3

# expression = "3 * 5 + 2"
# print(eval(expression))


#Excercise 4
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# primes = list(filter(is_prime, numbers))
# print(primes)  


# Excercise 5
# def to_uppercase(values):
#     return list(map(str.upper, values))
# list_5 = ["apple", "cat", "banana", "dog", "elephant"]
# result = to_uppercase(list_5)
# print(result)



