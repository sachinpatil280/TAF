import mysql.connector
import psycopg2
from mysql.connector import Error


class DbUtils:

    def __init__(self, host, user, password, database_name, port=0):
        self.host = host
        self.user = user
        self.password = password
        self.database = database_name
        self.port = port

    def execute_mysql_query(self, query):
        connection = None
        db_cursor = None
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database)

            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                conn = connection
                db_cursor = conn.cursor()
                db_cursor.execute(query)
                record = db_cursor.fetchall()
                return record

        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                db_cursor.close()
                connection.close()

    def execute_postgres_query(self, query):
        connection = None
        db_cursor = None
        try:
            connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database)

            conn = connection
            db_cursor = conn.cursor()
            db_cursor.execute(query)
            record = db_cursor.fetchall()
            return record

        except Error as e:
            print("Error while connecting to Postgres", e)
        finally:
            db_cursor.close()
            connection.close()
