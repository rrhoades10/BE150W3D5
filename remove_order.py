from connect_mysql import connect_db
from mysql.connector import Error

def remove_order():    
    try:
        conn = connect_db()
        cursor = conn.cursor()

        order_id = int(input("Which order(id) would you like to remove? "))

        # query to delete order by id
        query= "DELETE FROM Orders where order_id = %s"

        # executing the query
        cursor.execute(query, (order_id,))
        conn.commit()
        print("Your order was succesfully cancelled. ")
    
    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close() #turns off the cursor
            conn.close()

remove_order()

    