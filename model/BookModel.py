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
            for x in range(len(subjects_tupl)):
                subjects_dict[str(x + 1)] = subjects_tupl[x]
            return subjects_dict
        except Error as error:
            raise DBError("Database error, failed to fetch subjects") from error
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
