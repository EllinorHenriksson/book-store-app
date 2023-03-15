"""
Classes:

    MemberMenu
"""

from model.errors.DBError import DBError
from view.actions.MemberActions import MemberActions
from view.actions.BookActions import BookActions
from view.actions.SearchActions import SearchActions
from view.actions.CheckoutActions import CheckoutActions

class MemberMenu:
    """
    Represents a member menu.

    Attributes
    ----------
    view : view.MemberView
        a MemberView object
    book_model : model.Book
        a Book object
    cart_model : model.Cart
        a Cart object
    order_model : model.Order
        an Order object
    odetail_model : model.Odetails
        an Odetails object
    member : {"userid": int, "fname": str, "lname": str, "address": str, "city": str, "state": str, "zip": int, "phone": str}

    Methods
    -------
    ___init__(view, book_model, cart_model, order_model, odetails_model):
        Initializing constructor.
    run(member)
        Runs the member menu.
    browse()
        Lets the user browse through the books by subject.
    get_input(input_type, subjects = None)
        Gets input from the user of the specified type.
    show_books_by_subject(subject, offset)
        Shows books browsed by subject to the user.
    add_book_to_cart()
        Adds a book to a cart.
    search()
        Lets the user search for books by search term in author/title.
    search_by_author()
        Lets the user search for books by search term in author.
    search_by_title()
        Lets the user search for books by search term in title.
    show_books_by_title(search_term, offset)
        Shows books searched by title to the user.
    checkout()
        Lets the user check out.
    perform_checkout(carts, total_cost)
        Actually performs the checkout.
    logout()
        Logs out the user.
    """

    def __init__(self, view, book_model, cart_model, order_model, odetails_model):
        self.view = view
        self.book_model = book_model
        self.cart_model = cart_model
        self.order_model = order_model
        self.odetails_model = odetails_model

        self.member = None

    def run(self, member):
        """Runs the member menu."""
        self.member = member
        run_menu = True
        while run_menu:
            self.view.print_menu()
            try:
                choice = self.get_input("member_action")
                if choice == MemberActions.BROWSE:
                    self.browse()
                elif choice == MemberActions.SEARCH:
                    self.search()
                elif choice == MemberActions.CHECKOUT:
                    self.checkout()
                else:
                    run_menu = False
            except (ValueError, DBError) as error:
                self.view.print_error_message(str(error))

        self.logout()

    def browse(self):
        """Lets the user browse through the books by subject."""
        self.view.print_browse_header()
        subjects = self.book_model.get_subjects()
        self.view.print_subjects(subjects)
        subject = self.get_input("subject", subjects)
        book_count = self.book_model.get_count_by_subject(subject)
        self.view.print_book_count(book_count)
        if book_count > 0:
            self.show_books_by_subject(subject, 0)

    def get_input(self, input_type, subjects = None):
        """Gets input from the user of the specified type."""
        input_value = None
        while not input_value:
            try:
                input_value = self.view.get_input(input_type, subjects)
                return input_value
            except (ValueError) as error:
                self.view.print_error_message(str(error))

    def show_books_by_subject(self, subject, offset):
        """Shows books browsed by subject to the user."""
        books = self.book_model.browse_by_subject(subject, offset)
        self.view.print_books(books)
        book_action = self.get_input("book_action")
        if book_action == BookActions.ADD:
            self.add_book_to_cart()
        elif book_action == BookActions.LOAD:
            self.show_books_by_subject(subject, offset + 2)

    def add_book_to_cart(self):
        """Adds a book to a cart."""
        isbn = self.get_input("isbn")
        if self.book_model.is_book_in_db(isbn):
            pass
        else:
            self.view.print_error_message("There is no book with the provided ISBN")
            self.add_book_to_cart()

        quantity = self.get_input("quantity")
        self.cart_model.update_cart(self.member["userid"], isbn, quantity)
        self.view.print_cart_success()

    def search(self):
        """Lets the user search for books by search term in author/title."""
        self.view.print_search_header()
        self.view.print_search_options()
        action = self.get_input("search_action")

        if action == SearchActions.AUTHOR:
            self.search_by_author()
        elif action == SearchActions.TITLE:
            self.search_by_title()

    def search_by_author(self):
        search_term = self.get_input("search_term")
        book_count = self.book_model.get_count_by_author(search_term)
        self.view.print_book_count(book_count)
        if book_count > 0:
            self.show_books_by_author(search_term, 0)

    def show_books_by_author(self, search_term, offset):
        """Lets the user search for books by search term in author."""
        books = self.book_model.search_by_author(search_term, offset)
        self.view.print_books(books)
        book_action = self.get_input("book_action")
        if book_action == BookActions.ADD:
            self.add_book_to_cart()
        elif book_action == BookActions.LOAD:
            self.show_books_by_author(search_term, offset + 3)

    def search_by_title(self):
        """Lets the user search for books by search term in title."""
        search_term = self.get_input("search_term")
        book_count = self.book_model.get_count_by_title(search_term)
        self.view.print_book_count(book_count)
        if book_count > 0:
            self.show_books_by_title(search_term, 0)

    def show_books_by_title(self, search_term, offset):
        """Shows books searched by title to the user."""
        books = self.book_model.search_by_title(search_term, offset)
        self.view.print_books(books)
        book_action = self.get_input("book_action")
        if book_action == BookActions.ADD:
            self.add_book_to_cart()
        elif book_action == BookActions.LOAD:
            self.show_books_by_title(search_term, offset + 3)

    def checkout(self):
        """Lets the user check out."""
        self.view.print_checkout_header()
        carts = self.cart_model.get_carts(self.member["userid"])
        if len(carts) > 0:
            total_cost = self.cart_model.get_total_cost(self.member["userid"])
            self.view.print_carts(carts, total_cost)
            action = self.get_input("checkout_action")
            if action == CheckoutActions.YES:
                self.perform_checkout(carts, total_cost)

        else:
            self.view.print_error_message("There is no cart content")

    def perform_checkout(self, carts, total_cost):
        """Actually performs the checkout."""
        order_number = self.order_model.create(self.member["userid"])
        for cart in carts:
            self.odetails_model.create({
                "order_number": order_number,
                "isbn": cart["ISBN"],
                "quantity": cart["Quantity"],
                "total_price": cart["Total"]
            })
            self.cart_model.delete(self.member["userid"], cart["ISBN"])

        self.view.print_invoice(self.member, carts, total_cost)

    def logout(self):
        """Logs out the user."""
        self.member = None
        self.view.print_logout_success()