"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9388552#search
Files
"""
myfile = open('myfile.txt')
print(myfile.read())
print(myfile.read())  # Nothing will be printed !
# The reason why the second print doesn't print anything is because we move the cursor at the end of the file after
# the first print. So, to read it again we have to reset the cursor!

myfile.seek(0)  # reset the cursor
print(myfile.read())

print("")
print("Read a txt file located with the python script")
myfile.seek(0)
print(myfile.readlines())
myfile.close()

print("")
print("Read a txt file located somewhere else")
myfile = open("C:\\Users\\MOTTIER LUCIE\\Documents\\GitHub\\Udemy\\CompletePythonBootcampFromZeroToHeroInPython\\Folder\\myfile.txt")
print(myfile.read())
myfile.close()

# Best practice
with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()

print("")
print("Best practice")
print(contents)
print("")

# Let's look at what you can do on a file: read, write, append, reading and writing, writing and reading
# mode='r' is read only
# mode='w' is write only (will overwrite files or create new!)
# mode='a' is append only (will add on to files)
# mode='r+' is reading and writing
# mode='w+' is writing and reading (Overwrites existing files or creates a new file!)
print("")
with open('my_new_file', mode='r') as f:
    print(f.read())

print("")
print("Append FOUR ON FOURTH")
with open('my_new_file', mode='a') as f:
    f.write('\nFOUR ON FOURTH')

with open('my_new_file', mode='r') as f:
    print(f.read())

with open('dhfjdkshfjdks.txt', mode='w') as f:
    f.write('I CREATED THIS FILE!')