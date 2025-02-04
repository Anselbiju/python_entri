# 5_File and Exception Handling

# Exercise 1: (score : 1) Write a Python program to read a file and display its contents 
# Exercise 2: (score : 1) Write a Python program to copy the contents of one file to another file 
# Exercise 3: (score : 2) Write a Python program to read the content of a file and count the total number of words in that file. 
# Exercise 4: (score : 1) Write a Python program that prompts the user to input a string and converts it to an integer. Use try-except blocks to handle any exceptions that might occur 
# Exercise 5: (score : 1) Write a Python program that prompts the user to input a list of integers and raises an exception if any of the integers in the list are negative. 

# Exercise 6: (score : 2) Write a Python program that prompts the user to input a list of integers and computes the average of those integers. 
# Use try-except blocks to handle any exceptions that might occur.use the finally clause to print a message indicating that the program has finished running. 

# Exercise 7 : (score : 2) Write a Python program that prompts the user to input a filename and writes a string to that file. 
# Use try-except blocks to handle any exceptions that might occur and print a welcome message if there is no exception occurred

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Exercise 1:
# file_path = open("/Users/anselbiju/Documents/testobj.rtf",'r')
# print(file_path.read())

# Exercise 2:
# with open("/Users/anselbiju/Documents/testobj.rtf",'r') as source:
#     with open("/Users/anselbiju/Documents/copytest.rtf",'w') as destination:
#         destination.write(source.read())
#         print("File copied successfully")

# Exercise 3:
# with open("/Users/anselbiju/Documents/testobj.rtf",'r') as source:
#    content= source.read()
#    word = content.split()
#    word_count = len(word)
#    print(word_count)

# Exercise 4:
# user_input = input("enter your number :")
# print(type(user_input))
# try:
#     conv = int(user_input)
#     print(f"You entered the integer: {conv}")
# except ValueError:
#     print("enter a number to proceed!!!")
# print(type(conv))

# Exercise 5:
# user_input = input("Enter the list of numbers seperated by spaces :")
# try:
#     numbers = list(map(int, user_input.split()))
#     for n in numbers:
#         if n < 0:
#             raise ValueError("Error: Negative numbers are not allowed!")
# except ValueError as e:
#     print("error", e)    


#Excercise 6:
# user_input = input("Enter the list of numbers seperated by spaces :")
# try:
#     numbers = list(map(int, user_input.split()))
#     avg = sum(numbers)/len(numbers)
#     print(f"Average : {avg}")
# except ZeroDivisionError:
#     print("Enter a value to process")
# except ValueError as e:
#     print(f"error:{e}")
# finally:
#     print("process excecution has finished")
    

#Excercise 7:
# filename = input("Enter the filename: ")
# content = "Hello, this is a test file. Welcome!"  
# try:
#     with open(filename, 'w') as file:
#         file.write(content)
#     print("File written successfully. Welcome!")
# except Exception as e:
#     print(f"Error: {e}")
# finally:
#     print("Program execution has finished.")

