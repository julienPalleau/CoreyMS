"""
String indexing and Slicing
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9388528#search
"""
mystring = "Hello World"

# print the first character
print(mystring[0])

# print the eight character
print(mystring[8])

# Let's say we want to print the last l of the sentence
print(mystring[-2])

# We start counting to 0 from left to right and to 1 from right to left !!!
mystring = 'abcdefghijk'

# If we want a subsection of the string from c up to the end
print(mystring[2:])

# If now we want from begining up to c
# Note that the stop index is not included !!!
# So here we go up to letter d, but it is not included
print(mystring[:3])

# it starts at index 3 included and finish at index 6 not included
print(mystring[3:6])

# Let's see step-size
# go all the way from the begining to the end with a step size of two
print(mystring[::2])

# start from index 2 till index 7 but not included with a step size of two
print(mystring[2:7:2])

# print the string in reverse order
print(mystring[::-1])

