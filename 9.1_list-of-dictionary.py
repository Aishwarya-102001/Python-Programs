#****************List of Dictionary*************************
# alien1={'color':'green','points':5}
# alien2={'color':'red','points':15}
# alien3={'color':'yellow','points':10}

# aliens=[alien1,alien2,alien3]   #list called aliens is created which has 3 dictionaries

# for alien in aliens:
#     print(alien)

#****************List of Dictionary using range() function*************************
aliens=[]

for alien_number in range(30):   #Make 30 aliens using range() and append them in aliens list
    new_alien = {'color':'green','points':5, 'speed':'slow'}
    aliens.append(new_alien)

# for alien in aliens[:5]:  #print first 5 aliens
#     print(alien)

for alien in aliens[:3]:
    if alien ['color'] == 'green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10

for alien in aliens[:5]:  #print first 5 aliens with changed values
    print(alien)

print("*********************************")

print(f"The total number of aliens: {len(aliens)}")

print("*********************************")
