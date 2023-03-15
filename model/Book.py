"""
Classes:

    Book
"""

import os
from mysql.connector import connect, Error
from model.errors.DBError import DBError

class Book:
    """
    Represents a main menu.

    Methods
    -------
    get_subjects()
        Gets all subjects.
    get_count_by_subject(subject)
        Gets the count of the books of the current subject.
    browse_by_subject(subject, offset)
        Gets the books of the current subject.
    get_count_by_author(search_term)
        Gets the count of the books of authors containing the current search term.
    search_by_author(search_term, offset)
        Gets the books of authors containing the current search term.
    get_count_by_title(search_term)
        Gets the count of the books with titles containing the current search term.
    search_by_title(self, search_term, offset)
        Gets the books with titles containing the current search term.
    conv_one_value_tupl_to_dict(tuples)
        Converts one-value tuples to one dictionary.
    make_pretty(text)
        Makes text pretty by making the first character uppercase and the rest of the characters lowercase.
    make_books_pretty(books)
        Makes the representation of the books pretty.
    make_book_pretty(book)
        Makes the representation of a book pretty.
    is_book_in_db(isbn)
        Checks if the current book is in the database.
    """

    def get_subjects(self):
        """Gets all subjects."""
        try:
            connection = None
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
            if connection:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

    def get_count_by_subject(self, subject):
        """Gets the count of the books of the current subject."""
        try:
            connection = None
            connection = connect(
                host="localhost",
                database="book_store",
                user=os.environ["USER"],
                password=os.environ["PASSWORD"]
            )
            cursor = connection.cursor()
            query = "SELECT COUNT(*) FROM books WHERE subject = %s"
            cursor.execute(query, (subject,))
            return cursor.fetchall()[0][0]
        except Error as error:
            raise DBError("Database error, failed to get book count") from error
        finally:
            if connection:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

    def browse_by_subject(self, subject, offset):
        """Gets the books of the current subject."""
        try:
            connection = None
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
            if connection:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

    def get_count_by_author(self, search_term):
        """Gets the count of the books of authors containing the current search term."""
        try:
            connection = None
            connection = connect(
                host="localhost",
                database="book_store",
                user=os.environ["USER"],
                password=os.environ["PASSWORD"]
            )
            cursor = connection.cursor()
            query = """SELECT COUNT(*) FROM books WHERE author LIKE concat("%", %s, "%")"""
            cursor.execute(query, (search_term,))
            return cursor.fetchall()[0][0]
        except Error as error:
            raise DBError("Database error, failed to get book count") from error
        finally:
            if connection:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

    def search_by_author(self, search_term, offset):
        """Gets the books of authors containing the current search term."""
        try:
            connection = None
            connection = connect(
                host="localhost",
                database="book_store",
                user=os.environ["USER"],
                password=os.environ["PASSWORD"]
            )
            cursor = connection.cursor(dictionary=True)
            query = """SELECT * FROM books WHERE author LIKE concat("%", %s, "%") LIMIT %s, 3;"""
            cursor.execute(query, (search_term, offset))
            books = cursor.fetchall()
            return self.make_books_pretty(books)
        except Error as error:
            raise DBError("Database error, failed to fetch books") from error
        finally:
            if connection:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

    def get_count_by_title(self, search_term):
        """Gets the count of the books with titles containing the current search term."""
        try:
            connection = None
            connection = connect(
                host="localhost",
                database="book_store",
                user=os.environ["USER"],
                password=os.environ["PASSWORD"]
            )
            cursor = connection.cursor()
            query = """SELECT COUNT(*) FROM books WHERE title LIKE concat("%", %s, "%")"""
            cursor.execute(query, (search_term,))
            return cursor.fetchall()[0][0]
        except Error as error:
            raise DBError("Database error, failed to get book count") from error
        finally:
            if connection:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

    def search_by_title(self, search_term, offset):
        """Gets the books with titles containing the current search term."""
        try:
            connection = None
            connection = connect(
                host="localhost",
                database="book_store",
                user=os.environ["USER"],
                password=os.environ["PASSWORD"]
            )
            cursor = connection.cursor(dictionary=True)
            query = """SELECT * FROM books WHERE title LIKE concat("%", %s, "%") LIMIT %s, 3;"""
            cursor.execute(query, (search_term, offset))
            books = cursor.fetchall()
            return self.make_books_pretty(books)
        except Error as error:
            raise DBError("Database error, failed to fetch books") from error
        finally:
            if connection:
                if connection.is_connected():
                    cursor.close()
                    connection.close()

    def conv_one_value_tupl_to_dict(self, tuples):
        """Converts one-value tuples to one dictionary."""
        dict = {}
        count = 1
        for tupl in tuples:
            value = tupl[0]
            dict[str(count)] = self.make_pretty(value)
            count = count + 1
        return dict

    def make_pretty(self, text):
        """Makes text pretty by making the first character uppercase and the rest of the characters lowercase."""
        return text[0].upper() + text[1:].lower()

    def make_books_pretty(self, books):
        """Makes the representation of the books pretty."""
        books_pretty = []
        for book in books:
            books_pretty.append(self.make_book_pretty(book))

        return books_pretty

    def make_book_pretty(self, book):
        """Makes the representation of a book pretty."""
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

    def is_book_in_db(self, isbn):
        """Checks if the current book is in the database."""
        try:
            connection = None
            connection = connect(
                host="localhost",
                database="book_store",
                user=os.environ["USER"],
                password=os.environ["PASSWORD"]
            )
            cursor = connection.cursor()
            query ="SELECT COUNT(*) FROM books WHERE isbn = %s"
            cursor.execute(query, (isbn,))
            count = cursor.fetchall()[0][0]
            if count == 1:
                return True
            return False
        except Error as error:
            raise DBError("Database error, failed to check ISBN") from error
        finally:
            if connection:
                if connection.is_connected():
                    cursor.close()
                    connection.close()
