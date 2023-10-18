lottery_numbers = {13, 21, 22, 5, 8}

player1 = {"player0": {1, 2, 3, 4, 5}}
player2 = {"player1": {6, 7, 8, 9, 10}}
name = [player1, player2]

for i in range(len(name)):
    print(f"players{i}", len(name[i][f"player{i}"].intersection(lottery_numbers)))

