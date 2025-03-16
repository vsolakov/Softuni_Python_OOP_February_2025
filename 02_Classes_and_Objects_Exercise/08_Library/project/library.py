from project.user import User
class Library:
    def __init__(self):
        self.user_records: list[User] = []
        self.books_available = {}
        self.rented_books: dict[str, dict[str, int]] = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if book_name in self.books_available.keys():
            # if book_name in self.rented_books.values():
            #     for username, nested_dicts in self.rented_books.items():
            #         for book, days_left in nested_dicts.items():
            #             if book == book_name:
            #                 return f'"The book "{book_name}" is already rented and will be available in {days_left} days!'
            u = next((key for key in self.rented_books if book_name in self.rented_books[key]), None)
            if u is not None:
                days_left = self.rented_books[u][book_name]
                return f'"The book "{book_name}" is already rented and will be available in {days_left} days!'
            self.rented_books[user.username] = {book_name: days_to_return}
            self.books_available[author].remove(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"

    def return_book(self, author:str, book_name:str, user: User):

