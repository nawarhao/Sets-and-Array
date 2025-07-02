#Different types of sets in python
#set of integers
my_set = {1, 2, 3}
print(my_set)

#set of mixed datatypes
my_set = {1.0, "hello", (1, 2, 3)}
print(my_set)

#set cannot have duplicates
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)

#we can make set from a list
my_et = set([1, 2, 3, 2])
print(my_set,"\n")

#remove  a number from a set
num_set = set([0, 1, 3, 4, 5])
print("Original set")
print(num_set)
num_set.pop()
print("After removing the first element from the said set:")
print(num_set,"\n")

setx = {"green", "blue"}
sety = {"blue", "yellow"}
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx.intersection(sety)
print(setz)

import array as arr

#create an array
array_num = arr.array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array: "+str(array_num))

#count number of occurences
print("Number of occurences of the number 3 in the said array: "+str(array_num.count(3)))

#reverse the array
array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))

#Character array
character_array = arr.array('u', ['a', 'b', 'c', 'd'])
print(character_array[3])
character_array.append('e')
print(character_array)

#decimal array
decimal_array = arr.array('f', [1.25, 0.5, 1.27])
print(decimal_array[0])
decimal_array.append(13.17)
print(decimal_array)