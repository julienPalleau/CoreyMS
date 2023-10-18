def check(list1):

    counter = 0
    i = 0
    j = 0
    # print("list1 =", list1)

    # check vertical
    for i in range(6):
        # print("i", i)
        # print("i+1", i+1)
        if (i <= 6):
            # print("list1[i][0] =", list1[i][0])
            # print("list1[i+1][0] =", list1[i+1][0])
            if list1[int(i)][0] == 'X' and list1[int(i+1)][0] == 'X':
                counter += 1
                print("counter :", counter)
        if (counter >= 2):
            return True

    # check horizontal
    for j in range(6, -1, -1):
        # print("j", j)
        # print("j+1", j+1)
        if (j <= 5):
            # print(f"list1[6][{j}] =", list1[6][j])
            # print(f"list1[6][{j+1}] =", list1[6][j+1])
            if list1[6][int(j)] == 'X' and list1[6][int(j+1)] == 'X':
                counter += 1
                print("counter :", counter)
        if (counter >= 2):
            return True

    # check for diagonals

    return False
