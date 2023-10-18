import random


def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


# board = 10 * " "
test_board = ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-']


def choose_first():
    player = random.choice(['X', 'O'])
    return player


def full_board_check(board):
    if "-" in board:
        return False
    else:
        return True


def place_marker(board, mark, position):
    board[position] = mark
    return board


def player_input():
    position = 11
    while position not in range(1, 10):
        position = int(input("Entrer une position (1..10): "))

    return mark, position


def reset():
    return ['#', '-', '-', '-', '-', '-', '-', '-', '-', '-']


def win_check(board, mark):
    win_value = 0
    print(board[1] == board[2] == board[3] == mark, mark)
    print(board[4] == board[5] == board[6] == mark, mark)
    print(board[7] == board[8] == board[9] == mark, mark)
    print(board[1] == board[5] == board[9] == mark, mark)
    print(board[7] == board[5] == board[3] == mark, mark)
    print("")
    if board[1] == board[2] == board[3] == mark or board[4] == board[5] == board[6] == mark or \
            board[7] == board[8] == board[9] == mark or board[1] == board[5] == board[9] == mark or \
            board[7] == board[5] == board[3] == mark or board[1] == board[4] == board[7] == mark or \
            board[2] == board[5] == board[8] == mark or board[3] == board[6] == board[9] == mark:
        print("True")
        return True
    else:
        print("False")
        return False


play = "y"
mark = choose_first()
while play == "y":
    if mark == "X":
        mark = "O"
    else:
        mark = "X"
    marker, position = player_input()
    display_board(place_marker(test_board, marker, position))
    if win_check(test_board, marker):
        print("Bravo vous avez gagne cette partie de TicTacToe !!!")
        play = input("Voulez vous faire une autre partie? y/n: ")
        test_board = reset()
        display_board(test_board)
    elif full_board_check(test_board):
        print("Vous avez perdu :-(")
        play = input("Voulez vous faire une autre partie? y/n: ")
        test_board = reset()
        display_board(test_board)
