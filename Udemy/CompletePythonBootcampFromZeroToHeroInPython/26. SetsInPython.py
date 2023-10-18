"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9388544#search
Sets
"""
myset = set()
myset.add(1)
print(myset)
myset.add(2)
print(myset)
myset.add(2)
print(myset)

print("")
mylist = [1,1,1,1,1,2,2,2,3,3,3,3]
print(set(mylist))
# Remember set doesn't have any particular order to go in. In the example above it might look like but this is because
# there are just few values. So no order !