nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

friend = input("name of a friend")

# Add the name to the empty set
user_friends.add(friend)

# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
print(user_friends.intersection(nearby_people))