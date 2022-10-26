l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")  # you can't add or delete an element in a tuple
# => list and tuples keep the order of elements.

s = {"bob", "Rolf", "Anne"}  # you can't have duplicate elements in a set

print(l[0])  # gives you the element 0 of the list l
print(t[1])  # gives you the first element of the tuple t
# However you can't write S[2] it doesn't mean anything as element are not in order in set. So Python
# doesn't allow you to write that.

l[0] = "Smith"
print(l)

# t[0] = "Smith"  # you'll get an error because tuples can't be modified after they're created
#
# s[0] = "Smith" # you can't do this for a set because set doesn't allow for subscribe notation


# you can add element to a list:
l.append('Brown')
print(l)

# there is no equivalent of append for tuples because you can't add / remove things from a tuple

# remove element from a list
l.remove('Brown')
print(l)

# add element in a set:
s.add("Smith")  # Notice that it's add and not append, when working with sets. That's because append means "add at the
# end ", but sets don't have and "end" since they don't have order.
s.add("Smith") # you'll notice that there is only one Smith in the result because set don't keep duplicate.
print(s)