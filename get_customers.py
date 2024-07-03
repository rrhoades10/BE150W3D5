from connect_mysql import connect_db
from mysql.connector import Error

def get_customers():
    
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # create a SQL query as a python string
        query = "SELECT * FROM Customers"

        # Executing the query using the cursor
        cursor.execute(query)

        # fetching the results from the above query
        # print(cursor.fetchall())
        # loops through the results and prints each row of data
        # is returned as an tuple
        for row in cursor.fetchall():#fetchall returns data from the query execution as a list of tuples
            # looping through the list of tuples
            print(row) #printing each row as a tuple
    
    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close() #turns off the cursor
            conn.close() #turns of the connection to the db

get_customers()


        
