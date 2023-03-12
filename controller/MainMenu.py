from controller.MainMenuActions import MainMenuActions

class MainMenu:
    def __init__(self, view):
        self.view = view
    def run(self):
        """Runs the main menu"""
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
                self.view.print_error(error)

        self.quit_app()

    def register(self):
        print("Register")

    def login(self):
        print("Login")

    def quit_app(self):
        print("Quit program")
