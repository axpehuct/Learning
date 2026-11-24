from db import get_connection
from finance import add_record, create_table, get_balance, report_by_category
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    connection = get_connection()
    try:
        balance = get_balance(connection)
    finally:
        connection.close()
    return render_template("index.html", balance=balance)

@app.route("/report")
def report():
    connection = get_connection()
    try:
        balance = get_balance(connection)
        report = report_by_category(connection)
    finally:
        connection.close()
    return render_template("report.html", balance=balance, report=report)

@app.route("/add", methods=["POST"])
def add():
    operation_type = request.form["operation_type"]
    category = request.form["category"]
    amount = float(request.form["amount"])
    connection = get_connection()
    try:
        add_record(connection, operation_type, category, amount)
    finally:
        connection.close()
    return redirect("/")

if __name__ == "__main__":
    connection = get_connection()
    try:
        create_table(get_connection())
    finally:
        connection.close()
    app.run(debug=True)
