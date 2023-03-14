import os
import bcrypt
from mysql.connector import connect, Error
from model.errors.DBError import DBError

class MemberModel:
    def is_email_unique(self, email):
        try:
            connection = connect(
                host="localhost",
                database="book_store",
                user=os.environ["USER"],
                password=os.environ["PASSWORD"]
            )
            cursor = connection.cursor()
            query ="SELECT * FROM members WHERE email = %s"
            cursor.execute(query, (email,))
            if len(cursor.fetchall()) == 0:
                return True
            return False
        except Error as error:
            raise DBError("Database error, failed to check email") from error
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def create_member(self, member):
        # Hashes password
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(member["password"].encode(), salt)

        # Creates member
        try:
            connection = connect(
                host="localhost",
                database="book_store",
                user=os.environ["USER"],
                password=os.environ["PASSWORD"]
            )
            cursor = connection.cursor()
            query = ("INSERT INTO members "
                "(email, password, fname, lname, address, zip, city, state, phone) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
            data = (member["email"], hashed, member["fname"], member["lname"],
                    member["address"], member["zip_code"], member["city"], member["state"],
                    member["phone"])
            cursor.execute(query, data)
            connection.commit()
        except Error as error:
            raise DBError("Database error, failed to create an account") from error
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def login(self, credentials):
        try:
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
            if connection.is_connected():
                cursor.close()
                connection.close()
