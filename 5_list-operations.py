bikes = ['honda','yamaha','suzuki','tata']
print(bikes)
#***************MODIFYING ELEMENT IN LIST************************
#bikes[0]='ducati'  #changes the first element of the original list
#print(bikes)
#***************ADDING ELEMENT IN LIST************************
#bikes.append('ducati')  #adds new element to the end of the list
#print(bikes)
#***************INSERTING ELEMENT IN LIST************************
#bikes.insert(1,'ducati')  #adds new element at the specific index and shifts the other elements to the right
#print(bikes)
#***************REMOVING ELEMENT IN LIST using del statement************************
#del bikes[0]  #deletes the element at that specific index
#print(bikes)
#***************REMOVING ELEMENT IN LIST using pop() method************************
#new_bikes=bikes.pop()
#new_bikes=bikes.pop(0)  #popping elements from any position in list
#print(bikes)  #gives new list 
#print(new_bikes)  #gives the element that is popped 
#***************REMOVING ELEMENT IN LIST using remove() method************************
#bikes.remove('honda') 
#print (bikes)\
#***************SORTING ELEMENT IN LIST permanently using sort() method********************
#bikes.sort() #sorts elements in alphabetical order
#bikes.sort(reverse=True) #sorts elements in reverse alphabetical order
#print(bikes)
#***************SORTING ELEMENT IN LIST temporarily using sorted() function********************
#print(sorted(bikes)) 
#print(bikes) #list still remains in original order after using the sorted() function
#***************PRINTING LIST IN REVERSE ORDER********************
#bikes.reverse() 
#print(bikes)
#***************FINDING LENGTH OF LIST********************
print(len(bikes))
