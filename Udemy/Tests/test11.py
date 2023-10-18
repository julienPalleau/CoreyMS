# coding:utf-8
mylist = []
print(type(mylist))


def table(nb, max=10):
    """Fonction affichant la table de multiplication par nb
    de 1*nb à max*nb
    (max >= 0)"""

    i = 0
    while i < max:
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1


help(table)


def dog_check(my_string):
    return 'dog' in my_string.lower()


print(dog_check('there is a Dog in my garden'))


# map
def square(num):
    return num**2


my_nums = [1, 2, 3, 4, 5]

for item in map(square, my_nums):
    print(item)

print(list(map(square, my_nums)))


def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    else:
        return mystring[0]


names = ['Andy', 'Eve', 'Sally']
print(list(map(splicer, names)))

mynums = [1, 2, 3, 4, 5, 6]
print(list(map(lambda num: num**2, mynums)))
