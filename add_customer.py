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
       

   


    
        

