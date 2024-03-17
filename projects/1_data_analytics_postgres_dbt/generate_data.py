import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="dbt",
    user="postgres",
    password="postgres"
)

# Create a cursor object to interact with the database
cur = conn.cursor()

# Set the search path to the "source" schema
cur.execute("SET search_path TO source")

# Create the Customer table
cur.execute("""
    CREATE TABLE IF NOT EXISTS customer (
        customer_id INTEGER PRIMARY KEY,
        customer_name VARCHAR(255),
        customer_email VARCHAR(255)
    )
""")

# Create the Product table
cur.execute("""
    CREATE TABLE IF NOT EXISTS product (
        product_id INTEGER PRIMARY KEY,
        product_name VARCHAR(255),
        price NUMERIC
    )
""")

# Create the Order table
cur.execute("""
    CREATE TABLE IF NOT EXISTS order_table (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        product_id INTEGER,
        order_date DATE,
        total_amount NUMERIC,
        FOREIGN KEY (customer_id) REFERENCES customer (customer_id),
        FOREIGN KEY (product_id) REFERENCES product (product_id)
    )
""")

# Create the Payment table
cur.execute("""
    CREATE TABLE IF NOT EXISTS payment (
        payment_id INTEGER PRIMARY KEY,
        order_id INTEGER,
        payment_date DATE,
        payment_amount NUMERIC,
        FOREIGN KEY (order_id) REFERENCES order_table (order_id)
    )
""")

# Define the data to be inserted into the Customer table
customer_data = [
    (1, 'John Doe', 'johndoe@example.com'),
    (2, 'Jane Smith', 'janesmith@example.com'),
    (3, 'David Johnson', 'davidjohnson@example.com')
]

# Define the data to be inserted into the Order table
order_data = [
    (101, 1, 301, '2024-01-15', 150.50),
    (102, 2, 302, '2024-02-01', 75.20),
    (103, 3, 303, '2024-02-10', 200.00),
    (104, 1, 302, '2024-03-05', 100.00)
]

# Define the data to be inserted into the Payment table
payment_data = [
    (201, 101, '2024-01-16', 150.50),
    (202, 102, '2024-02-02', 75.20),
    (203, 103, '2024-02-11', 200.00),
    (204, 104, '2024-03-06', 100.00)
]

# Define the data to be inserted into the Product table
product_data = [
    (301, 'Laptop', 800),
    (302, 'Smartphone', 500),
    (303, 'Headphones', 100)
]

try:
    # Insert data into the Product table
    cur.executemany("INSERT INTO product (product_id, product_name, price) VALUES (%s, %s, %s)", product_data)
    
    # Insert data into the Customer table
    cur.executemany("INSERT INTO customer (customer_id, customer_name, customer_email) VALUES (%s, %s, %s)", customer_data)

    # Insert data into the Order table
    cur.executemany("INSERT INTO order_table (order_id, customer_id, product_id, order_date, total_amount) VALUES (%s, %s, %s, %s, %s)", order_data)

    # Insert data into the Payment table
    cur.executemany("INSERT INTO payment (payment_id, order_id, payment_date, payment_amount) VALUES (%s, %s, %s, %s)", payment_data)

    # Commit the changes to the database
    conn.commit()

    print("Data inserted successfully!")

except (Exception, psycopg2.DatabaseError) as error:
    print("Error inserting data:", error)

finally:
    # Close the cursor and connection
    if cur:
        cur.close()
    if conn:
        conn.close()