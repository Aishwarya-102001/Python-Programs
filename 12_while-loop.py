# message =''
# while message != 'quit':
#     message= input("Tell me something and I'll repeat it: ")  #inputs message from user
#     if message != 'quit':  #checks whether message is quit or not? if msg is quit it automatically exits the loop
#         print("Aishwarya", message)

#**BREAK**
#******************using break to exit a loop**************

# while True:
#     city=input("Enter the name of city you have visited. Enter 'quit' to exit :")

#     if city == 'quit':
#         break
#     else:
#         print(f"I would like to visit {city.title()}!")


#**CONTINUE**
#******************using continue in a loop**************
current_number=0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)