"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9388536#search
Dictionaries
"""
prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}
print(prices_lookup)
print(prices_lookup['apple'])
d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey': 100}}
print(d['k2'])
print(d['k3']['insideKey'])
print(d['k2'][2])

d = {'k1': 100, 'k2': 200}
d['k3'] = 300
print(d)
d['k1'] = 'NEW VALUE'
print(d)
d = {'k1': 100, 'k2': 200, 'k3': 300}

print(d.keys())
print(d.values())
print(d.items())

d={'k1':[1,2,3]}
print(d)
print(d['k1'][1])