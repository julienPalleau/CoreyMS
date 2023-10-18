import timeit

code_to_test = """
def summer_69(arr):
    while 6 in arr:
        start, stop = arr.index(6), arr.index(9)+1
        del arr[start:stop]
    result = 0
    for n in arr:
        result += n
    return result

summer_69([4, 5, 6, 7, 8, 9])
"""

elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)

code_to_test2 = """
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
    return sum



summer_69([4, 5, 6, 7, 8, 9])
"""
elapsed_time2 = timeit.timeit(code_to_test2, number=100)/100
print(elapsed_time2)
