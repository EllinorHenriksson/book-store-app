from view.actions.MemberActions import MemberActions

class MemberMenu:
    def __init__(self, view):
        self.view = view
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
        print("Browse")

    def search(self):
        print("Search")

    def checkout(self):
        print("Checkout")

    def logout(self):
        self.member = None
        self.view.print_logout_success()