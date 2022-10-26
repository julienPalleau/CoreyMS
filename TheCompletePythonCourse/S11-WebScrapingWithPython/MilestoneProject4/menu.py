import logging

from app import books

logger = logging.getLogger('scrapping.menu')

USER_CHOICE = '''Enter on of the following
- 'b' to look at ordered books by number of stars
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the catalogue
- 't' list of books ordered by price and stars
- 'q' to exit

Enter your choice: '''


def print_best_books():
    logger.info('Finding best books by rating...')
    best_books = sorted(books, key=lambda x: x.rating * -1)[:10]
    for book in best_books:
        print(book)
    print("\n")


def print_cheapest_books():
    logger.info('Finding best books by price...')
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)
    print("\n")


# Sorting by 2 criteria
def print_two_criteria():
    logger.info('Finding best books by two criteria...')
    two_criteria = sorted(books, key=lambda x: (x.rating * -1, x.price))[:10]
    for book in two_criteria:
        print(book)
    print("\n")


books_generator = (x for x in books)


def get_next_book():
    logger.info('Getting next book from generator of all books...')
    print(next(books_generator))


user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': get_next_book,
    't': print_two_criteria,
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b', 'c', 'n', 't', 'x'):
            user_choices[user_input]()
        else:
            print('Please choose a valid command.')
        user_input = input(USER_CHOICE)
    logger.debug('Terminating program...')


menu()
