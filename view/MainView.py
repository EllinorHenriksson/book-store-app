"""
Classes:

    MainView
"""

from view.actions.MainActions import MainActions

class MainView:
    """
    Represents a main view.

    Attributes
    -------
    validator : view.validators.MainViewValidator
        a MainViewValidator object

    Methods
    -------
    __init__(validator)
        Initializing constructor.
    print_welcome_message()
        Prints a welcome message.
    print_menu()
        Prints the menu.
    print_register_header()
        Prints the register header.
    print_login_header()
        Prints the register header.
    print_registration_success()
        Prints registration success message.
    print_login_success()
        Prints login success message.
    print_error_message(message)
        Prints error message.
    get_input(input_type)
        Gets user input of the provided type.
    get_main_action()
        Gets main action from user.
    get_email()
        Gets email from user.
    get_password()
        Gets password from user.
    get_fname()
        Gets first name from user.
    get_lname()
        Gets last name from user.
    get_address()
        Gets address from user.
    get_city()
        Gets city from user.
    get_state()
        Gets state from user.
    get_zip_code()
        Gets zip code from user.
    get_phone()
        Gets phone number from user.
    """

    def __init__(self, validator):
        self.validator = validator

    def print_welcome_message(self):
        """Prints a welcome message."""
        print("########## Welcome to the Book Store ##########")

    def print_menu(self):
        """Prints the menu."""
        print("\n***** Main Menu *****\nr : Register\nl : Login\nq : Quit")

    def print_register_header(self):
        """Prints the register header."""
        print("\n----- Register -----")

    def print_login_header(self):
        """Prints the login header."""
        print("\n----- Login -----")

    def print_registration_success(self):
        """Prints registration success message."""
        print("Successfully registered!")

    def print_login_success(self):
        """Prints login success message."""
        print("Successfully logged in!")

    def print_error_message(self, message):
        """Prints error message."""
        print(message)

    def get_input(self, input_type):
        """Gets user input of the provided type."""
        match input_type:
            case "main_action":
                return self.get_main_action()
            case "email":
                return self.get_email()
            case "password":
                return self.get_password()
            case "fname":
                return self.get_fname()
            case "lname":
                return self.get_lname()
            case "address":
                return self.get_address()
            case "zip_code":
                return self.get_zip_code()
            case "city":
                return self.get_city()
            case "state":
                return self.get_state()
            case "phone":
                return self.get_phone()
            case "credit_card_type":
                return self.get_credit_card_type()
            case "credit_card_number":
                return self.get_credit_card_number()
            case _:
                raise ValueError(input_type + " is not a valid argument value")
            
    def get_main_action(self):
        """Gets main action from user."""
        value = input("Menu choice: ")

        for action in MainActions:
            if value == action.value:
                return MainActions(value)

        raise ValueError(value + " is not a vaild menu choice")

    def get_email(self):
        """Gets email from user."""
        email = input("Email: ")
        self.validator.check_email(email)
        return email

    def get_password(self):
        """Gets password from user."""
        password = input("Password: ")
        self.validator.check_password(password)
        return password

    def get_fname(self):
        """Gets first name from user."""
        fname = input("First name: ")
        self.validator.check_fname(fname)
        return fname

    def get_lname(self):
        """Gets last name from user."""
        lname = input("Last name: ")
        self.validator.check_lname(lname)
        return lname

    def get_address(self):
        """Gets address name from user."""
        address = input("Address: ")
        self.validator.check_address(address)
        return address

    def get_zip_code(self):
        """Gets zip code from user."""
        try:
            return int(input("Zip code: "))
        except ValueError:
            raise ValueError("Zip code must consist of numbers")

    def get_city(self):
        """Gets city from user."""
        city = input("City: ")
        self.validator.check_city(city)
        return city

    def get_state(self):
        """Gets state from user."""
        state = input("State: ")
        self.validator.check_state(state)
        return state

    def get_phone(self):
        """Gets phone number from user."""
        phone = input("Phone: ")
        self.validator.check_phone(phone)
        return phone