import sqlite3
from datetime import date

def start(connection):
    clear_table(connection)
    create_table(connection)
    add_record(connection, "expense", "car", 1200)
    add_record(connection, "expense", "food", 200)
    add_record(connection, "income", "work", 10000)
    add_record(connection, "expense", "food", 300)
    add_record(connection, "expense", "entertainment", 3000)
    add_record(connection, "; DROP TABLE records;--", "entertainment ", 3000)
    print(f"Ваш баланс: {get_balance(connection)}")
    report_by_category(connection)

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            type TEXT NOT NULL,
            category TEXT,
            amount REAL NOT NULL
        )
    """)
def add_record(connection, operation_type, category, amount):
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO records (date, type, category, amount) VALUES (?, ?, ?, ?)""",
      (date.today().isoformat(), operation_type, category, amount))
    connection.commit()

def get_balance(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT 
            COALESCE(SUM(CASE WHEN type = 'income' THEN amount else 0 END), 0) - 
            COALESCE(SUM(CASE WHEN type = 'expense' THEN amount else 0 END), 0) as total_balance
          FROM records
    """)
    return cursor.fetchone()[0]    

def report_by_category(connection):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT category, SUM(amount) FROM records WHERE type = 'expense' GROUP BY category
    """)
    for cat in cursor.fetchall():
        print(f"{cat[0]}: {cat[1]} руб.")

def clear_table(connection):
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM records """)
    connection.commit()

def create_connection():
    connection = sqlite3.connect("finance.db")
    return connection

def close_connection(connection):
    connection.close()

if __name__ == "__main__":
    connection = create_connection()
    start(connection)
    close_connection(connection)