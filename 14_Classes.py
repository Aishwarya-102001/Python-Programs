class Dog:
    """defining a class(by convention,capitalized names refer to classes in python)"""
    
    def __init__(self,name,age):   #a function that's part of a class is a "method"
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)  #created an instance form class "Dog"
print(f"My dog's name is {my_dog.name} and age is {my_dog.age}.")
my_dog.sit()

your_dog = Dog('Casper', 7)  #created another instance form class "Dog"
print(f"\nYour dog's name is {your_dog.name} and age is {your_dog.age}.")
your_dog.roll_over()