"""
Classes:

    Odetails
"""

import os
from mysql.connector import connect, Error
from model.errors.DBError import DBError

class Odetails:
    """
    Represents order details.

    Methods
    -------
    create(data)
        Creates new order details.
    """
    def create(self, data):
        """Creates new order details."""
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
            INSERT INTO odetails (ono, isbn, qty, price)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (data["order_number"], data["isbn"], data["quantity"], data["total_price"]))
            connection.commit()
        except Error as error:
            if connection:
                connection.rollback()
            raise DBError("Database error, failed to create order details") from error
        finally:
            if connection:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
