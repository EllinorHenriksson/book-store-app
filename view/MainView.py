from controller.MainMenuActions import MainMenuActions

class MainView:
    def __init__(self):
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

    def register(self):
        email = input("Email: ")
        fname = input("First name: ")
        lname = input("Last name: ")
        address = input("Address: ")
        city = input("City: ")
        state = input("State: ")

        zip_code = 0
        try:
            zip_code = int(input("Zip code: "))
        except ValueError:
            raise ValueError("Zip code must only consist of numbers")

        phone = input("Phone (optional): ")
        password = input("Password: ")
        credit_card_type = input("Credit card type (optional): ")
        credit_card_number = input("Credit card number (optional): ")
