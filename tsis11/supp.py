import psycopg2
import csv

def connect():
    conn = None
    #You can choose insert|update|delete|check
    print("insert|update|delete|check or func")
    choose = input()
    if choose == "insert":
        print("type your first name")
        first_name = input()
        print("type your last name")
        last_name = input()
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
    if choose == "func":
        print("Enter number from 1 to 5")
        #1.Function that returns all records based on a pattern (example of pattern: part of name, surname, phone number)
        #2.Create procedure to insert new user by name and phone, update phone if user already exists
        #3.Create procedure to insert many new users by list of name and phone. Use loop and if statement in stored procedure. Check correctness of phone in procedure and return all incorrect data.
        #4.Create function to querying data from the tables with pagination (by limit and offset)
        #5.Implement procedure to deleting data from tables by username or phone
        choose = input()
        if choose == "2":
            print("type your first name")
            first_name = input()
            print("type your last name")
            last_name = input()
            print("type your phone")
            phone = input()

        ls = ['afdfa','afdad','99232'],['afdvv','asdfsd','9213'],['asfdfa','cafdfacaa','813981238'],['adjsf','asdf','88adfs']

        if choose == "4":
            print('Limit: ')
            lim = input()
            print('offset: ')
            offset = input()
        
        if choose == "5":
            print("type your first name")
            first_name = input()
            print("type your last name")
            last_name = input()
            print("type your phone")
            phone = input()

    try:
        conn = psycopg2.connect(host="localhost", database="suppliers", user="postgres", password="1234")

        conn.autocommit = True

        with conn.cursor() as cursor:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            phone VARCHAR(255) UNIQUE NOT NULL
            )""")

        with conn.cursor() as cursor:
            cursor.execute("""COPY phonebook
            FROM 'C:\\Users\\Bekarys\\Desktop\\work\\hello\\tsis10\\book.csv'
            DELIMITER ',' CSV HEADER;""")


        if choose == "insert":
            with conn.cursor() as cursor:
                cursor.execute(f"""INSERT INTO phonebook
                (first_name, last_name, phone) VALUES('{first_name}','{last_name}','{phone}')
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

        if choose == "1":
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM phonebook ORDER BY first_name")
                row = cursor.fetchone()

                while row is not None:
                    print(row)
                    row = cursor.fetchone()
        
        if choose == "2":
            with conn.cursor() as cursor:
                cursor.execute("SELECT phone FROM phonebook WHERE first_name = '{}'".format(first_name))
                row = cursor.fetchone()
                if row == None:
                    cursor.execute(f"""INSERT INTO phonebook
                    (first_name, last_name, phone) VALUES('{first_name}','{last_name}','{phone}')""")
                else:
                    cursor.execute("""UPDATE phonebook SET phone = %s WHERE first_name = %s; """, (phone,first_name))
        
        if choose == "3":
            with conn.cursor() as cursor:
                for x in ls:
                    temp = x[2].isdigit()
                    if temp:
                        cursor.execute("""INSERT INTO phonebook
                        (first_name, last_name, phone) VALUES('{}','{}','{}')""".format(x[0],x[1],x[2]))
                    else:
                        print(x[2],"is incorrect")

        if choose == "4":
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM phonebook ORDER BY first_name LIMIT {} OFFSET {}  ".format(lim, offset))
                row = cursor.fetchone()

                while row is not None:
                    print(row)
                    row = cursor.fetchone()

        
        if choose == "5":
            with conn.cursor() as cursor:
                cursor.execute("SELECT phone FROM phonebook WHERE first_name = '{}' or phone = '{}'".format(first_name, phone))
                row = cursor.fetchone()
                if row != None:
                    cursor.execute("DELETE FROM phonebook WHERE first_name = '{}'".format(first_name))
                    cursor.execute("DELETE FROM phonebook WHERE phone = '{}'".format(phone))
            

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error")
    finally:
        if conn is not None:
            print("done")


connect()