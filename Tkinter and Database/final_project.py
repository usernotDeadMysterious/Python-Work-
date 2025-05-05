import tkinter as tk
from tkinter import ttk, messagebox
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['AUP']
collection = db['Record_book']

# Create the main application window
root = tk.Tk()
root.title("Student Records")

# Label on top
title_label = tk.Label(root, text="Student Record Book", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Create a treeview widget for displaying data
tree = ttk.Treeview(root, columns=("rollno", "first_name", "last_Name", "cgpa", "contact", "address"), show="headings")
tree.heading("rollno", text="Roll No")
tree.heading("first_name", text="First Name")
tree.heading("last_Name", text="Last Name")
tree.heading("cgpa", text="CGPA")
tree.heading("contact", text="Contact")
tree.heading("address", text="Address")
tree.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Function to show all records from the database
def show_records():
    for record in tree.get_children():
        tree.delete(record)
    
    try:
        # Retrieve all documents from the collection
        records = collection.find()
        for doc in records:
            tree.insert("", "end", values=(doc.get("rollno", ""), doc.get("first_name", ""),
                                           doc.get("last_Name", ""), doc.get("cgpa", ""),
                                           doc.get("contact", ""), doc.get("address", "")))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to insert a new record
def insert_record():
    try:
        # Prompt user for details
        rollno = tk.simpledialog.askstring("Input", "Enter Roll No:")
        first_name = tk.simpledialog.askstring("Input", "Enter First Name:")
        last_Name = tk.simpledialog.askstring("Input", "Enter Last Name:")
        cgpa = tk.simpledialog.askstring("Input", "Enter CGPA:")
        contact = tk.simpledialog.askstring("Input", "Enter Contact:")
        address = tk.simpledialog.askstring("Input", "Enter Address:")

        # Insert the record into the collection
        if rollno and first_name:
            collection.insert_one({
                "rollno": rollno,
                "first_name": first_name,
                "last_Name": last_Name,
                "cgpa": cgpa,
                "contact": contact,
                "address": address
            })
            messagebox.showinfo("Success", "Record inserted successfully!")
            show_records()
        else:
            messagebox.showwarning("Input Error", "Roll No and First Name are required!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to update a selected record
def update_record():
    try:
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a record to update!")
            return

        # Get the selected record's Roll No
        rollno = tree.item(selected_item)["values"][0]
        if not rollno:
            messagebox.showwarning("Update Error", "Selected record has no Roll No!")
            return

        # Prompt user for new details
        first_name = tk.simpledialog.askstring("Input", "Enter New First Name:")
        last_Name = tk.simpledialog.askstring("Input", "Enter New Last Name:")
        cgpa = tk.simpledialog.askstring("Input", "Enter New CGPA:")
        contact = tk.simpledialog.askstring("Input", "Enter New Contact:")
        address = tk.simpledialog.askstring("Input", "Enter New Address:")

        # Update the record in the collection
        update_data = {"first_name": first_name, "last_Name": last_Name, "cgpa": cgpa, "contact": contact, "address": address}
        collection.update_one({"rollno": rollno}, {"$set": {k: v for k, v in update_data.items() if v}})
        messagebox.showinfo("Success", "Record updated successfully!")
        show_records()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to delete a selected record
def delete_record():
    try:
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a record to delete!")
            return

        rollno = tree.item(selected_item)["values"][0]
        if rollno:
            collection.delete_one({"rollno": rollno})
            messagebox.showinfo("Success", "Record deleted successfully!")
            show_records()
        else:
            messagebox.showwarning("Delete Error", "Selected record has no Roll No!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to search records by Roll No
def search_record():
    try:
        rollno = tk.simpledialog.askstring("Input", "Enter Roll No to search:")
        if not rollno:
            messagebox.showwarning("Input Error", "Roll No is required to search!")
            return

        # Retrieve the record from the collection
        record = collection.find_one({"rollno": rollno})
        if record:
            for item in tree.get_children():
                tree.delete(item)
            tree.insert("", "end", values=(record.get("rollno", ""), record.get("first_name", ""),
                                           record.get("last_Name", ""), record.get("cgpa", ""),
                                           record.get("contact", ""), record.get("address", "")))
        else:
            messagebox.showinfo("No Results", "No record found with the given Roll No.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

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

# Start the Tkinter event loop
show_records()
root.mainloop()
