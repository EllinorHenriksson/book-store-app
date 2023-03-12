import re
import bcrypt

class Member:
    def __init__(self, email):
        self.set_email(email)

    def set_fname(self, fname):
        if not isinstance(fname, str):
            raise TypeError("First name must be a string")

        if len(fname) > 20:
            raise ValueError("First name must be <= 20 characters long")

        self.fname = fname

    def set_lname(self, lname):
        if not isinstance(lname, str):
            raise TypeError("Last name must be a string")

        if len(lname) > 20:
            raise ValueError("Last name name must be <= 20 characters long")

        self.lname = lname

    def set_address(self, address):
        if not isinstance(address, str):
            raise TypeError("Address must be a string")

        if len(address) > 50:
            raise ValueError("Address must be <= 50 characters long")

        self.address = address

    def set_city(self, city):
        if not isinstance(city, str):
            raise TypeError("City must be a string")

        if len(city) > 30:
            raise ValueError("City must be <= 30 characters long")

        self.city = city

    def set_state(self, state):
        if not isinstance(state, str):
            raise TypeError("State must be a string")

        if len(state) > 20:
            raise ValueError("State must be <= 20 characters long")

        self.state = state

    def set_zip_code(self, zip_code):
        if not isinstance(zip_code, int):
            raise TypeError("Zip code must be an integer")

        self.zip_code = zip_code

    def set_email(self, email):
        if not isinstance(email, str):
            raise TypeError("Email must be a string")

        if len(email) > 40:
            raise ValueError("Email must be <= 40 characters long")

        regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
        re.search(regex, email)

        # OBS! Fortsätt här! Kolla vad som händer med regex

        self.email = email

    def set_password(self, password):
        if not isinstance(password, str):
            raise TypeError("Password must be a string")

        # Hashes password
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password, salt)
        self.password = hashed

    def set_phone(self, phone):
        if not isinstance(phone, str):
            raise TypeError("Phone must be a string")

        if len(phone) > 12:
            raise ValueError("Phone must be <= 12 characters long")

        self.phone = phone

    def set_credit_card_type(self, credit_card_type):
        if not isinstance(credit_card_type, str):
            raise TypeError("Credit card type must be a string")

        if len(credit_card_type) > 10:
            raise ValueError("Credit card type must be <= 10 characters long")

        self.credit_card_type = credit_card_type

    def set_credit_card_number(self, credit_card_number):
        if not isinstance(credit_card_number, str):
            raise TypeError("Credit card number must be a string")

        if len(credit_card_number) != 10:
            raise ValueError("Credit card number must be 16 characters long")

        self.credit_card_number = credit_card_number

