"""
Classes:

    MemberView
"""


from tabulate import tabulate
from datetime import date, timedelta

from view.actions.MemberActions import MemberActions
from view.actions.BookActions import BookActions
from view.actions.SearchActions import SearchActions
from view.actions.CheckoutActions import CheckoutActions

class MemberView:
    """
    Represents a member view.

    Attributes
    -------
    validator : view.validators.MemberViewValidator
        a MemberViewValidator object

    Methods
    -------
    __init__(validator)
        Initializing constructor.
    print_menu()
        Prints the menu.
    print_browse_header()
        Prints the browse header.
    print_search_header()
        Prints the search header.
    print_search_options()
        Prints the search options.
    print_checkout_header()
        Prints the checkout header.
    print_cart_success(self)
        Prints cart success.
    print_logout_success()
        Prints logout success
    print_error_message(message)
        Prints error message.
    get_input(input_type, subjects)
        Gets user input of the provided type.
    get_member_action()
        Gets member action.
    get_book_action()
        Gets book action.
    print_subjects(subjects)
        Prints the available book subjects.
    get_subject(subjects)
        Gets a subject from the user.
    print_book_count(count)
        Prints book count.
    print_books(books)
        Prints books.
    get_isbn()
        Gets an ISBN from the user.
    get_quantity()
        Gets book quantity from the user.
    get_search_action()
        Gets search action from the user.
    get_search_term()
        Gets a search term from the user.
    print_carts(carts, total_cost)
        Prints the user's carts.
    get_checkout_action()
        Gets checkout action from the user.
    print_invoice(member, carts, total_cost)
        Prints the invoice of the user.
    """
    def __init__(self, validator):
        self.validator = validator

    def print_menu(self):
        """Prints the menu."""
        print("\n***** Member Menu *****\nb : Browse by subject\ns : Search by author/title\nc : Checkout\nl : Logout")

    def print_browse_header(self):
        """Prints the browse header."""
        print("\n----- Browse by subject -----")

    def print_search_header(self):
        """Prints the search header."""
        print("\n----- Search by author/title -----")

    def print_search_options(self):
        """Prints the search options."""
        print("a : Author search\nt : Title search\nr : Return")

    def print_checkout_header(self):
        """Prints the checkout header."""
        print("\n----- Checkout -----")

    def print_cart_success(self):
        """Prints cart success."""
        print("Successfully added to cart!")

    def print_logout_success(self):
        """Prints logout success"""
        print("Successfully logged out!")

    def print_error_message(self, message):
        """Prints error message."""
        print(message)

    def get_input(self, input_type, subjects):
        """Gets user input of the provided type."""
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
            case "checkout_action":
                return self.get_checkout_action()
            case _:
                raise ValueError(input_type + " is not a valid argument value")

    def get_member_action(self):
        """Gets member action."""
        value = input("Menu choice: ")

        for action in MemberActions:
            if value == action.value:
                return MemberActions(value)

        raise ValueError(value + " is not a vaild menu choice")
    
    def get_book_action(self):
        """Gets book action."""
        value = input("Book choice: ")

        for action in BookActions:
            if value == action.value:
                return BookActions(value)

        raise ValueError(value + " is not a vaild book choice")
    
    def print_subjects(self, subjects):
        """Prints the available book subjects."""
        for key in subjects.keys():
            print(key + " : " + subjects[key])

    def get_subject(self, subjects):
        """Gets a subject from the user."""
        input_value = input("Subject choice: ")
        for key in subjects.keys():
            if input_value == key:
                return subjects[key]

        raise ValueError(input_value + " is not a valid subject choice")
    
    def print_book_count(self, count):
        """Prints book count."""
        print("\n" + str(count) + " books were found")
    
    def print_books(self, books):
        """Prints books."""
        if len(books) == 0:
            print("\nThere are no more books")
        for book in books:
            print()
            for key in book.keys():
                print(key + ": " + str(book[key]))
        print("\na : Add book to cart\nl : Load more books\nr : Return")

    def get_isbn(self):
        """Gets an ISBN from the user."""
        isbn = input("ISBN: ")
        self.validator.check_isbn(isbn)
        return isbn

    def get_quantity(self):
        """Gets book quantity from the user."""
        quantity = None
        try:
            quantity = int(input("Quantity: "))
        except ValueError as error:
            raise ValueError("Quantity must be a number") from error

        self.validator.check_quantity(quantity)
        return quantity
    
    def get_search_action(self):
        """Gets search action from the user."""
        value = input("Search choice: ")

        for action in SearchActions:
            if value == action.value:
                return SearchActions(value)

        raise ValueError(value + " is not a vaild search choice")

    def get_search_term(self):
        """Gets a search term from the user."""
        search_term = input("Search term: ")
        self.validator.check_search_term(search_term)
        return search_term

    def print_carts(self, carts, total_cost):
        """Prints the user's carts."""
        print("\nCart content: ")
        print (tabulate(carts, headers="keys"))
        print("Total cost: " + str(round(total_cost, 2)) + " $")

    def get_checkout_action(self):
        """Gets checkout action from the user."""
        value = input("\nProceed with checkout (y/n): ")

        for action in CheckoutActions:
            if value == action.value:
                return CheckoutActions(value)

        raise ValueError(value + " is not a vaild checkout choice")
    
    def print_invoice(self, member, carts, total_cost):
        """Prints the invoice of the user."""
        print("\n¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤ Invoice ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
        print("\nShipping/billing address:\n" + member["fname"] + " " + member["lname"] +
                "\n" + member["address"] + "\n" + member["city"] + "\n" + member["state"] + " " + str(member["zip"]))
        self.print_carts(carts, total_cost)
        print("\nExpected delivery date: " + str(date.today() + timedelta(days=7)))
        print("\n¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
        input("\nPress enter to exit")
