from connect_mysql import connect_db
from mysql.connector import Error

def update_order():    
    try:
        conn = connect_db()
        cursor = conn.cursor()

        order_id = int(input("Please enter the order(id) to update: "))
        date = input("Please enter the update order date: ")

        # query for updating
        query = "UPDATE Orders SET date = %s WHERE order_id = %s"

        cursor.execute(query, (date, order_id))
        conn.commit()

        print("Order successfully updated!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close() #turns off the cursor
            conn.close()
update_order()
