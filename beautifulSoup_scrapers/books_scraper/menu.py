from app import get_all_books


def sort_book_by_price(books):
    return sorted(books, key=lambda book: book.price)


def print_book_info(books):
    for book in books:
        print(book)


def get_five_stars_books(books):
    five_star_books = list(filter(lambda book: book.stars == 5, books))
    expensive_sort = sort_book_by_price(five_star_books)
    expensive_sort.reverse()
    return expensive_sort[:20]


def get_cheapest_books(books):
    cheap_books = sort_book_by_price(books)
    return cheap_books[:20]


def get_next_book(books_generator):
    current_book = next(books_generator)
    return [current_book]


USER_OPTIONS = {
    't': get_five_stars_books,
    'c': get_cheapest_books,
    'n': get_next_book
}

USER_MENU = '''Enter one of the following
- "t": to get the expensive top 20 five-stars books
- "c": to get the top 20 cheapest books
- "n": next book
- "q": quit

Enter your choice: '''


def menu():
    print("getting books.....")
    books = get_all_books()
    print("books loaded!")
    books_generator = (book for book in books)

    user_input = input(USER_MENU)
    while user_input != 'q':
        if user_input in USER_OPTIONS:
            if user_input in ('t', 'c'):
                list_books = USER_OPTIONS.get(user_input)(books)
            else:
                list_books = USER_OPTIONS.get(user_input)(books_generator)
            print_book_info(list_books)

        else:
            print("Enter a valid command")
        user_input = input(USER_MENU)


menu()
