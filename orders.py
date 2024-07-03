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
            conn.close()


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