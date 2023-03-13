import re

class UserInfoValidator:
    def check_fname(self, fname):
        if not isinstance(fname, str):
            raise TypeError("First name must be a string")

        if len(fname) > 20:
            raise ValueError("First name must be <= 20 characters long")

    def check_lname(self, lname):
        if not isinstance(lname, str):
            raise TypeError("Last name must be a string")

        if len(lname) > 20:
            raise ValueError("Last name name must be <= 20 characters long")

    def check_address(self, address):
        if not isinstance(address, str):
            raise TypeError("Address must be a string")

        if len(address) > 50:
            raise ValueError("Address must be <= 50 characters long")

    def check_city(self, city):
        if not isinstance(city, str):
            raise TypeError("City must be a string")

        if len(city) > 30:
            raise ValueError("City must be <= 30 characters long")

    def check_state(self, state):
        if not isinstance(state, str):
            raise TypeError("State must be a string")

        if len(state) > 20:
            raise ValueError("State must be <= 20 characters long")

    def check_email(self, email):
        if not isinstance(email, str):
            raise TypeError("Email must be a string")

        if len(email) > 40:
            raise ValueError("Email must be <= 40 characters long")

        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[. ]\w{2,3}$'
        match = re.fullmatch(regex, email)

        if not match:
            raise ValueError("Email is not in a valid format")

    def check_password(self, password):
        if not isinstance(password, str):
            raise TypeError("Password must be a string")

        if len(password) < 10 | len(password) > 100:
            raise TypeError("Password must be between 10 and 100 characters long")

    def check_phone(self, phone):
        if not isinstance(phone, str):
            raise TypeError("Phone must be a string")

        if len(phone) > 12:
            raise ValueError("Phone must be <= 12 characters long")

    def check_credit_card_type(self, credit_card_type):
        if not isinstance(credit_card_type, str):
            raise TypeError("Credit card type must be a string")

        if len(credit_card_type) > 10:
            raise ValueError("Credit card type must be <= 10 characters long")

    def check_credit_card_number(self, credit_card_number):
        if not isinstance(credit_card_number, str):
            raise TypeError("Credit card number must be a string")

        if len(credit_card_number) != 10:
            raise ValueError("Credit card number must be 16 characters long")
