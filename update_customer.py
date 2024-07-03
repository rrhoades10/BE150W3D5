from connect_mysql import connect_db
from mysql.connector import Error


def update_customer():

    # example for some SPICY updates
    # response = input("What would you like to update")

    # if response == "email":
    #     # code to update email
    #     pass

    # elif response == "phone":
    #     # code to update phone
    #     pass
    # elif response == "name":
    #     # code to update name
    #     pass

    try:
        conn = connect_db()
        cursor = conn.cursor()

        customer_id = int(input("Which customer (id) would you like to update the phone number of?"))
        phone = input("Please enter the new phone number")

        # updated customer information
        updated_customer = (phone, customer_id)

        # SQL Query to update customer information
        query = "UPDATE Customers SET phone = %s WHERE customer_id = %s"

        # executing the query
        cursor.execute(query, updated_customer)
        conn.commit()
        print("Customer details successfully updated! ")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close() #turns off the cursor
            conn.close() #turns of the connection to the db


update_customer()




