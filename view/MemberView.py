from view.actions.MemberActions import MemberActions

class MemberView:
    def print_menu(self):
        print("\n***** Member Menu *****\nb : Browse by subject\ns : Search by author/title\nc : Checkout\nl : Logout")

    def print_browse_header(self):
        print("\n----- Browse by subject -----")

    def print_logout_success(self):
        print("Successfully logged out!")

    def print_error_message(self, message):
        """Prints error message."""
        print(message)

    def get_action(self):
        """
        Gets user action.

        Returns
        -------
        MemberAction
        """
        value = input("Menu choice: ")

        for action in MemberActions:
            if value == action.value:
                return MemberActions(value)

        raise ValueError(value + " is not a vaild menu choice")
    
    def get_input(self, input_type):
        match input_type:
            case "isbn":
                return self.get_ISBN()
            case _:
                raise ValueError(input_type + " is not a valid argument value")

    def print_subjects(self, subjects):
        for key in subjects.keys():
            print(key + " : " + subjects[key])

    def get_subject(self, subjects):
        input_value = input("Subject choice: ")
        for key in subjects.keys():
            if input_value == key:
                return subjects[key]

        raise ValueError(input_value + " is not a valid subject choice")