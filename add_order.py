from connect_mysql import connect_db
from mysql.connector import Error

def add_order():    
    try:
        conn = connect_db()
        cursor = conn.cursor()

        customer_id = int(input("Please enter the customer(id) who made the order: "))
        date = input("Please enter the order date: ")

        new_order = (customer_id, date)

        # query to insert order
        query = "INSERT INTO Orders(customer_id, date) Values(%s, %s)"

        # executing query and committing changes
        cursor.execute(query, new_order)
        conn.commit()
        print("Order added successfully")
    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close() #turns off the cursor
            conn.close() #turns of the connection to the db

add_order()

