from view.actions.MemberActions import MemberActions
from view.actions.BookActions import BookActions
import re

class MemberView:
    def print_menu(self):
        print("\n***** Member Menu *****\nb : Browse by subject\ns : Search by author/title\nc : Checkout\nl : Logout")

    def print_browse_header(self):
        print("\n----- Browse by subject -----")

    def print_logout_success(self):
        print("Successfully logged out!")

    def print_error_message(self, message):
        """Prints error message."""
        print(message)

    def get_input(self, input_type, subjects):
        match input_type:
            case "member_action":
                return self.get_member_action()
            case "book_action":
                return self.get_book_action()
            case "subject":
                return self.get_subject(subjects)
            case "book":
                return self.get_book()
            case _:
                raise ValueError(input_type + " is not a valid argument value")

    def get_member_action(self):
        """
        Gets member action.

        Returns
        -------
        MemberAction
        """
        value = input("Menu choice: ")

        for action in MemberActions:
            if value == action.value:
                return MemberActions(value)

        raise ValueError(value + " is not a vaild menu choice")
    
    def get_book_action(self):
        """
        Gets book action.

        Returns
        -------
        BookAction
        """
        value = input("Book choice: ")

        for action in BookActions:
            if value == action.value:
                return BookActions(value)

        raise ValueError(value + " is not a vaild book choice")
    
    def print_subjects(self, subjects):
        for key in subjects.keys():
            print(key + " : " + subjects[key])

    def get_subject(self, subjects):
        input_value = input("Subject choice: ")
        for key in subjects.keys():
            if input_value == key:
                return subjects[key]

        raise ValueError(input_value + " is not a valid subject choice")
    
    def print_books(self, books):
        for book in books:
            print()
            for key in book.keys():
                print(key + ": " + str(book[key]))
        print("\na : Add book to cart\nl : Load more books\nr : Return")

    def get_book(self):
        book = input("ISBN: ")
        if len(book) != 10:
            raise ValueError("The ISBN must be 10 characters long")

        regex = "^\d+$"
        match = re.fullmatch(regex, book)
        if not match:
            raise ValueError("The ISBN may only consist of numbers")

        return book
