'''
This script provides a modular way to interact with a SQLite database. You can use the provided functions to create tables, insert data into those tables, and retrieve data from those tables. Additionally, the query_to_df function allows you to easily convert the result of a SQL query to a Pandas DataFrame for further analysis or visualization.
'''

import sqlite3
import pandas as pd

# Function to connect to a database and return a connection object
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
 
    return conn

# Function to execute SQL queries
def execute_query(conn, query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        print("Query executed successfully")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")

# Function to create a table in a database
def create_table(conn, create_table_query):
    execute_query(conn, create_table_query)

# Function to insert data into a table
def insert_data(conn, insert_data_query):
    execute_query(conn, insert_data_query)

# Function to retrieve data from a table
def select_data(conn, select_data_query):
    cursor = conn.cursor()
    cursor.execute(select_data_query)

    rows = cursor.fetchall()

    return rows

# Function to convert a SQLite query result to a Pandas DataFrame
def query_to_df(conn, query):
    df = pd.read_sql_query(query, conn)
    return df
