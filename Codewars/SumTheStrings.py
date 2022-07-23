def sum_str(a, b):
    if (a == "" and b == ""):
        a = 0
        b = 0
    elif (a == ""):
        a = 0
    elif (b == ""):
        b = 0

    result = int(a) + int(b)
    return str(f"{result}")


print(sum_str("", ""))
