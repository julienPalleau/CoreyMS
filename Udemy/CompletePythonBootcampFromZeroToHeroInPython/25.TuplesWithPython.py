"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9388540#search
Tuples
"""
t = (1,2,3)
mylist = [1, 2, 3]
print(type(t))
print(type(mylist))
x = (1, 2, [1, 2])
print(type(x))

t = ('one', 2)
print(t[0])
print(t[-1])

print("")
print("count and index:")
t = ('a', 'a', 'b')
print(f'tuple: {t}')
print(f"count 'a': {t.count('a')}")
print(f"index 'a': {t.index('a')}")
# Tuples are imutable !

print("")
print(f"mylist: {mylist}")
mylist[0] = 'NEW'
print(mylist)

