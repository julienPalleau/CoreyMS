

def summer_69(*args):
    sum = 0
    switch = True
    for x in args[0]:
        if x == 6:
            switch = False
        elif x == 9:
            switch = True
        elif switch:
            sum += x
    print(sum)


summer_69([1, 3, 5])  # --> 9
summer_69([4, 5, 6, 7, 8, 9])  # --> 9
summer_69([2, 1, 6, 9, 11])  # --> 14
summer_69([])  # --> 0

print("\nAmedeo solution")


def summer_69b(arr):
    while 6 in arr:
        start, stop = arr.index(6), arr.index(9)+1
        del arr[start:stop]
    result = 0
    for n in arr:
        result += n
    return result


print(summer_69b([1, 3, 5]))  # --> 9
print(summer_69b([4, 5, 6, 7, 8, 9]))  # --> 9
print(summer_69b([2, 1, 6, 9, 11]))  # --> 14
print(summer_69b([]))  # --> 0
