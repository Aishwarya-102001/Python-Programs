import pizza  #importing entire module

#   module_name.function_name ---> use this format for calling the function in that module
pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12,'peppers','mushrooms','cheese')

#**************************************************************
import pizza as p  #giving entire module an alias

#   alias_module_name.function_name ---> use this format for calling the function in that module
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'peppers','mushrooms','cheese')

#**************************************************************
from pizza import make_pizza  #importing specific functions
# from module_name import function_name ---> use this format for explicitly importing the particular function

make_pizza(16,'pepperoni')
make_pizza(12,'peppers','mushrooms','cheese')  #no need to use the dot notation

#**************************************************************
from pizza import make_pizza as mp   # using "as" to give a function an alias 
# from module_name import function_name as fn ---> here import statement renames the function make_pizza() to an alias mp()

make_pizza(16,'pepperoni')
make_pizza(12,'peppers','mushrooms','cheese')  #no need to use the dot notation

#**************************************************************
from pizza import *   #import every function in the module using *
#from module_name import *  ---> can call every function in that module without using dot notation

make_pizza(16,'pepperoni')
make_pizza(12,'peppers','mushrooms','cheese')