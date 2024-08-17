import pymysql

class Users:
    def __init__(self, id, email, password, username):
        self.id = id
        self.email = email
        self.password = password
        self.username = username

    def __str__(self) -> str:
        return f"{self.id} - {self.email} - {self.password} - {self.username}"

def open_connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='Abhi@123',
        db='pymysql'
    )
    return conn

def close_connection(conn):
    conn.close()

# Select query
def get_users():
    conn = open_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    output = cur.fetchall()

    for i in output:
        print("select query output", i)

    close_connection(conn)

def get_user(users_id):
    conn = open_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (users_id,))
    output = cur.fetchall()

    for i in output:
        print("select query output", i)

    close_connection(conn)

def insert_static_value():
    conn = open_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO users (email, password, username) 
        VALUES (%s, %s, %s)
    """, ('test@test.com', 'password', 'test'))
    print(conn.insert_id()) #to retrieve the id of the last inserted element provided by pymysql 
    conn.commit()
    close_connection(conn)

def insert_dynamic_value(users_list):
    conn = open_connection()
    cur = conn.cursor()
    for user in users_list:
        cur.execute("""
            INSERT INTO users (email, password, username) 
            VALUES (%s, %s, %s)
        """, (user.email, user.password, user.username))
    print(conn.insert_id())
    conn.commit()
    close_connection(conn)

def delete_user(users_id):
    conn = open_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = %s", (users_id,))
    conn.commit()
    close_connection(conn)

def update_user(user):
    conn = open_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE users SET email = %s, password = %s, username = %s WHERE id = %s
    """, (user.email, user.password, user.username, user.id))
    conn.commit()
    close_connection(conn)

# Testing the functions

get_users()
get_user('1')

users1 = Users(4, 'abc@test.com', 'passwordd', 'testt')
print("users", users1)
users_list = [users1]
insert_dynamic_value(users_list)
get_user('4')  

update_user_data = Users(3, 'update@gmail.com', 'newpassword', 'newuser')
update_user(update_user_data)
get_user('4')

delete_user('4')
get_users()
