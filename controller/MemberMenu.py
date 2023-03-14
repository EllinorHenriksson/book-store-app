from view.actions.MemberActions import MemberActions

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
                choice = self.get_action()
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

    def get_action(self):
        action = None
        while not action:
            try:
                action = self.view.get_action()
                return action
            except ValueError as error:
                self.view.print_error_message(str(error))

    def browse(self):
        subjects = self.book_model.get_subjects()
        subject = self.choose_subject(subjects)
        """
        books = self.book_model.get_books(subject)
        self.view.print_books(books)
        book_option = self.get_book_option()
        
        if book_option == BookActions.ISBN:
            # Add ISBN
        elif book_option == BookActions.NEXT:
            # Swow more books
        elif book_option == BookActions.EXIT:
            # Go back to member menu
            """
        
    def choose_subject(self, subjects):
        subject = None
        while not subject:
            try:
                subject = self.view.choose_subject(subjects)
                return subject
            except (ValueError) as error:
                self.view.print_error_message(str(error))

    def get_input(self, input_type):
        input_value = None
        while not input_value:
            try:
                input_value = self.view.get_input(input_type)
                return input_value
            except (ValueError) as error:
                self.view.print_error_message(str(error))

    def search(self):
        print("Search")

    def checkout(self):
        print("Checkout")

    def logout(self):
        self.member = None
        self.view.print_logout_success()