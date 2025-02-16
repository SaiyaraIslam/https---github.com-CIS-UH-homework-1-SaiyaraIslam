import creds
from sql import create_connection
from sql import execute_query


#creating db connection
myCreds = creds.Creds()
conn = create_connection(myCreds.conString,myCreds.userName, myCreds.password, myCreds.dbName)

query = "INSERT INTO vault (VaultNum, VaultCode, Content, Owner) VALUES (%s, %s, %s, %s)"
values = (100, 12345, "This is secret content from vault 1", "AI Capone")
execute_query(conn, query, values)