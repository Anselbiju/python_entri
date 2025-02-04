# Question 1: (5 Marks) Build a program to manage a university's course catalog. You want to define a base class Course that has the following properties:
# course_code: a string representing the course code (e.g., "CS101") 
# course_name: a string representing the course name (e.g., "Introduction to Computer Science") 
# credit_hours: an integer representing the credit hours for the course (e.g., 3) 
# You also want to define two subclasses CoreCourse and ElectiveCourse, which inherit from the Course class. 
# CoreCourse should have an additional property required_for_major which is a boolean representing whether the course is required for a particular major. 
# ElectiveCourse should have an additional property elective_type which is a string representing the type of elective (e.g., "general", "technical", "liberal arts"). 

# Question 2: (5 Marks) Create a Python module named employee that contains a class Employee with attributes name, salary and methods get_name() and get_salary(). 
# Write a program to use this module to create an object of the Employee class and display its name and salary

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Question 1
# class Course:
#     def __init__(self, code, name, credit_hours):
#         self.code = code
#         self.name = name
#         self.credit_hours = credit_hours

#     def display(self):
#         return f"Course code:{self.code}, Name:{self.name}, Credit Hours:{self.credit_hours}"
    
# class CoreCourse:
#     def __init__(self, code, name, credit_hours, required_for_major):
#         self.code = code
#         self.name = name
#         self.credit_hours = credit_hours
#         self.required_for_major = required_for_major
#     def display(self):
#         return f"Course code:{self.code}, Name:{self.name}, Credit Hours:{self.credit_hours}, required for credit: {'Yes' if self.required_for_major else 'No'}"

# class ElectiveCourse(Course):
#     def __init__(self, code, name, credit_hours, elective_type):
#         self.code = code
#         self.name = name
#         self.credit_hours = credit_hours
#         self.elective_type = elective_type
#     def display(self):
#         return f"Course code:{self.code}, Name:{self.name}, Credit Hours:{self.credit_hours}, Elective type:{self.elective_type}"

# c1 = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
# elective_course = ElectiveCourse("ART201", "History of Art", 2, "liberal arts")
# print(c1.display())
# print(elective_course.display())


# Question 2
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_name(self):
        return f"{self.name}"
    def get_salary(self):
        return self.salary
        


    
