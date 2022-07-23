# coding:utf-8

print("Multiple of 3 and 5")
# Multiple of 3 and 5
result = []
total = 0
for i in range(1, 1000):
    if (i % 3 == 0):
        result.append(i)
    elif (i % 5 == 0):
        result.append(i)
for value in result:
    total += value

print(total)

print("\nSum of Even Fibonacci numbers")
# Even Fibonacci numbers
x = 0
y = 1
z = 0
total = 0
while (z < 4000000):
    z = x + y
    x = y
    y = z
    if (z % 2 == 0):
        total += z

print(total)

print("\nLargest prime factor")
# Largest prime factor
