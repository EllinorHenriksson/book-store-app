"""
Classes:

    MainViewValidator
"""

import re

class MainViewValidator:
    """
    Represents a main view validator.

    Methods
    -------
    check_fname(fname)
        Checks that the first name is correct.
    check_lname(lname)
        Checks that the last name is correct.
    check_address(address)
        Checks that the address is correct.
    check_city(city)
        Checks that the city is correct.
    check_state(state)
        Checks that the state is correct.
    check_email(email)
        Checks that the email is correct.
    check_password(password)
        Checks that the password is correct.
    check_phone(phone)
        Checks that the phone is correct.
    """
    def check_fname(self, fname):
        """Checks that the first name is correct."""
        if len(fname) == 0 or len(fname) > 20:
            raise ValueError("First name must be <= 20 characters long")

    def check_lname(self, lname):
        """Checks that the last name is correct."""
        if len(lname) == 0 or len(lname) > 20:
            raise ValueError("Last name name must be <= 20 characters long")

    def check_address(self, address):
        """Checks that the address is correct."""
        if len(address) == 0 or len(address) > 50:
            raise ValueError("Address must be <= 50 characters long")

    def check_city(self, city):
        """Checks that the city is correct."""
        if len(city) == 0 or len(city) > 30:
            raise ValueError("City must be <= 30 characters long")

    def check_state(self, state):
        """Checks that the state is correct."""
        if len(state) == 0 or len(state) > 20:
            raise ValueError("State must be <= 20 characters long")

    def check_email(self, email):
        """Checks that the email is correct."""
        if len(email) == 0 or len(email) > 40:
            raise ValueError("Email must be <= 40 characters long")

        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[. ]\w{2,3}$'
        match = re.fullmatch(regex, email)

        if not match:
            raise ValueError("Email is not in a valid format")

    def check_password(self, password):
        """Checks that the password is correct."""
        if len(password) < 10 or len(password) > 100:
            raise ValueError("Password must be between 10 and 100 characters long")

    def check_phone(self, phone):
        """Checks that the phone is correct."""
        if len(phone) == 0 or len(phone) > 12:
            raise ValueError("Phone must be <= 12 characters long")
