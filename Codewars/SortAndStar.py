def two_sort(array):
    i = 0
    result = ""
    array.sort()
    print(array[0][-1])
    for letter in array[0]:
        i += 1
        if (i == len(array[0])):
            result += letter
        else:
            result += letter+"***"
    return result


print(two_sort(["bitcoin", "take", "over", "the", "world",
                "maybe", "who", "knows", "perhaps"]))
