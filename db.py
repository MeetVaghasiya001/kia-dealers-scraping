import mysql.connector


def connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Actowiz",
        database="mydb"
    )

    cur = conn.cursor()

    return conn,cur 


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

