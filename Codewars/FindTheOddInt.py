def find_it(seq):
    temp = 0
    seq.sort()
    for i in seq:
        if (seq.count(i) % 2 != 0 and temp != i):
            temp = i
            print(i)
            return i


print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
print(find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5])
find_it([10])
find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1])
find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10])
