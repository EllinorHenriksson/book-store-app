from view.actions.MemberActions import MemberActions

class MemberView:
    def print_menu(self):
        print("\n***** Member Menu *****\nb : Browse by subject\ns : Search by author/title\nc : Checkout\nl : Logout")

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
            
    def choose_subject(self, subjects):
        for key in subjects.keys():
            print(key + " : " + subjects[key])
        subject = input("Select subject: ")
        # OBS! Fortsätt här! Ovan ger Error
        # Check that subject is correct
        # Translate number into name
        # Return subject
        """
        self.validator.check_subject(subject)
        return subject
        """
