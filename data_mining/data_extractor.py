#From https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
import sqlite3
from sqlite3 import Error
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn



#General function for sqlite queries
def execQuery(conn,query,print_out=True,limit=0):
    if(limit!=0):
        query += " LIMIT "+str(limit)
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    
    
    if(print_out):
        for row in rows:
            print(row)



#Example
conn = create_connection("./database.sqlite")
query = "SELECT * FROM Match"
execQuery(conn,query,limit=10)



