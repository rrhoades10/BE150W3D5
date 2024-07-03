from connect_mysql import connect_db
from mysql.connector import Error

def remove_customer():
    
    try:
        conn = connect_db()
        cursor = conn.cursor()

        customer_id = int(input("Which customer(id) would you like to remove? "))

        customer_to_remove = (customer_id,)
        query_check = "SELECT * FROM Orders WHERE customer_id = %s"
        cursor.execute(query_check, customer_to_remove)
        orders = cursor.fetchall()
        # checking if customer has associated orders
        if orders:
            print("Cannot remove customer that has assoicated orders.")
        else:
        # SQL Query
            query = "DELETE FROM Customers WHERE customer_id = %s"

            # executing the query
            cursor.execute(query, (customer_id, ))
            conn.commit()
            print("Customer Removed Successfully")
    
    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close() #turns off the cursor
            conn.close() #turns of the connection to the db

remove_customer()