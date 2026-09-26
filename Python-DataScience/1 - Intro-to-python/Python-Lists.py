# Python Lists
"""
Python Data Types
float - real numbers
int - integer numbers
str - string, text
bool - True, False
"""
# we can create python lists using square brackets
#  a list is a way to give name a collection of values
# we can have any type in lists
#  we can have lists inside Lists 
[45,56,67]

# we can access items in a List using indexes
# python uses zero indexing
# we can access from the end using - indexing

# we also get  
# Slicing -  allows selecting multiple items from a list 
# slicing syntax [start(inclusive):end(exclusive)] 
# we can access items backward using negative indexing

# a python list can have another list inside - to subset lists of lists we use the sa technique of square brackets
# say we have a lists list investments[[longgterm][bonds],[shortterm][trading]] - we can get elements by 
# subsetting just like in a normal list eg to get the value for shortterm investments 
# investment[-1][1] 


# Manipulating lists (change list elemets, Add ,remove)
# we use the square brackets and the assignment operator
# we can add values in a list using the + operator and we can remove tehm using the del keyword 
# eg del investment[2]

# understandign how python handles lisst under the hood
#  python store a refrence of the variable in memory ....if yu assign another variable the 1st variable
# changes in values reflects on both 
 
#  to cretae a separate refrence we can use the method list() and it cretaes a new refrence assignin gthe variable