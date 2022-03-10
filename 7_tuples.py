# tuples are immutable whereas lists are mutable

dimensions=(200,100,50,25)
print(dimensions[0])
print(dimensions[1])
print(dimensions[3])

list1=[]
print(type(list1))

int1=(3)   #without a comma indicates int type
print(type(int1))

tuple1=(3,)  #presence of comma and parenthesis is technically defined as tuple
print(type(tuple1))