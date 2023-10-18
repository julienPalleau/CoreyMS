from MilestoneProject2.DB.Utils import database


def prompt_add_book():
    name = input("Nom du livre : ")
    author = input("Autheur du livre : ")
    database.add_book(name, author)


def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")


def prompt_read_book():
    name = input("What is the name of the book you read: ")
    database.mark_book_as_read(name)


def prompt_delete_book():
    name = input("Nom du livre a supprimer?")
    database.delete_book(name)


USER_CHOICE = """
 Enter:
 - 'a' to add a new book
 - 'l' to list all books
 - 'r' to mark a book as read
 - 'd' to delete a book
 - 'q' to quit

 Your choice:"""

user_options = {
    'a': prompt_add_book,
    'l': list_books,
    'r': prompt_read_book,
    'd': prompt_delete_book,
}


def menu():
    database.create_book_table()
    selection = input(USER_CHOICE)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('unknown, try again')
        selection = input(USER_CHOICE)
    # def prompt_add_book() ask for book name and author
    # def list_books() show all the books in our list
    # def prompt_read_book() ask for book name and change it to "read" in our list
    # def_prompt_delete_book() ask for book name and remove book from list


menu()
