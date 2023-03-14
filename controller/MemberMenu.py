from view.actions.MemberActions import MemberActions
from view.actions.BookActions import BookActions

class MemberMenu:
    def __init__(self, view, book_model):
        self.view = view
        self.book_model = book_model
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
            except ValueError as error:
                self.view.print_error_message(str(error))

        self.logout()

    def browse(self):
        self.view.print_browse_header()
        subjects = self.book_model.get_subjects()
        self.view.print_subjects(subjects)
        subject = self.get_input("subject", subjects)
        self.print_books(subject, 0)

    def get_input(self, input_type, subjects = None):
        input_value = None
        while not input_value:
            try:
                input_value = self.view.get_input(input_type, subjects)
                return input_value
            except (ValueError) as error:
                self.view.print_error_message(str(error))

    def print_books(self, subject, offset):
        books = self.book_model.get_books(subject, offset)
        self.view.print_books(books)
        book_action = self.get_input("book_action")
        if book_action == BookActions.ADD:
            self.add_book_to_cart()
        elif book_action == BookActions.LOAD:
            self.print_books(subject, offset + 2)

    def add_book_to_cart(self):
        book = self.get_input("book")
        # OBS! Fortsätt här!
        # Check if isbn exsists in DB
        # Let user enter quantity
        # Update cart if already existing, or create new cart

    def search(self):
        print("Search")

    def checkout(self):
        print("Checkout")

    def logout(self):
        self.member = None
        self.view.print_logout_success()