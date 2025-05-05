import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import mysql.connector

# Connect to MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Replace with your MySQL password
            database="Record_book"
        )
        return connection
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None

connection = connect_to_database()
cursor = connection.cursor()

# Create the main application window
root = tk.Tk()
root.title("Student Records")

# Label on top
title_label = tk.Label(root, text="Student Record Book", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Create a treeview widget for displaying data
tree = ttk.Treeview(root, columns=("rollno", "first_name", "last_name", "cgpa", "contact", "address"), show="headings")
tree.heading("rollno", text="Roll No")
tree.heading("first_name", text="First Name")
tree.heading("last_name", text="Last Name")
tree.heading("cgpa", text="CGPA")
tree.heading("contact", text="Contact")
tree.heading("address", text="Address")
tree.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Function to show all records from the database
def show_records():
    for record in tree.get_children():
        tree.delete(record)

    try:
        cursor.execute("SELECT * FROM student_record")
        records = cursor.fetchall()
        for record in records:
            tree.insert("", "end", values=record)
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

def show_records_some():
    for record in tree.get_children():
        tree.delete(record)

    try:
        cursor.execute("SELECT * FROM student_record limit 50")
        records = cursor.fetchall()
        for record in records:
            tree.insert("", "end", values=record)
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

# Function to insert a new record
def insert_record():
    try:
        rollno = simpledialog.askstring("Input", "Enter Roll No:")
        first_name = simpledialog.askstring("Input", "Enter First Name:")
        last_name = simpledialog.askstring("Input", "Enter Last Name:")
        cgpa = simpledialog.askstring("Input", "Enter CGPA:")
        contact = simpledialog.askstring("Input", "Enter Contact:")
        address = simpledialog.askstring("Input", "Enter Address:")

        if rollno and first_name:
            cursor.execute(
                "INSERT INTO student_record (rollno, first_name, last_name, cgpa, contact, address) VALUES (%s, %s, %s, %s, %s, %s)",
                (rollno, first_name, last_name, cgpa, contact, address))
            connection.commit()
            messagebox.showinfo("Success", "Record inserted successfully!")
            show_records()
        else:
            messagebox.showwarning("Input Error", "Roll No and First Name are required!")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

# Function to update a selected record
def update_record():
    try:
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a record to update!")
            return

        rollno = tree.item(selected_item)["values"][0]

        first_name = simpledialog.askstring("Input", "Enter New First Name:")
        last_name = simpledialog.askstring("Input", "Enter New Last Name:")
        cgpa = simpledialog.askstring("Input", "Enter New CGPA:")
        contact = simpledialog.askstring("Input", "Enter New Contact:")
        address = simpledialog.askstring("Input", "Enter New Address:")

        update_data = {
            "first_name": first_name,
            "last_name": last_name,
            "cgpa": cgpa,
            "contact": contact,
            "address": address
        }

        set_clause = ", ".join([f"{key} = %s" for key, value in update_data.items() if value])
        values = tuple(value for value in update_data.values() if value)

        if set_clause:
            cursor.execute(f"UPDATE student_record SET {set_clause} WHERE rollno = %s", values + (rollno,))
            connection.commit()
            messagebox.showinfo("Success", "Record updated successfully!")
            show_records()
        else:
            messagebox.showwarning("Update Error", "No new values provided to update!")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

# Function to delete a selected record
def delete_record():
    try:
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a record to delete!")
            return

        rollno = tree.item(selected_item)["values"][0]
        cursor.execute("DELETE FROM student_record WHERE rollno = %s", (rollno,))
        connection.commit()
        messagebox.showinfo("Success", "Record deleted successfully!")
        show_records()
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

# Function to search records by Roll No
def search_record():
    try:
        rollno = simpledialog.askstring("Input", "Enter Roll No to search:")
        if not rollno:
            messagebox.showwarning("Input Error", "Roll No is required to search!")
            return

        cursor.execute("SELECT * FROM student_record WHERE rollno = %s", (rollno,))
        record = cursor.fetchone()
        if record:
            for item in tree.get_children():
                tree.delete(item)
            tree.insert("", "end", values=record)
        else:
            messagebox.showinfo("No Results", "No record found with the given Roll No.")
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

# Create buttons for CRUD operations
insert_button = ttk.Button(root, text="Insert Record", command=insert_record)
insert_button.grid(row=2, column=0, padx=10, pady=10)

update_button = ttk.Button(root, text="Update Record", command=update_record)
update_button.grid(row=2, column=1, padx=10, pady=10)

delete_button = ttk.Button(root, text="Delete Record", command=delete_record)
delete_button.grid(row=2, column=2, padx=10, pady=10)

search_button = ttk.Button(root, text="Search Record", command=search_record)
search_button.grid(row=3, column=1, padx=10, pady=10)

# Button to show all records
show_button = ttk.Button(root, text="Show All Records", command=show_records)
show_button.grid(row=3, column=0, padx=10, pady=10)

show_button = ttk.Button(root, text="Show 10 Records", command=show_records_some)
show_button.grid(row=3, column=2, padx=10, pady=10)

# Start the Tkinter event loop
show_records()
root.mainloop()

# Close the database connection on exit
if connection:
    connection.close()
