import os
from mysql.connector import connect, Error
from model.errors.DBError import DBError

class CartModel:
    def update_cart(self, userid, isbn, quantity):
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
                connection.commit()
            else:
                query ="UPDATE cart SET qty = %s WHERE userid = %s AND isbn = %s"
                cursor.execute(query, (quantity, userid, isbn))
                connection.commit()
        except Error as error:
            raise DBError("Database error, failed to update cart") from error
        finally:
            if connection:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
