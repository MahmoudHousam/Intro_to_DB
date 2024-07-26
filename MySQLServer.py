import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# load_dotenv()


def create_connection(host_name, username, password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name, user=username, password=password
        )
        print("Successful connection to MySQL server")
    except mysql.connector.Error as e:
        print(f"Error occurred: {e}")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
        connection.commit()
        connection.close()
        print("New changes committed and connection closed")
    except Exception as e:
        print(f"Error occurred: {e}")
    return cursor


if __name__ == "__main__":
    host = "localhost"
    user = "root"
    password = os.getenv("mysql_password")

    connection = create_connection(host_name=host, username=user, password=password)
    create_database_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"
    execute_query(connection=connection, query=create_database_query)

    create_table_query = """
    CREATE TABLE IF NOT EXISTS Books (
    book_id INT PRIMARY KEY,
    title NOT NULL VARCHAR(130),
    author_id INT NOT NULL,
    price,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
    );

    -- create Authors table
    CREATE TABLE IF NOT EXISTS Authors (
        author_id INT PRIMARY KEY,
        author_name VARCHAR(215),
    );

    -- create Customers table
    CREATE TABLE IF NOT EXISTS Customers (
        customer_id INT PRIMARY KEY,
        customer_name VARCHAR(215),
        email VARCHAR(215),
        address TEXT
    );

    -- create Orders table
    CREATE TABLE IF NOT EXISTS Orders (
        order_id INT PRIMARY KEY,
        customer_id INT NOT NULL VARCHAR(215),
        order_date DATE,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    );

    -- create Order_Details table
    CREATE TABLE IF NOT EXISTS Order_Details (
        order_id INT PRIMARY KEY,
        book_id INT NOT NULL VARCHAR(215),
        quantity DOUBLE,
        FOREIGN KEY (order_id) REFERENCES Orders(order_id),
        FOREIGN KEY (book_id) REFERENCES Books(book_id),
    );
    """
    execute_query(connection=connection, query=create_table_query)
