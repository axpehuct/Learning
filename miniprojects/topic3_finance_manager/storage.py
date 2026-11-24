import json
from datetime import datetime

import os

filename = "finances.json"
directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(directory, filename)

def read_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Введено не число, попробуйте еще раз")

def add_record(records, operation_type, category, amount):
    data = {}
    data["date"] = datetime.now().strftime("%Y-%m-%d")
    data["type"] = operation_type
    data["category"] = category
    data["amount"] = amount
    records.append(data)
    save_JSON(file_path, records)

def report_by_category(data):
    report = {}
    for record in data:
        if record["type"] == "expense":
            category  = record.get("category")
            report[category] = report.get(category, 0) + record["amount"]
    return report

def get_balance(records):
    expense = sum(rec["amount"] for rec in records if rec["type"] == "expense")
    income = sum(rec["amount"] for rec in records if rec["type"] == "income")
    return income - expense
    
def save_JSON(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_JSON():
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print("Файл не найден.")
            return []
            

if __name__ == "__main__":
    JSON_data = load_JSON(file_path)
    add_record(JSON_data, "expense", "food", 100)
    add_record(JSON_data, "income", "food", 900)
    add_record(JSON_data, "expense", "food", 900)
    print(report_by_category(JSON_data))
    print(get_balance(JSON_data))