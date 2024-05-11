


#SET
first_set = {0,9,7,3,44,5}
print("Original Set:",first_set)

#adding a new element in the set
first_set.add(1)
print("Updated Set",first_set)

#Removing an element form the set
first_set.remove(44)
print("Updated Set",first_set)

#Modification in the set
first_set.discard(5)
first_set.add(99)
print("Updated Set",first_set)

#DICTIONARY
first_dict = {'Name':'Darry','Age':35,'City':'Chennai'}
print("Original Dictionary:",first_dict)

#Adding in dictionary
first_dict['Year of birth'] = 1989
print("Updated Dictionary:",first_dict)

#Removing From dictionary

del first_dict['Age']
print("Updated Dictionary",first_dict)

#modifying the dictionary
first_dict['city'] = 'Ranchi'
print("Updated Dictionary",first_dict)

#LIST
first_list = [7,8,9,10,12]
print("Original List:",first_list)

#adding an element to list
first_list.append(16)
print ("Updated List:",first_list)

#Removing an element from the list
first_list.remove(10)
print ("Updated List:",first_list)

#Modification in a list
first_list[2] = 13
print ("Updated List:",first_list)
