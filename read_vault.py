import mysql.connector
from sql import create_connection
from sql import execute_query
import creds
# importing all the connections

#connecting to mysql
myCreds = creds.Creds()
conn = conn = create_connection(myCreds.host, myCreds.user, myCreds.password, myCreds.db_name)
# reading the vault content
def read_vault():
    query = "INSERT INTO Content, Owner FRON vault (VaultNum, VaultCode) VALUES (%s, %s)"
    cursor = conn.cursor()
    execute_query(conn, query) #executing the results
