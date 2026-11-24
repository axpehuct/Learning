from datetime import date


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
    return cursor.fetchall()

def clear_table(connection):
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM records """)
    connection.commit()


def close_connection(connection):
    connection.close()