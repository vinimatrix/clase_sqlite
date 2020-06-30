import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn



def create_table(conn, create_table_sql):
    try:
        c= conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database ='pythonsql.db'
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                        );"""
    conn = create_connection(database)
    if conn is not None:
        create_table(conn,sql_create_projects_table)
    else:
        print("Error! cannot create the database connection.")
if __name__ == '__main__':
    main()        

