import re

class UserInfoValidator:
    def check_fname(self, fname):
        if len(fname) == 0 or len(fname) > 20:
            raise ValueError("First name must be <= 20 characters long")

    def check_lname(self, lname):
        if len(lname) == 0 or len(lname) > 20:
            raise ValueError("Last name name must be <= 20 characters long")

    def check_address(self, address):
        if len(address) == 0 or len(address) > 50:
            raise ValueError("Address must be <= 50 characters long")

    def check_city(self, city):
        if len(city) == 0 or len(city) > 30:
            raise ValueError("City must be <= 30 characters long")

    def check_state(self, state):
        if len(state) == 0 or len(state) > 20:
            raise ValueError("State must be <= 20 characters long")

    def check_email(self, email):
        if len(email) == 0 or len(email) > 40:
            raise ValueError("Email must be <= 40 characters long")

        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[. ]\w{2,3}$'
        match = re.fullmatch(regex, email)

        if not match:
            raise ValueError("Email is not in a valid format")

    def check_password(self, password):
        if len(password) < 10 or len(password) > 100:
            raise ValueError("Password must be between 10 and 100 characters long")

    def check_phone(self, phone):
        if len(phone) == 0 or len(phone) > 12:
            raise ValueError("Phone must be <= 12 characters long")

    def check_credit_card_type(self, credit_card_type):
        if len(credit_card_type) == 0 or len(credit_card_type) > 10:
            raise ValueError("Credit card type must be <= 10 characters long")

    def check_credit_card_number(self, credit_card_number):
        if len(credit_card_number) != 10:
            raise ValueError("Credit card number must be 16 characters long")
