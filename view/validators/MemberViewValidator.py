import re

class MemberViewValidator:
    def check_isbn(self, isbn):
        regex = "^\d{10}$"
        match = re.fullmatch(regex, isbn)
        if not match:
            raise ValueError("The ISBN must consist of 10 numbers")

    def check_quantity(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be above 0")
        
    def check_search_term(self, search_term):
        if len(search_term) == 0:
            raise ValueError("Search term must contain at least one character")

