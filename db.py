import mysql.connector


# it it use to create db connection
def connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Actowiz",
        database="mydb"
    )

    cur = conn.cursor()

    return conn,cur 

# it create databse table 
def create_db():
    conn,cur = connection()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS kia(
                s_id INT AUTO_INCREMENT PRIMARY KEY,
                state_name VARCHAR(255),
                store_id VARCHAR(255),
                store_name VARCHAR(255),
                url TEXT,
                full_address TEXT,
                phone1 VARCHAR(255),
                phone2 VARCHAR(255),
                dealer_type VARCHAR(255)
            )

    """)

    conn.commit()
    conn.close()


# it insert 100 rows at the time
def insert_data(data):
    query = """INSERT INTO kia(state_name,store_id,store_name,url,full_address,phone1,phone2,dealer_type) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
    conn,cur = connection()

    cur.executemany(query,data)
    print(f'100 row was add!')
    conn.commit()
    conn.close()

