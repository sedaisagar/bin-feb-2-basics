# 
import psycopg2

DB_NAME = "ok_test"
DB_USER = "postgres"
DB_PASS = "root"
DB_HOST = "localhost"
DB_PORT = "5432"

try:
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    print("Database connected successfully")
except:
    print("Database not connected successfully")


cursor = conn.cursor()

# try:
#     cursor.execute("""
#     DROP TABLE IF EXISTS Employee; -- Drops the existing table
#     CREATE TABLE if not exists Employee -- Creates new one
#     (
#         ID INT PRIMARY KEY NOT NULL,
#         NAME TEXT NOT NULL,
#         EMAIL TEXT NOT NULL
#     );
#     """)
#     # commit the changes
#     conn.commit()
#     print("Table Created successfully")
# except Exception as e:
#     print(f"Exception caused in table creation {e}")
#     # rollback to initial state
#     conn.rollback()
#     print("Table Not Created")


# try:
#     cursor.execute("""
#         INSERT INTO Employee (id, name, email) values (2, 'Sagar PandeyX', 'sagar@pandeyx.com');
#         INSERT INTO Employee (id, name, email) values (3, 'Sagar PandeyY', 'sagar@pandeyy.com');
#     """)
#     conn.commit()
# except Exception as e:
#     print(f"Exception caused in insertion {e}")

#     conn.rollback()

cursor.execute("SELECT * FROM Employee")
rows = cursor.fetchall()
for data in rows:
    # print("-"*50)
    print("ID :" + str(data[0]))
    print("NAME :" + data[1])
    print("EMAIL :" + data[2])
    print("-"*50)


print('Data fetched successfully')


# conn.close()