#py_practice_2017

#Permutations and Combinations
#Are Python Generators which require for loops to activate or be acted on.  
#Can do cool stuff with join to search massive numbers or combinations or probably to create a game
import itertools

my_letter = ['a','b','c']
comboletter = itertools.combinations(my_letter, 3) #Need iterable sequence and int for characters
print(comboletter) #prints object
for thing in comboletter:
    print(thing) #need for loop to act on object I guess

comboletter = itertools.combinations(my_letter, 2) #will print only 2 letter list combinations
for vice in comboletter:#Output: ('a', 'b') ('a', 'c')  ('b', 'c') 
      print(vice) 

permletter = itertools.permutations(my_letter,3) #creates permutations with 3 items
for miami in permletter:#Output  ('a','b','c') ('a', 'c', 'b')   ('b', 'a', 'c') etc.
     print(miami)


