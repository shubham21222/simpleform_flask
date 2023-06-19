import pymysql

# Connect to the database
conn = pymysql.connect(
    host='localhost',
    user='username',
    password='password',
    database='techritzy'
)

# Create a cursor object
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM student2")

# Fetch the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()