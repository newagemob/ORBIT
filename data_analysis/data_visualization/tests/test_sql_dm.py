from data_visualization import create_connection, create_table, insert_data, select_data, query_to_df

# Connect to a database
conn = create_connection('example.db')

# Create a table
create_table_query = '''CREATE TABLE stocks
                        (date text, trans text, symbol text, qty real, price real)'''
create_table(conn, create_table_query)

# Insert data into the table
insert_data_query = '''INSERT INTO stocks VALUES
                        ('2006-01-05','BUY','RHAT',100,35.14),
                        ('2006-03-28','SELL','IBM',50,109.72),
                        ('2006-04-06','BUY','MSFT',200,22.69),
                        ('2006-05-05','SELL','GOOG',25,201.59)'''
insert_data(conn, insert_data_query)

# Retrieve data from the table
select_data_query = '''SELECT * FROM stocks'''
rows = select_data(conn, select_data_query)
for row in rows:
    print(row)

# Convert the query result to a Pandas DataFrame
df = query_to_df(conn, select_data_query)
print(df)
