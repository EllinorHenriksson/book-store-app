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
            subjects_tupl = cursor.fetchall()
            subjects_dict = {}
            count = 1
            for row in subjects_tupl:
                subject = row[0]
                subjects_dict[str(count)] = subject[0].upper() + subject[1:].lower()
                count = count + 1
            return subjects_dict
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

    def make_books_pretty(self, books):
        books_pretty = []
        for book in books:
            books_pretty.append(self.make_book_pretty(book))

    def make_book_pretty(self, book):
        book_pretty = {}
        for key in book.keys():
            key_pretty = None
            if key.upper() == "ISBN":
                key_pretty = key.upper()
            else:
                key_pretty = key[0].upper() + key[1:].lower()
            book_pretty[key_pretty] = book[key]
        return book_pretty