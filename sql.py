import mysql.connector
from mysql.connector import Error
#creating connection to the db
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error {e} ocurred.")
    return connection

def execute_query(connection, query, values=None):
    cursor = connection.cursor()
    try:
        if values:
            cursor.execute(query, values)
        else: #had to use the else statement or was getting error message
            cursor.execute(query)
        connection.commit() #commiting the changes in the query
        print("Query executed successfully")
    except Error as e:
        print(f"The error {e} ocurred.")

def execute_read_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error {e} ocurred.")
