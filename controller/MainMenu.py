from view.actions.MainMenuActions import MainMenuActions
from model.errors.DBError import DBError

class MainMenu:
    def __init__(self, view, member_model):
        self.view = view
        self.member_model = member_model

    def run(self):
        """Runs the main menu"""
        self.view.print_welcome_message()
        run_app = True
        while run_app:
            self.view.print_menu()
            try:
                choice = self.view.get_action()
                if choice == MainMenuActions.REGISTER:
                    self.register()
                elif choice == MainMenuActions.LOGIN:
                    self.login()
                else:
                    run_app = False
            except ValueError as error:
                self.view.print_error_message(str(error))

        self.quit_app()

    def register(self):
        self.view.print_register_header()

        member = {
            "email": self.get_email(),
            "password": self.get_input("password"),
            "fname": self.get_input("fname"),
            "lname": self.get_input("lname"),
            "address": self.get_input("address"),
            "zip_code": self.get_input("zip_code"),
            "city": self.get_input("city"),
            "state": self.get_input("state"),
            "phone": self.get_input("phone")
        }

        try:
            self.member_model.create_member(member)
            self.view.print_registration_success()
        except DBError as error:
            self.view.print_error_message(str(error))

    def get_email(self):
        is_email_unique = False
        while not is_email_unique:
            try:
                email = self.view.get_email()
                is_email_unique = self.member_model.is_email_unique(email)

                if not is_email_unique:
                    self.view.print_error_message("Email is already registered")
                else:
                    return email
            except (ValueError, DBError) as error:
                self.view.print_error_message(str(error))

    def get_input(self, input_type):
        input = None
        while not input:
            try:
                input = self.view.get_input(input_type)
                return input
            except (ValueError) as error:
                self.view.print_error_message(str(error))

    def login(self):
        print("Login")

    def quit_app(self):
        print("Quit program")
