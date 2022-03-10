#*******************EVEN/ODD Program****************
num=int(input("Enter a number: "))   #int()--> used to convert original string datatype to int datatype

# if num % 2 == 0:   # % modulo operator--> gives remainder as output nd checks whether number is divisible by 2
#     print("number is even")
# else:
#     print("number is odd")

#*******************MULTIPLE OF 10****************
if num % 10 == 0:   # % modulo operator--> gives remainder as output nd checks whether number is divisible by 10
    print("number is multiple of 10")
else:
    print("number is not multiple of 10")