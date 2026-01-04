import tkinter as tk
from tkinter import messagebox
import json
import os

DATA_FILE = "expenses.json"
BALANCE_FILE = "balance.json"

# ------------------ Data Handling ------------------
def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_expenses():
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def load_balance():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "r") as file:
            return json.load(file).get("hold", 0)
    return 0

def save_balance():
    with open(BALANCE_FILE, "w") as file:
        json.dump({"hold": hold_balance.get()}, file, indent=4)

expenses = load_expenses()

# ------------------ Core Functions ------------------
def set_hold():
    try:
        value = float(hold_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Value", "Hold must be a number.")
        return
    hold_balance.set(value)
    save_balance()
    update_list()
    messagebox.showinfo("Hold Set", f"Hold balance set to ৳ {value}")

def add_expense():
    title = title_entry.get().strip()
    amount = amount_entry.get().strip()
    category = category_entry.get().strip()

    if not title or not amount or not category:
        messagebox.showwarning("Missing Data", "Please fill all fields.")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Invalid Amount", "Amount must be a number.")
        return

    if amount > hold_balance.get():
        messagebox.showwarning("Insufficient Hold", "Not enough balance in hold!")
        return

    expense = {
        "title": title,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    hold_balance.set(hold_balance.get() - amount)
    save_expenses()
    save_balance()
    update_list()
    clear_fields()

def delete_expense():
    selected = expense_list.curselection()
    if not selected:
        messagebox.showwarning("No Selection", "Select an expense to delete.")
        return

    index = selected[0]
    removed = expenses.pop(index)
    hold_balance.set(hold_balance.get() + removed["amount"])
    save_expenses()
    save_balance()
    update_list()

def update_list():
    expense_list.delete(0, tk.END)
    total = 0

    for exp in expenses:
        expense_list.insert(
            tk.END,
            f"{exp['title']} | {exp['category']} | ৳{exp['amount']}"
        )
        total += exp["amount"]

    total_label.config(text=f"Total Expense: ৳ {total}")
    hold_label.config(text=f"Hold Balance: ৳ {hold_balance.get():.2f}")

def clear_fields():
    title_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)

# ------------------ GUI Setup ------------------
window = tk.Tk()
window.title("Smart Expense Buddy 💸")
window.geometry("580x500")
window.configure(bg="#F4F6F7")
window.resizable(False, False)

title = tk.Label(
    window,
    text="Smart Expense Buddy 💸",
    font=("Segoe UI", 18, "bold"),
    bg="#F4F6F7"
)
title.pack(pady=10)

# ------------------ Hold Balance ------------------
hold_frame = tk.Frame(window, bg="#F4F6F7")
hold_frame.pack(pady=5)

tk.Label(hold_frame, text="Set Hold Balance: ৳", bg="#F4F6F7").grid(row=0, column=0)
hold_entry = tk.Entry(hold_frame, width=10)
hold_entry.grid(row=0, column=1, padx=5)

tk.Button(
    hold_frame,
    text="Set Hold",
    command=set_hold,
    bg="#3498DB",
    fg="white",
    width=10
).grid(row=0, column=2, padx=10)

hold_balance = tk.DoubleVar()
hold_balance.set(load_balance())

hold_label = tk.Label(
    window,
    text=f"Hold Balance: ৳ {hold_balance.get():.2f}",
    font=("Segoe UI", 12, "bold"),
    bg="#F4F6F7"
)
hold_label.pack(pady=5)

# ------------------ Input Fields ------------------
frame = tk.Frame(window, bg="#F4F6F7")
frame.pack(pady=5)

tk.Label(frame, text="Title", bg="#F4F6F7").grid(row=0, column=0, padx=5)
title_entry = tk.Entry(frame, width=20)
title_entry.grid(row=0, column=1)

tk.Label(frame, text="Amount", bg="#F4F6F7").grid(row=0, column=2, padx=5)
amount_entry = tk.Entry(frame, width=10)
amount_entry.grid(row=0, column=3)

tk.Label(frame, text="Category", bg="#F4F6F7").grid(row=0, column=4, padx=5)
category_entry = tk.Entry(frame, width=15)
category_entry.grid(row=0, column=5)

# ------------------ Buttons ------------------
btn_frame = tk.Frame(window, bg="#F4F6F7")
btn_frame.pack(pady=10)

tk.Button(
    btn_frame,
    text="Add Expense",
    command=add_expense,
    bg="#2ECC71",
    fg="white",
    width=15
).grid(row=0, column=0, padx=10)

tk.Button(
    btn_frame,
    text="Delete Selected",
    command=delete_expense,
    bg="#E74C3C",
    fg="white",
    width=15
).grid(row=0, column=1, padx=10)

# ------------------ Expense List ------------------
expense_list = tk.Listbox(
    window,
    width=75,
    height=12
)
expense_list.pack(pady=10)

# ------------------ Total ------------------
total_label = tk.Label(
    window,
    text="Total Expense: ৳ 0",
    font=("Segoe UI", 12, "bold"),
    bg="#F4F6F7"
)
total_label.pack(pady=5)

update_list()
window.mainloop()
