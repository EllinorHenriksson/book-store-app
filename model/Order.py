"""
Classes:

    Order
"""

import os
from mysql.connector import connect, Error
from model.errors.DBError import DBError
from datetime import date

class Order:
    """
    Represents an order.

    Methods
    -------
    create(userid)
        Creates new order.
    """
    def create(self, userid):
        """Creates new order."""
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
            INSERT INTO orders (userid, received)
            VALUES (%s, %s)
            """
            cursor.execute(query, (userid, date.today()))
            connection.commit()
            return cursor.lastrowid
        except Error as error:
            if connection:
                connection.rollback()
            raise DBError("Database error, failed to create order") from error
        finally:
            if connection:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
