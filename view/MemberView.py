from view.actions.MemberActions import MemberActions
from view.actions.BookActions import BookActions
from view.actions.SearchActions import SearchActions

class MemberView:
    def __init__(self, validator):
        self.validator = validator

    def print_menu(self):
        print("\n***** Member Menu *****\nb : Browse by subject\ns : Search by author/title\nc : Checkout\nl : Logout")

    def print_browse_header(self):
        print("\n----- Browse by subject -----")

    def print_search_header(self):
        print("\n----- Search by author/title -----")

    def print_search_options(self):
        print("a : Author search\nt : Title search\nr : Return")

    def print_checkout_header(self):
        print("----- Checkout -----")

    def print_cart_success(self):
        print("Successfully added to cart!")

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
            case "isbn":
                return self.get_isbn()
            case "quantity":
                return self.get_quantity()
            case "search_action":
                return self.get_search_action()
            case "search_term":
                return self.get_search_term()
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

    def get_isbn(self):
        isbn = input("ISBN: ")
        self.validator.check_isbn(isbn)
        return isbn

    def get_quantity(self):
        quantity = None
        try:
            quantity = int(input("Quantity: "))
        except ValueError as error:
            raise ValueError("Quantity must be a number") from error

        self.validator.check_quantity(quantity)
        return quantity
    
    def get_search_action(self):
        """
        Gets search action.

        Returns
        -------
        Search
        """
        value = input("Search choice: ")

        for action in SearchActions:
            if value == action.value:
                return SearchActions(value)

        raise ValueError(value + " is not a vaild search choice")

    def get_search_term(self):
        search_term = input("Search term: ")
        self.validator.check_search_term(search_term)
        return search_term
