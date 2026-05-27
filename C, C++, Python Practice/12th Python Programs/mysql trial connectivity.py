import mysql.connector
from mysql.connector import Error

try:
    # Establish the connection
    with mysql.connector.connect(
        user='myuser',
        password='mypassword',
        host='user-PC',
        database='student'
    ) as cnx:

        if cnx.is_connected():
            print("Successfully connected to the database")

        with cnx.cursor() as cursor:
            # Execute the query
            cursor.execute("SELECT * FROM student18")
            results = cursor.fetchall()

            # Print the results
            for row in results:
                print(row)

except Error as e:
    print(f"Error: {e}")
