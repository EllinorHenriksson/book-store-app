from controller.MainMenuActions import MainMenuActions

class MainView:
    def __init__(self):
        self.menu = "r : Register\nl : Login\nq : Quit"

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
