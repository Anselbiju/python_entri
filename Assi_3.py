# Exercise 4
# num1 = int(input("enter the first number : "))
# num2 = int(input("enter the second number : "))
# num3 = int(input("enter the third number : "))

# greatest = num1
# if num2 > greatest:
#     greatest = num2
# if num3 > greatest:
#     greatest = num3
# print("the greatest number is : ", greatest) 



# Exercise 5
# num = int(input("Enter a number to find its factorial: "))
# factorial = 1

# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# elif num == 0:
#     print("The factorial of 0 is 1.")
# else:
#     for i in range(1, num + 1):
#         factorial *= i
#     print(f"The factorial of {num} is {factorial}.")


# Excercise 7
# num = int(input("Enter the number to find its multiples: "))
# count = int(input("Enter how many multiples you want: "))

# print(f"The first {count} multiples of {num} are:")
# for i in range(1, count + 1):
#     print(num * i)

# Excercise 8

# while True:  
#     user_input = input("Input :")  
#     if user_input.lower() == "done":  
#         print("Entered value is correct")
#         break  
#     else:
#         print(user_input)  


# Excercise 9
# for i in range(1, 16):  # Loop through numbers from 1 to 10
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")  
#     elif i % 3 == 0:
#         print("Fizz")  
#     elif i % 5 == 0:
#         print("Buzz")  
#     else:
#         print(i) 

# Excercise 10

# for i in range(5, 0, -1):  
#     for j in range(i, 0, -1):  
#         print(j, end=" ") 
#     print()  