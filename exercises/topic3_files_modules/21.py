from datetime import datetime

def days_until(date_str):
    return (datetime.strptime(date_str, "%Y-%m-%d") - datetime.today()).days

print(days_until("2026-12-31"))
print(days_until("2026-10-14"))
print(days_until("2026-01-01"))
print(days_until("2027-01-01"))