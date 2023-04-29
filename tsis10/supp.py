import psycopg2
import csv

def connect():
    conn = None
    #You can choose insert|update|delete|check
    print("insert|update|delete|check")
    choose = input()
    if choose == "insert":
        print("type your first name")
        first_name = input()
        print("type your second name")
        second_name = input()
        print("type your phone")
        phone = input()
    if choose == "update":
        print("old phone num")
        ph_old = input()
        print("new phone num")
        ph_new = input()
    if choose == "delete":
        print("number of phone you want to delete")
        dl = input()

    try:
        conn = psycopg2.connect(host="localhost", database="suppliers", user="postgres", password="1234")

        conn.autocommit = True

        with conn.cursor() as cursor:
            cursor.execute("SELECT version()")
            version = cursor.fetchone()
            print(version)

        with conn.cursor() as cursor:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            phone VARCHAR(11) UNIQUE NOT NULL
            )""")

        with conn.cursor() as cursor:
            cursor.execute("""COPY phonebook
            FROM 'C:\\Users\\Bekarys\\Desktop\\work\\hello\\tsis10\\book.csv'
            DELIMITER ',' CSV HEADER;""")


        if choose == "insert":
            with conn.cursor() as cursor:
                cursor.execute(f"""INSERT INTO phonebook
                (first_name, last_name, phone) VALUES('{first_name}','{second_name}','{phone}')
                """)
        
        if choose == "update":
            with conn.cursor() as cursor:
                cursor.execute("""UPDATE phonebook SET phone = %s WHERE phone = %s; 
                """, (ph_new,ph_old))

            updated_rows = cursor.rowcount
            conn.commit()

        if choose == "check":
            with conn.cursor() as cursor:
                cursor.execute("""
                SELECT first_name, last_name FROM phonebook ORDER BY phone
                """)
                row = cursor.fetchone()
                
                while row is not None:
                    print(row)
                    row = cursor.fetchone()

        if choose == "delete":
            with conn.cursor() as cursor:
                cursor.execute("""
                DELETE FROM phonebook WHERE phone = %s
                """, (dl,))
            

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error")
    finally:
        if conn is not None:
            print("done")


connect()