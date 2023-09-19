# String/sequential data-structures is a collection of characters
# ' '  /  " "
# we can perform CRUD on str 
# the 5th operation is traversing which means going to each element 1 by 1 and reading the data and then perform the crud operations


# CRUD 


# Creation of strings
# s = "John Doe"
# s = "" --or-- s = str() ----> Empty strings

# Reading the String 
# Slicing
# s[start : end+1 : steps]
# s[0:4:1] === s[:4:1] === s[:4]
# s[5:8:1] === s[5::1] === s[5:]
# s[0] --> first
# s[-1] --> last
# s[3::-1]
# s[::] ---> for cloning a string 

# Update 
# we cant update but we can replace
# s[1] = "a" XXXXXXXX 
# a = "abc"
# a = "abcde"

# Delete
# del s --> delets the variable
# s = ""
# s = None 


# input method
# a = input("ABC")

# explicit type conversion
# a = int(input("Number"))