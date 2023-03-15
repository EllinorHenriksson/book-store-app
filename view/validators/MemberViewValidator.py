import re

"""
Classes:

    MemberViewValidator
"""

class MemberViewValidator:
    """
    Represents a member view validator.

    Methods
    -------
    check_isbn(isbn)
        Checks that the isbn is correct.
    check_quantity(quantity)
        Checks that the quantity is correct.
    check_search_term(search_term)
        Checks that the search term is correct.
    """
    def check_isbn(self, isbn):
        """Checks that the isbn is correct."""
        regex = "^\d{10}$"
        match = re.fullmatch(regex, isbn)
        if not match:
            raise ValueError("The ISBN must consist of 10 numbers")

    def check_quantity(self, quantity):
        """Checks that the quantity is correct."""
        if quantity <= 0:
            raise ValueError("Quantity must be above 0")
        
    def check_search_term(self, search_term):
        """Checks that the search term is correct."""
        if len(search_term) == 0:
            raise ValueError("Search term must contain at least one character")

