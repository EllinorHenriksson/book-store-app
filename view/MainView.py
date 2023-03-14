from view.actions.MainActions import MainActions

class MainView:
    def __init__(self, validator):
        self.validator = validator

    def print_welcome_message(self):
        """Prints a welcome message."""
        print("########## Welcome to the Book Store ##########")

    def print_menu(self):
        """Prints the menu."""
        print("\n***** Main Menu *****\nr : Register\nl : Login\nq : Quit")

    def print_register_header(self):
        print("\n----- Register -----")

    def print_login_header(self):
        print("\n----- Login -----")

    def print_registration_success(self):
        print("Successfully registered!")

    def print_login_success(self):
        print("Successfully logged in!")

    def print_error_message(self, message):
        """Prints error message."""
        print(message)

    def get_input(self, input_type):
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
        """
        Gets main action.

        Returns
        -------
        MainAction
        """
        value = input("Menu choice: ")

        for action in MainActions:
            if value == action.value:
                return MainActions(value)

        raise ValueError(value + " is not a vaild menu choice")

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
