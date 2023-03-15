from view.actions.MemberActions import MemberActions
from view.actions.BookActions import BookActions
from model.errors.DBError import DBError
from view.actions.SearchActions import SearchActions

class MemberMenu:
    def __init__(self, view, book_model, cart_model):
        self.view = view
        self.book_model = book_model
        self.cart_model = cart_model

        self.member = None

    def run(self, member):
        """Runs the member menu"""
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
        self.view.print_browse_header()
        subjects = self.book_model.get_subjects()
        self.view.print_subjects(subjects)
        subject = self.get_input("subject", subjects)
        self.show_books_by_subject(subject, 0)

    def get_input(self, input_type, subjects = None):
        input_value = None
        while not input_value:
            try:
                input_value = self.view.get_input(input_type, subjects)
                return input_value
            except (ValueError) as error:
                self.view.print_error_message(str(error))

    def show_books_by_subject(self, subject, offset):
        books = self.book_model.browse_by_subject(subject, offset)
        self.view.print_books(books)
        book_action = self.get_input("book_action")
        if book_action == BookActions.ADD:
            self.add_book_to_cart()
        elif book_action == BookActions.LOAD:
            self.show_books_by_subject(subject, offset + 2)

    def add_book_to_cart(self):
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
        self.view.print_search_header()
        self.view.print_search_options()
        action = self.get_input("search_action")

        if action == SearchActions.AUTHOR:
            self.search_by_author()
        elif action == SearchActions.TITLE:
            self.search_by_title()

    def search_by_author(self):
        search_term = self.get_input("search_term")
        self.show_books_by_author(search_term, 0)

    def show_books_by_author(self, search_term, offset):
        books = self.book_model.search_by_author(search_term, offset)
        self.view.print_books(books)
        book_action = self.get_input("book_action")
        if book_action == BookActions.ADD:
            self.add_book_to_cart()
        elif book_action == BookActions.LOAD:
            self.show_books_by_author(search_term, offset + 3)

    def search_by_title(self):
        search_term = self.get_input("search_term")
        self.show_books_by_title(search_term, 0)

    def show_books_by_title(self, search_term, offset):
        books = self.book_model.search_by_title(search_term, offset)
        self.view.print_books(books)
        book_action = self.get_input("book_action")
        if book_action == BookActions.ADD:
            self.add_book_to_cart()
        elif book_action == BookActions.LOAD:
            self.show_books_by_title(search_term, offset + 3)

    def checkout(self):
        print("Checkout")

    def logout(self):
        self.member = None
        self.view.print_logout_success()