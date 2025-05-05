import tkinter as tk
from tkinter import ttk, messagebox
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['AUP']
collection = db['Record_book']

# Create the main application window
root = tk.Tk()
root.title("Student Record Book")

# Add a label at the top
label = tk.Label(root, text="Student Record Book", font=("Helvetica", 16))
label.grid(row=0, column=0, columnspan=3, pady=10)

# Create a treeview widget for displaying data
tree = ttk.Treeview(root, columns=("rollno", "first_Name", "last_name", "cgpa", "contact", "address"), show="headings")
tree.heading("rollno", text="Roll No")
tree.heading("first_Name", text="First Name")
tree.heading("last_name", text="Last Name")
tree.heading("cgpa", text="CGPA")
tree.heading("contact", text="Contact")
tree.heading("address", text="Address")
tree.grid(row=1, column=0, columnspan=3)

# Function to show all records from the database
def show_records():
    for record in tree.get_children():
        tree.delete(record)
    
    try:
        # Retrieve all documents from the collection
        records = collection.find()
        for doc in records:
            tree.insert("", "end", values=(doc.get("rollno", ""), doc.get("first_Name", ""),
                                              doc.get("last_name", ""), doc.get("cgpa", ""),
                                              doc.get("contact", ""), doc.get("address", "")))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to open a new window for record insertion
def open_insert_window():
    insert_window = tk.Toplevel(root)
    insert_window.title("Insert Record")

    rollno_var = tk.StringVar()
    first_Name_var = tk.StringVar()
    last_name_var = tk.StringVar()
    cgpa_var = tk.StringVar()
    contact_var = tk.StringVar()
    address_var = tk.StringVar()

    fields = [
        ("Roll No", rollno_var),
        ("First Name", first_Name_var),
        ("Last Name", last_name_var),
        ("CGPA", cgpa_var),
        ("Contact", contact_var),
        ("Address", address_var)
    ]

    for idx, (label_text, var) in enumerate(fields):
        tk.Label(insert_window, text=label_text).grid(row=idx, column=0, sticky="w")
        tk.Entry(insert_window, textvariable=var).grid(row=idx, column=1, sticky="w")

    def insert_record():
        try:
            doc = {
                "rollno": rollno_var.get(),
                "first_Name": first_Name_var.get(),
                "last_name": last_name_var.get(),
                "cgpa": cgpa_var.get(),
                "contact": contact_var.get(),
                "address": address_var.get()
            }
            collection.insert_one(doc)
            messagebox.showinfo("Success", "Record inserted successfully.")
            insert_window.destroy()
            show_records()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    ttk.Button(insert_window, text="Insert", command=insert_record).grid(row=len(fields), column=0, columnspan=2, pady=10)

# Function to delete a document
def delete_record():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "No record selected.")
        return

    try:
        values = tree.item(selected_item, "values")
        collection.delete_one({"rollno": values[0]})
        messagebox.showinfo("Success", "Record deleted successfully.")
        show_records()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to update a document
def update_record():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "No record selected.")
        return

    try:
        values = tree.item(selected_item, "values")
        collection.update_one(
            {"rollno": values[0]},
            {"$set": {
                "first_Name": values[1],
                "last_name": values[2],
                "cgpa": values[3],
                "contact": values[4],
                "address": values[5]
            }}
        )
        messagebox.showinfo("Success", "Record updated successfully.")
        show_records()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to search for a document
def search_record():
    for record in tree.get_children():
        tree.delete(record)

    try:
        query = {"rollno": rollno_var.get()}
        records = collection.find(query)
        for doc in records:
            tree.insert("", "end", values=(doc.get("rollno", ""), doc.get("first_Name", ""),
                                              doc.get("last_name", ""), doc.get("cgpa", ""),
                                              doc.get("contact", ""), doc.get("address", "")))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Buttons for CRUD operations
buttons = [
    ("Show All Records", show_records),
    ("Insert Record", open_insert_window),
    ("Delete Record", delete_record),
    ("Update Record", update_record)
]

for idx, (btn_text, command) in enumerate(buttons):
    ttk.Button(root, text=btn_text, command=command).grid(row=8, column=idx, pady=10)

# Start the Tkinter event loop
root.mainloop()
