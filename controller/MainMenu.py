"""
Classes:

    MainMenu
"""

from view.actions.MainActions import MainActions
from model.errors.DBError import DBError

class MainMenu:
    """
    Represents a main menu.

    Attributes
    ----------
    view : view.MainView
        a MainView object
    member_model : model.Member
        an Member object
    member_menu : controller.MemberMenu
        an MemberMenu object

    Methods
    -------
    ___init__(view, member_model, member_menu):
        Initializing constructor.
    run()
        Runs the main menu.
    register()
        Lets the user register.
    get_unique_email()
        Gets a unique email from the user.
    get_input(input_type)
        Gets input from the user of the specified type.
    login()
        Lets the user log in.
    """

    def __init__(self, view, member_model, member_menu):
        self.view = view
        self.member_model = member_model
        self.member_menu = member_menu

    def run(self):
        """Runs the main menu."""
        self.view.print_welcome_message()
        run_menu = True
        while run_menu:
            self.view.print_menu()
            try:
                choice = self.get_input("main_action")
                if choice == MainActions.REGISTER:
                    self.register()
                elif choice == MainActions.LOGIN:
                    self.login()
                else:
                    run_menu = False
            except (ValueError, DBError) as error:
                self.view.print_error_message(str(error))

    def register(self):
        """Lets the user register."""
        self.view.print_register_header()

        member = {
            "email": self.get_unique_email(),
            "password": self.get_input("password"),
            "fname": self.get_input("fname"),
            "lname": self.get_input("lname"),
            "address": self.get_input("address"),
            "zip_code": self.get_input("zip_code"),
            "city": self.get_input("city"),
            "state": self.get_input("state"),
            "phone": self.get_input("phone")
        }

        self.member_model.create(member)
        self.view.print_registration_success()

    def get_unique_email(self):
        """Gets a unique email from the user."""
        is_email_unique = False
        while not is_email_unique:
            try:
                email = self.view.get_email()
                is_email_unique = self.member_model.is_email_unique(email)

                if not is_email_unique:
                    self.view.print_error_message("Email is already registered")
                else:
                    return email
            except (ValueError) as error:
                self.view.print_error_message(str(error))

    def get_input(self, input_type):
        """Gets input from the user of the specified type."""
        input_value = None
        while not input_value:
            try:
                input_value = self.view.get_input(input_type)
                return input_value
            except (ValueError) as error:
                self.view.print_error_message(str(error))

    def login(self):
        """Lets the user log in."""
        self.view.print_login_header()
        credentials = {
            "email": self.get_input("email"),
            "password": self.get_input("password")
        }

        try:
            member = self.member_model.login(credentials)
            self.view.print_login_success()
            self.member_menu.run(member)
        except (ValueError) as error:
            self.view.print_error_message(str(error))
