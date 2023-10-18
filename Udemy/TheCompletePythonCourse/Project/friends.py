# Ask the user for a list of 3 friends
# For each friend, we'll tell the user wether tey are nearby
# For each nearby friend, we'll save their name to 'nearby_friends.txt'

# hint: readlines()
import re

list_friends = input("Entrer le nom de 3 amis separer par une virgule: ")
my_file_people = open('people.txt', 'r')
my_file_nearby_friends = open('nearby_friends.txt', 'w')
file_content = my_file_people.read()

# for friend in list_friends.split(", |,"):
for friend in re.split(', |,', list_friends):
    if friend in file_content:
        my_file_nearby_friends.write(f"{friend}\n")
        print(f'{friend} is nearby! Meet up with them.')

my_file_nearby_friends.close()
my_file_people.close()
