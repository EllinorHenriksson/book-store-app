from controller.MainMenuActions import MainMenuActions
from model.Member import Member

class MainView:
    def __init__(self, validator):
        self.validator = validator
        self.menu = "\n***** Main Menu *****\nr : Register\nl : Login\nq : Quit"

    def print_text(self, text):
        """Prints the given text."""
        print(text)

    def print_menu(self):
        """Prints the menu."""
        print(self.menu)

    def get_action(self):
        """
        Gets user action.

        Returns
        -------
        MainMenuAction
        """
        value = input("Enter menu choice: ")

        for action in MainMenuActions:
            if value == action.value:
                return MainMenuActions(value)

        raise ValueError(value + " is not a vaild menu choice")

    def print_error(self, message):
        print(message)

    def get_email(self):
        email = input("Email: ")
        self.validator.check_email(email)
        return email

    def get_password(self):
        password = input("Password: ")
        self.validator.check_password(password)
        return password

    def get_fname(self):
        fname = input("First name: ")
        self.validator.check_fname(fname)
        return fname

    def get_lname(self):
        lname = input("Last name: ")
        self.validator.check_lname(lname)
        return lname

    def get_address(self):
        address = input("Address: ")
        self.validator.check_address(address)
        return address

    def get_zip_code(self):
        try:
            return int(input("Zip code: "))
        except ValueError:
            raise ValueError("Zip code must consist of numbers")

    def get_city(self):
        city = input("City: ")
        self.validator.check_city(city)
        return city

    def get_state(self):
        state = input("State: ")
        self.validator.check_state(state)
        return state

    def get_phone(self):
        phone = input("Phone: ")
        self.validator.check_phone(phone)
        return phone

    def get_credit_card_type(self):
        credit_card_type = input("Credit card type: ")
        self.validator.check_credit_card_type(credit_card_type)
        return credit_card_type

    def get_credit_card_number(self):
        credit_card_number = input("Credit card number: ")
        self.validator.check_credit_card_number(credit_card_number)
        return credit_card_number
