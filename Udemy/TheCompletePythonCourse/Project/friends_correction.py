# Ask the user a list of 3 friens
# For each friend, we'll tell the user wether tey are nearby
# For each nearby friend, we'll save their name to 'nearby_friends.txt'

# hint: readlines()

friends = input('Enter three friend names, separated by commas (no spaces, please): ').split(',')

people = open('people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()]

people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open('nearby_friends.txt', 'w')

for counter, friend in enumerate(friends_nearby_set):
    if counter == len(friends_nearby_set) - 1:  # this test is to avoid an empty line at the end of nearby_friends.txt
        print(f'{friend} is nearby! Meet up with them.')
        nearby_friends_file.write(f'{friend}')
    else:
        print(f'{friend} is nearby! Meet up with them.')
        nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()
