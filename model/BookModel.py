import os
from mysql.connector import connect, Error
from model.errors.DBError import DBError

class BookModel:
    def get_subjects(self):
        try:
            connection = connect(
                host="localhost",
                database="book_store",
                user=os.environ["USER"],
                password=os.environ["PASSWORD"]
            )
            cursor = connection.cursor()
            query = """SELECT subject FROM books
                        GROUP BY subject
                        ORDER BY subject ASC"""
            cursor.execute(query)
            subjects = cursor.fetchall()
            return self.conv_one_value_tupl_to_dict(subjects)
        except Error as error:
            raise DBError("Database error, failed to fetch subjects") from error
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def get_books(self, subject, offset):
        try:
            connection = connect(
                host="localhost",
                database="book_store",
                user=os.environ["USER"],
                password=os.environ["PASSWORD"]
            )
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM books WHERE subject = %s LIMIT %s, 2;"
            cursor.execute(query, (subject, offset))
            books = cursor.fetchall()
            return self.make_books_pretty(books)
        except Error as error:
            raise DBError("Database error, failed to fetch books") from error
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def conv_one_value_tupl_to_dict(self, tuples):
        dict = {}
        count = 1
        for tupl in tuples:
            value = tupl[0]
            dict[str(count)] = self.make_pretty(value)
            count = count + 1
        return dict

    def make_pretty(self, text):
        return text[0].upper() + text[1:].lower()

    def make_books_pretty(self, books):
        books_pretty = []
        for book in books:
            books_pretty.append(self.make_book_pretty(book))

        return books_pretty

    def make_book_pretty(self, book):
        book_pretty = {}
        for key in book.keys():
            key_pretty = None
            value_pretty = book[key]
            if key.upper() == "ISBN":
                key_pretty = key.upper()
            else:
                key_pretty = self.make_pretty(key)
            if key.lower() == "subject":
                value_pretty = self.make_pretty(book[key])
            book_pretty[key_pretty] = value_pretty
        return book_pretty
