with open('pi_digits.txt') as file_object:
    content = file_object.read()

print(content)

#*******************RELATIVE FILE PATH******************
# with open('text_files/fileName.txt') as file_object:

#*******************ABSOLUTE FILE PATH******************
# file_path = '/home/ehmatthes/other_files/text_files/fileName.txt'

# with open(file_path) as file_object:

#***************Reading line by line***********************************

# filename= 'pi_digits.txt'

# with open(filename) as file_object:
#     for line in file_object:   #Reading line by line gives extra space between each line
#                                #bcuz an invisible newline character is at the end of each line in the text file
#                                #nd one newline is added by print() --> in all 2 lines are added!
#         # print(line)
#         print(line.rstrip())   #Removes extra blank line

#************Making a list of lines from a file*******
filename= 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())   # We can continue working with the content of file even after the "with" block 
                           # as we have stored the files's content in a list and its same.

#***************Working with a file's content***********
filename= 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)

print(len(pi_string))