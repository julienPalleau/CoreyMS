import random

lottery_numbers = set(random.sample(range(22), 6))

players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

result = 0
for index in range(len(players)):
    if 100 ** len(players[index]['numbers'].intersection(lottery_numbers)) > result:
        result = 100 ** len(players[index]['numbers'].intersection(lottery_numbers))
        name = players[index]['name']
        var = players[index]['name']

print(f"{name} won {result}")
