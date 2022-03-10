#bikes = ['honda','yamaha','suzuki','tata','c','f','g']
#print(bikes[0:2]) #prints first 2 elements
#print(bikes[1:4]) #prints second, third & fourth element
#print(bikes[:3])  #prints from zeroth to second element
#print(bikes[2:])  #prints from second element to last element
#print(bikes[-1:]) #prints from last element in reverse order
#print(bikes[0:7:2]) #prints from first element to last along with one element skipping
#*************************Looping through a slice*******************************
#players=['charles','martin','michael','florence','eli']
#print("These are first 3 players in my team:")
#for player in players[:3]:
#    print(player.title())
#*************************copying a list*******************************
my_foods=['pizza','burger','pasta','canoli','cakes',]
friend_foods=my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)