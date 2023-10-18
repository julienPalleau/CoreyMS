"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9407968#search
List Comprehension
"""
# This is a beginer solution!
mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)

print(mylist)

# There is a more efficient way to do the same as above:
my_list = [letter for letter in mystring]
print(my_list)

mylist = [letter for letter in 'word']
print(mylist)

mylist = [num for num in range(0, 11)]
print(mylist)

mylist = [num**2 for num in range(0, 11)]
print(mylist)

mylist = [x**2 for x in range(0, 11) if x % 2 == 0]
print(mylist)

celcius = [0, 10, 20, 34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)

# You can have an if/else in list comprehension but you should avoid them as it not easily readable!!!
# Remember Readibility FIRST !!!
celcius = [num for num in range(0, 11)]
results = [x if x % 2 == 0 else 'ODD' for x in celcius]
print(results)

# nested loops with list comprehension, same remark as above.
mylist = [x*y for x in [2, 4, 6] for y in [1, 10, 1000]]
print(mylist)