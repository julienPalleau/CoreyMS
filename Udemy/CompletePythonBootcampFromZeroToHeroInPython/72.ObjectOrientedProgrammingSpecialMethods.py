"""
https://www.udemy.com/course/complete-python-bootcamp/learn/lecture/9478306#search
Object Oriented Programming Part Four
"""


class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # String representation
    def __str__(self):
        return f"{self.title} by {self.author}"

    # Length
    def __len__(self):
        return self.pages

    # Delete
    def __del__(self):
        print("A book object has been deleted")


b = Book('Python rocks', 'Jose', 200)
print(b)
print(len(b))
del b

