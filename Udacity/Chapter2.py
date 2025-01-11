# Data Structures
# Types of Data Structures: Lists, Tuples, Sets, Dictionaries, Compound Data Structures
# Operators: Membership, Identity
# Built-In Functions or Methods

# list : mutable ordered sequence of elements
# Data structures are containers that organize and group data types together in different ways. A list is one of the most common and basic data structures in Python
my_list=["hello",3,78.6,True,"last",23]
# positive index and negative index
print(my_list[0],my_list[-4])
print(my_list[1],my_list[-3])
print(my_list[2],my_list[-2])
# print(my_list[25]) # IndexError: list index out of range
print(my_list[len(my_list) - 1])  # finding last element
#Slicing 
# my_list[startinclude : end excluded]
print(my_list[:9]) # start with 0 to 9
print(my_list[3:]) # start with 3 to len of string.
print(my_list[2:5]) # 2 indexed item is included and 5 indexed item is excluded.


# Memebership operators for string & list
# 1 IN : if item is present this will return true
# 2 NOT IN : if item is not present this will return true
print( True In my_list)
