from mysql.connector import connect


class database:

    def __init__(self, username, password) -> None:
        self.connection = connect(host="localhost", user=username, password=password, database="book_store")


    def __get_cursor__(self):
        return self.connection.cursor()


    def execute_with_fetchall(self, query):
        with self.__get_cursor__() as cursor:
            cursor.execute(query)
            return cursor.fetchall()


    def execute_with_commit(self, query):
        with self.__get_cursor__() as cursor:
            cursor.execute(query)
            self.connection.commit()
