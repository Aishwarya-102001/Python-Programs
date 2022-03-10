#fruits=['apple','banana','cherry','mango','grape']
#for fruit in fruits:
    #print(fruit)
#   print(f"{fruit.title()} is a good fruit!") #runs till the loop ends and is placed within hte indentations
#print("Thanks!!") #any code outside indentation is executed once without repetition
#*************************use of range()function*******************************
#for i in range(1,5):  #range()function shows off-by-one behaviour (prints number till 4)
#   print(i)
#*************************use of range()function to make list of numbers*******************************
#numbers=list(range(1,6))
#print(numbers)
#even_numbers=list(range(2,11,2))  #third argument skips numbers in given range
#print(even_numbers)

#table of 2
squares=[]
for value in range(1,11):
    #square=value*2
    squares.append(value*2)
print(squares)
