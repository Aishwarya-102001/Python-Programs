# def favorite_book(title):  # here "title" is called as "parameter"
#     """prints the favorite books""" #this is a DOCSTRING which generates documentation for function in our programs
    
#     print(f"One of my favorite books is {title.title()}.")

# favorite_book('Alice in wonderland')  # here "Alice in wonderland" is called as "argument"

#*Arguments and Parameters are used interchangeably.

# def get_formatted_name(first_name,last_name):
#     fullname= f"{first_name} {last_name}"
#     return fullname.title()

# Student= get_formatted_name('Aishwarya','Patil')
# print("Student Name:", Student)

#*********function with if-else condition*******
# def get_formatted_name(first_name,last_name,middle_name=''):
#     if middle_name:
#         fullname= f"{first_name} {middle_name} {last_name}"
#     else:
#         fullname= f"{first_name} {last_name}"
#     return fullname.title()

# Student1= get_formatted_name('Aishwarya','Patil')
# print("Student Name:", Student1)
# Student2= get_formatted_name('John','hooker','lee')
# print("Student Name:", Student2)

#************Returning a dictionary***********
def get_formatted_name(first_name,last_name):
    person= {'first':first_name,'last':last_name}
    return person

Student= get_formatted_name('Aishwarya','Patil')
print("Student Name:", Student)
