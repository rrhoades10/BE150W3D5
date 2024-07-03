# lastrowid -grabs the id from the last created item in our db
from customers import add_customer, update_customer, remove_customer, get_customers, add_customer2, add_customer3
from orders import add_order, update_order, remove_order, get_order_info
from connect_mysql import connect_db
from mysql.connector import Error


# driver code specifically for customer operations - calling the customer functions
# adding conn as a parameter to the functions and then executing the queries within the functions
def customer_operations():
    try:
        conn = connect_db()
        # cursor = conn.cursor()

        while True:
            response = input("""
    What would you like to do?
        1. Add Customer
        2. View Customers
        3. Update Customer Phone 
        4. Remove Customer
        5. Quit

    """) #the update option for your book functionality only needs to update the availability
            if response == "1":
                # unpack the tuple returned from add_customer2
                # use the above connection to execute and commit the query                 
                # query, new_customer = add_customer2()
                # cursor.execute(query, new_customer)
                # conn.commit()
                # print("Added new customer")

                # using the conn as a parameter in the function and committing the data through the function
                add_customer3(conn)
                
            elif response == "2":
                get_customers()
            elif response == "3":
                update_customer()
            elif response == "4":
                remove_customer()
            elif response == "5":
                print("terminating customer operations...")
                break
            else:
                print("Please enter a valid response...")
    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            # cursor.close() #turns off the cursor
            conn.close() #turns of the connection to the db

# driver code specifically for order operations - calling the order functions
def order_operations():
    while True:
        response = input("""
What would you like to do?
    1. Add Order
    2. View Orders
    3. Update Order Date
    4. Remove Order
    5. Quit

""")
        if response == "1":
            add_order()
        elif response == "2":
            get_order_info()
        elif response == "3":
            update_order()
        elif response == "4":
            remove_order()
        elif response == "5":
            print("terminating order operations...")
            break
        else:
            print("Please enter a valid response...")



def main():

    while True:
        response = input("1 - Customer Operations \n2 - Order Operations \n3. Quit\n")
        if response == "1":
            customer_operations()
        elif response == "2":
            order_operations()
        elif response == "3":
            print("Thanks for comin!")
            break

if __name__ == "__main__":
    main()

