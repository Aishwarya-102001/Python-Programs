
#************Passing a list***********
# def greet_users(names):
#     for name in names:
#         msg=f"Hello, {name.title()}!"
#         print(msg)

# usernames=['Hannah','ty','margot']
# greet_users(usernames)

#**********modifying a list in a function***********

# unprinted_designs= ['phone case','robot pendant','dodecahedron']
# completed_models=[]

# def print_models(unprinted_designs,completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)
# print(unprinted_designs)
# print(completed_models)

#**************PREVENTING FUNCTIONS FROM MODIFYING A LIST*********************
# unprinted_designs= ['phone case','robot pendant','dodecahedron']
# completed_models=[]

# def print_models(unprinted_designs,completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# print_models(unprinted_designs[:], completed_models)  #passing the function a copy of list and the original is intact
# show_completed_models(completed_models)
# print(unprinted_designs)
# print(completed_models)


#**************PASSING AN ARBITRARY NUMBER OF ARGUMENTS*********************
# def make_pizza(*toppings):   # (asterisk) * in parameter name makes an empty TUPLE to pack whatever values it receives into tuple.
#     print (toppings)
# make_pizza('pepperoni')
# make_pizza('mushroom','peppers','cheese')

#**************MIXING POSTITIONAL AND ARBITRARY ARGUMENTS*********************
# def make_pizza(size, *toppings):
#     print(f"\nMaking a {size}-inch pizza with toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'pepper','mushrooms','cheese')

#**************USING ARBITRARY KEYWORD ARGUMENTS*********************
def build_profile(first,last,**user_info):  # (**) is used to create an empty DICTIONARY and pack whatever name-value pair
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info

user_profile= build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)