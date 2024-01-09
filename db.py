import psycopg2

# Connect to the database
conn = psycopg2.connect(
    database="your_database",
    user="your_user",
    password="your_password",
    host="your_host",
    port="your_port"
)

# Create a cursor
cur = conn.cursor()

# Define the tables and columns
table1 = '3I_theta'
table2 = '3Hshsh_theta'

# Create the view
view_query = f'''
CREATE VIEW combined_view AS
SELECT t1.*, t2.*
FROM "{table1}" t1
FULL OUTER JOIN "{table2}" t2 ON t1.date_column = t2.date_column
ORDER BY COALESCE(t1.date_column, t2.date_column);
'''

# Execute the query
cur.execute(view_query)

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()