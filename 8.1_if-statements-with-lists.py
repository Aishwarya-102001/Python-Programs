
#************Checking for special items*******************
# toppings=['mushrooms','green peppers','extra cheese']
# for topping in toppings:
#     print(f"Adding {topping}")
# print("\nFinished making pizza")

#************Using multiple lists*******************
# available_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
# requested_toppings=['mushrooms','french fries','extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"Adding {requested_topping}")
#     else:
#         print(f"Sorry, we dont have {requested_topping}")
# print("\nFinished making Pizza")

#****************checking whether a value is not in a list************
banned_user=['andrew','carolina','david']
user=input("Enter your name:")
if user not in banned_user:
    print(f"{user.title()}, you can post a response.")