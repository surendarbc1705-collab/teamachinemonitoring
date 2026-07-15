import sqlite3

DATABASE_NAME = "tea_machine.db"


def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS machine_logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        machine_status TEXT,
        blade_status TEXT,
        machine_on_time TEXT,
        machine_off_time TEXT,
        running_time TEXT,
        wifi_status TEXT,
        last_sync TEXT
    )
    """)

    conn.commit()
    conn.close()


def create_default_user():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=?",
        ("admin",)
    )

    user = cursor.fetchone()

    if user is None:
        cursor.execute(
            "INSERT OR IGNORE INTO users(username,password) VALUES(?,?)",
            ("Croft", "Admin@123")
        )

        conn.commit()

    conn.close()


def check_login(username, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()

    conn.close()

    return user


create_database()
create_default_user()