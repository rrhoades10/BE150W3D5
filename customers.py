from connect_mysql import connect_db
from mysql.connector import Error

# a couple different ways to add things to your database with a function
# have the function take in parameters - add those parameters to the databse

# or

# we can use the input() to collect user input within the function and apply that information
# to the database

def add_customer():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # collect customer information to add to the database
        name = input("Please enter the customer's name: ")
        email = input("Please enter the customer's email: ")
        phone = input("Please enter the customer's phone number" )

        # creating the tuple that we will send over to the database
        # we set this to a tuple becuase the execute query method needs an iterable to match the position of values
        new_customer = (name, email, phone)

        # SQL Query to insert customer information                  place holders for the data to be inserted
        query = "INSERT INTO Customers (name, email, phone) VALUES (%s, %s, %s)"

        # excecute the query
        cursor.execute(query, new_customer) #prepares query with arguments
        conn.commit() #commits and sends changes to our database
        print(f"{name} has successfully been added to the database!")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if conn and conn.is_connected():
            cursor.close()
            conn.close() 


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

def add_customer2():  

        # collect customer information to add to the database
        name = input("Please enter the customer's name: ")
        email = input("Please enter the customer's email: ")
        phone = input("Please enter the customer's phone number" )

        # creating the tuple that we will send over to the database
        # we set this to a tuple becuase the execute query method needs an iterable to match the position of values
        new_customer = (name, email, phone)

        # SQL Query to insert customer information                  place holders for the data to be inserted
        query = "INSERT INTO Customers (name, email, phone) VALUES (%s, %s, %s)"

        # excecute the query

        return query, new_customer


def add_customer3(conn): 
        
        cursor = conn.cursor()

        # collect customer information to add to the database
        name = input("Please enter the customer's name: ")
        email = input("Please enter the customer's email: ")
        phone = input("Please enter the customer's phone number" )

        # creating the tuple that we will send over to the database
        # we set this to a tuple becuase the execute query method needs an iterable to match the position of values
        new_customer = (name, email, phone)

        # SQL Query to insert customer information                  place holders for the data to be inserted
        query = "INSERT INTO Customers (name, email, phone) VALUES (%s, %s, %s)"

        # excecute the query
        cursor.execute(query, new_customer)
        conn.commit()
        print("Successfully added user")
        cursor.close()

        