from connect_mysql import connect_db
from mysql.connector import Error

def get_order_info():
    
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Beefy Sql Query
        query = """SELECT order_id, date, Customers.customer_id, name, email
                    FROM Customers, Orders
                    WHERE Customers.customer_id = Orders.customer_id
           """
        
        # execute our query
        cursor.execute(query)

        # looping through results
        for order in cursor.fetchall():
            print(order)

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close() #turns off the cursor
            conn.close() #turns of the connection to the db

get_order_info()