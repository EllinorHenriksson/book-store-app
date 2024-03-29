"""
Classes:

    Member
"""

import os
import bcrypt
from mysql.connector import connect, Error
from model.errors.DBError import DBError

class Member:
    """
    Represents a Member.

    Methods
    -------
    is_email_unique(self, email)
        Checks if the current email is unique.
    create(member)
        Creates a new member.
    login(credentials)
        Tries to log in the user.
    """

    def is_email_unique(self, email):
        """Checks if the current email is unique."""
        try:
            connection = None
            connection = connect(
                host="localhost",
                database="book_store",
                user=os.environ["USER"],
                password=os.environ["PASSWORD"]
            )
            cursor = connection.cursor()
            query ="SELECT COUNT(*) FROM members WHERE email = %s"
            cursor.execute(query, (email,))
            count = cursor.fetchall()[0][0]
            if count == 0:
                return True
            return False
        except Error as error:
            raise DBError("Database error, failed to check email") from error
        finally:
            if connection:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

    def create(self, member):
        """Creates a new member."""
        # Hashes password
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(member["password"].encode(), salt)

        # Creates member
        try:
            connection = None
            connection = connect(
                host="localhost",
                database="book_store",
                user=os.environ["USER"],
                password=os.environ["PASSWORD"]
            )
            cursor = connection.cursor()
            query = """
                INSERT INTO members (email, password, fname, lname, address, zip, city, state, phone)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
            data = (member["email"], hashed, member["fname"], member["lname"],
                    member["address"], member["zip_code"], member["city"], member["state"],
                    member["phone"])
            cursor.execute(query, data)
            connection.commit()
        except Error as error:
            if connection:
                connection.rollback()
            raise DBError("Database error, failed to create an account") from error
        finally:
            if connection:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

    def login(self, credentials):
        """Tries to log in the user."""
        try:
            connection = None
            connection = connect(
                host="localhost",
                database="book_store",
                user=os.environ["USER"],
                password=os.environ["PASSWORD"]
            )
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM members WHERE email = %s"
            cursor.execute(query, (credentials["email"],))
            members = cursor.fetchall()
            if len(members) == 1:
                member = members[0]
                if bcrypt.checkpw(credentials["password"].encode(), member["password"].encode()):
                    return member
            raise ValueError("Invalid login credentials")
        except Error as error:
            raise DBError("Database error, failed to check user credentials") from error
        finally:
            if connection:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
