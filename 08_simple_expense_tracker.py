import csv
import time
import os

def load_expenses():
    if not os.path.exists("expense_tracer.csv"):
        return

    with open("expense_tracer.csv", "r", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row["expense"] = int(row["expense"])  # convert string to int
            data.append(row)

data = []
load_expenses()

def menu():
    print("-"*20+" Personal Expense Tracker "+"-"*20)
    print("\n")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. Search by Category or Date")
    print("4. Total spent")

def add_expense():
    print("Add expense: ")
    category = input("Category: ")
    expense = int(input("Amount: "))
    before_in = {"category": category, "expense":expense}
    global data
    data.append(before_in)

    with open('expense_tracer.txt', 'a', newline='') as csvfile:
        field_names = ['category','expense']
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)

print(data)
add_expense()