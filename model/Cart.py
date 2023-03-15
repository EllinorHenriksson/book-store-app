"""
Classes:

    Cart
"""

import os
from mysql.connector import connect, Error
from model.errors.DBError import DBError

class Cart:
    """
    Represents a cart.

    Methods
    -------
    update_cart(userid, isbn, quantity)
        Checks if cart with user id and isbn exists; updates it if it does, creates a new cart if it doesn't.
    get_carts(userid)
        Gets all carts of the current user.
    get_total_cost(userid)
        Gets the total cost of the books that the user has placed in carts.
    delete(userid, isbn)
        Deletes the cart of the current user and book.
    """
    def update_cart(self, userid, isbn, quantity):
        """Checks if cart with user id and isbn exists; updates it if it does, creates a new cart if it doesn't."""
        try:
            connection = None
            connection = connect(
                host="localhost",
                database="book_store",
                user=os.environ["USER"],
                password=os.environ["PASSWORD"]
            )
            cursor = connection.cursor()
            query ="SELECT COUNT(*) FROM cart WHERE userid = %s AND isbn = %s"
            cursor.execute(query, (userid, isbn))
            count = cursor.fetchall()[0][0]
            if count == 0:
                query ="INSERT INTO cart (userid, isbn, qty) VALUES (%s, %s, %s)"
                cursor.execute(query, (userid, isbn, quantity))
            else:
                query ="UPDATE cart SET qty = %s WHERE userid = %s AND isbn = %s"
                cursor.execute(query, (quantity, userid, isbn))
            connection.commit()
        except Error as error:
            if connection:
                connection.rollback()
            raise DBError("Database error, failed to update cart") from error
        finally:
            if connection:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

    def get_carts(self, userid):
        """Gets all carts of the current user."""
        try:
            connection = None
            connection = connect(
                host="localhost",
                database="book_store",
                user=os.environ["USER"],
                password=os.environ["PASSWORD"]
            )
            cursor = connection.cursor(dictionary = True)
            query ="""
            SELECT C.isbn AS ISBN, B.title AS Title, B.price as Price, C.qty as Quantity, SUM(B.price * C.qty) AS Total
            FROM cart AS C, books AS B 
            WHERE C.isbn = B.isbn AND C.userid = %s 
            GROUP BY B.isbn
            """
            cursor.execute(query, (userid,))
            return cursor.fetchall()
        except Error as error:
            raise DBError("Database error, failed to fetch carts") from error
        finally:
            if connection:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

    def get_total_cost(self, userid):
        """Gets the total cost of the books that the user has placed in carts."""
        try:
            connection = None
            connection = connect(
                host="localhost",
                database="book_store",
                user=os.environ["USER"],
                password=os.environ["PASSWORD"]
            )
            cursor = connection.cursor()
            query ="""
            SELECT SUM(B.price * C.qty) AS total
            FROM cart AS C, books AS B
            WHERE C.isbn = B.isbn AND C.userid = %s
            GROUP BY C.userid;
            """
            cursor.execute(query, (userid,))
            return cursor.fetchall()[0][0]
        except Error as error:
            raise DBError("Database error, failed to fetch total cost") from error
        finally:
            if connection:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

    def delete(self, userid, isbn):
        """Deletes the cart of the current user and book."""
        try:
            connection = None
            connection = connect(
                host="localhost",
                database="book_store",
                user=os.environ["USER"],
                password=os.environ["PASSWORD"]
            )
            cursor = connection.cursor()
            query ="DELETE FROM cart WHERE userid = %s AND isbn = %s"
            cursor.execute(query, (userid, isbn))
            connection.commit()
        except Error as error:
            if connection:
                connection.rollback()
            raise DBError("Database error, failed to delete cart") from error
        finally:
            if connection:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
