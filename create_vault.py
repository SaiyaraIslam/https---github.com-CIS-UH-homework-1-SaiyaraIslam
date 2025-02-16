import mysql.connector
import creds
from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execute_read_query

#creating db connection
myCreds = creds.Creds()
conn = create_connection(myCreds.conString,myCreds.userName, myCreds.password, myCreds.dbName)

query = "INSERT INTO vault (VaultNum, VaultCode, Content, Owner) VALUES (%s, %s, %s, %s)"
