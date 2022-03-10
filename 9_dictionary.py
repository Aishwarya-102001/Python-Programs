alien={'color':'green','points':5}
# print(alien['color'])
# print(alien['points'])

print(alien)
alien['x-position']=0   #adding new key-value pair
alien['y-position']=25  #adding new key-value pair
print(alien) 

alien['color']='yellow' #modifying values in dictionary
print(alien)

del alien['points']  #deletes the respective key-value pair PERMANENTLY
print(alien)

#******************dictionary with similar objects*****************
favorite_languages={
    'jen':'python',
    'sarah':'C',
    'edward':'C++',
    'john':'java',
    'jenelia':'ruby',
}
language=favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language} ")

#********************Looping through all key-value pairs***************
favorite_languages={
    'jen':'python',
    'sarah':'C',
    'edward':'C++',
    'john':'python',
    'jenelia':'ruby',
}
for key,value in favorite_languages.items():  #items() method would list down all key-value pairs
    print(f"{key.title()}'s favorite language is {value.title()}")

print("\nOutput is using sorted() function: ")
for key,value in sorted(favorite_languages.items()):   #sorted() function sorts the dictionary according to the keys
    print(f"{key.title()}'s favorite language is {value.title()}")

print("\n")
#********************Looping through all keys only (BY DEFAULT)***************
print("The keys are as follows: ")
for key1 in favorite_languages.keys():   #keys() method would list down through all keys only
    print(key1.title())

print("\n")
# if 'erin' not in favorite_languages.keys():   #checks whether a particular key is present in the dictionary
#     print("Erin, please take our poll first!!")

#********************Looping through all values only***************
print("The following languages WITH repetition are: ")
for value in favorite_languages.values():   #values() method would list down through all values only
    print(value.title())
print("\n")

print("The following languages WITHOUT repetition are: ")
for value in set(favorite_languages.values()):   #set() is colllection in which each item is identified as unique one
    print(value.title())
print("\n")

#******************using get() method to access values*****************
alien={'color':'green'}
#print(alien['points'])  #this gives a traceback KeyError
print(alien.get('points','No point value assigned')) 
# if there's a chance the key you're asking for might not exist,
# consider get() method instead of square bracket notation
