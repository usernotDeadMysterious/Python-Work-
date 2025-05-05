import tkinter as tk
from tkinter import ttk
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  port="3306",
  database = "student_records"
)



# Sample data for student records
student_records = [
    {"Rollno": 1, "Name": "Alice", "Father Name": "John", "CGPA": 3.9, "Contact": "1234567890", "Address": "123 Main St"},
    {"Rollno": 2, "Name": "Bob", "Father Name": "Michael", "CGPA": 3.7, "Contact": "1234567891", "Address": "456 Elm St"},
    {"Rollno": 3, "Name": "Charlie", "Father Name": "David", "CGPA": 3.5, "Contact": "1234567892", "Address": "789 Pine St"},
    {"Rollno": 4, "Name": "David", "Father Name": "Thomas", "CGPA": 3.8, "Contact": "1234567893", "Address": "321 Oak St"},
    {"Rollno": 5, "Name": "Eve", "Father Name": "Richard", "CGPA": 3.6, "Contact": "1234567894", "Address": "654 Cedar St"},
    {"Rollno": 6, "Name": "Frank", "Father Name": "Joseph", "CGPA": 3.4, "Contact": "1234567895", "Address": "987 Birch St"},
    {"Rollno": 7, "Name": "Grace", "Father Name": "Charles", "CGPA": 3.9, "Contact": "1234567896", "Address": "159 Maple St"},
    {"Rollno": 8, "Name": "Hank", "Father Name": "George", "CGPA": 3.8, "Contact": "1234567897", "Address": "753 Walnut St"},
    {"Rollno": 9, "Name": "Ivy", "Father Name": "Edward", "CGPA": 3.7, "Contact": "1234567898", "Address": "951 Spruce St"},
    {"Rollno": 10, "Name": "Jack", "Father Name": "Henry", "CGPA": 4.0, "Contact": "1234567899", "Address": "357 Willow St"},
]

# Function to create the GUI
def create_student_records_gui():
    def add_record():
        # Function to open input window and add a new record
        def save_record():
            new_record = {
                "Rollno": len(student_records) + 1,
                "Name": name_var.get(),
                "Father Name": father_name_var.get(),
                "CGPA": float(cgpa_var.get()),
                "Contact": contact_var.get(),
                "Address": address_var.get(),
            }
            student_records.append(new_record)
            tree.insert("", tk.END, values=(
                new_record["Rollno"],
                new_record["Name"],
                new_record["Father Name"],
                new_record["CGPA"],
                new_record["Contact"],
                new_record["Address"],
            ))
            input_window.destroy()

        # Create a new window for input
        input_window = tk.Toplevel(root)
        input_window.title("Add New Record")

        # Input fields
        tk.Label(input_window, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        name_var = tk.StringVar()
        tk.Entry(input_window, textvariable=name_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(input_window, text="Father Name:").grid(row=1, column=0, padx=10, pady=5)
        father_name_var = tk.StringVar()
        tk.Entry(input_window, textvariable=father_name_var).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(input_window, text="CGPA:").grid(row=2, column=0, padx=10, pady=5)
        cgpa_var = tk.StringVar()
        tk.Entry(input_window, textvariable=cgpa_var).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(input_window, text="Contact:").grid(row=3, column=0, padx=10, pady=5)
        contact_var = tk.StringVar()
        tk.Entry(input_window, textvariable=contact_var).grid(row=3, column=1, padx=10, pady=5)

        tk.Label(input_window, text="Address:").grid(row=4, column=0, padx=10, pady=5)
        address_var = tk.StringVar()
        tk.Entry(input_window, textvariable=address_var).grid(row=4, column=1, padx=10, pady=5)

        tk.Button(input_window, text="Save", command=save_record).grid(row=5, column=0, columnspan=2, pady=10)

    def add_multiple_records():
        def save_multiple():
            try:
                count = int(record_count_var.get())
                multiple_window.destroy()
                for _ in range(count):
                    add_record()
            except ValueError:
                tk.messagebox.showerror("Invalid Input", "Please enter a valid number.")

        multiple_window = tk.Toplevel(root)
        multiple_window.title("Add Multiple Records")

        tk.Label(multiple_window, text="How many records to add?").grid(row=0, column=0, padx=10, pady=5)
        record_count_var = tk.StringVar()
        tk.Entry(multiple_window, textvariable=record_count_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Button(multiple_window, text="Proceed", command=save_multiple).grid(row=1, column=0, columnspan=2, pady=10)

    def delete_record():
        def search_and_delete():
            search_key = search_var.get().lower()
            matched_ids = []
            for idx, record in enumerate(student_records):
                if (str(record["Rollno"]) == search_key or
                        record["Name"].lower() == search_key or
                        record["Father Name"].lower() == search_key):
                    matched_ids.append(idx)
            for idx in reversed(matched_ids):
                del student_records[idx]
                tree.delete(tree.get_children()[idx])
            search_window.destroy()

        search_window = tk.Toplevel(root)
        search_window.title("Delete Record")

        tk.Label(search_window, text="Enter Rollno, Name, or Father Name:").grid(row=0, column=0, padx=10, pady=5)
        search_var = tk.StringVar()
        tk.Entry(search_window, textvariable=search_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Button(search_window, text="Delete", command=search_and_delete).grid(row=1, column=0, columnspan=2, pady=10)

    def update_record():
        def search_and_update():
            search_key = search_var.get().lower()
            for record in student_records:
                if (str(record["Rollno"]) == search_key or
                        record["Name"].lower() == search_key or
                        record["Father Name"].lower() == search_key):
                    # Open update window
                    update_window = tk.Toplevel(root)
                    update_window.title("Update Record")

                    def save_update():
                        record["Name"] = name_var.get()
                        record["Father Name"] = father_name_var.get()
                        record["CGPA"] = float(cgpa_var.get())
                        record["Contact"] = contact_var.get()
                        record["Address"] = address_var.get()
                        update_window.destroy()
                        refresh_tree()

                    tk.Label(update_window, text="Name:").grid(row=0, column=0, padx=10, pady=5)
                    name_var = tk.StringVar(value=record["Name"])
                    tk.Entry(update_window, textvariable=name_var).grid(row=0, column=1, padx=10, pady=5)

                    tk.Label(update_window, text="Father Name:").grid(row=1, column=0, padx=10, pady=5)
                    father_name_var = tk.StringVar(value=record["Father Name"])
                    tk.Entry(update_window, textvariable=father_name_var).grid(row=1, column=1, padx=10, pady=5)

                    tk.Label(update_window, text="CGPA:").grid(row=2, column=0, padx=10, pady=5)
                    cgpa_var = tk.StringVar(value=record["CGPA"])
                    tk.Entry(update_window, textvariable=cgpa_var).grid(row=2, column=1, padx=10, pady=5)

                    tk.Label(update_window, text="Contact:").grid(row=3, column=0, padx=10, pady=5)
                    contact_var = tk.StringVar(value=record["Contact"])
                    tk.Entry(update_window, textvariable=contact_var).grid(row=3, column=1, padx=10, pady=5)

                    tk.Label(update_window, text="Address:").grid(row=4, column=0, padx=10, pady=5)
                    address_var = tk.StringVar(value=record["Address"])
                    tk.Entry(update_window, textvariable=address_var).grid(row=4, column=1, padx=10, pady=5)

                    tk.Button(update_window, text="Save", command=save_update).grid(row=5, column=0, columnspan=2, pady=10)

            search_window.destroy()

        search_window = tk.Toplevel(root)
        search_window.title("Update Record")

        tk.Label(search_window, text="Enter Rollno, Name, or Father Name:").grid(row=0, column=0, padx=10, pady=5)
        search_var = tk.StringVar()
        tk.Entry(search_window, textvariable=search_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Button(search_window, text="Search", command=search_and_update).grid(row=1, column=0, columnspan=2, pady=10)

    def refresh_tree():
        # Clear the current tree view
        for i in tree.get_children():
            tree.delete(i)
        # Populate tree with updated records
        for record in student_records:
            tree.insert("", tk.END, values=(
                record["Rollno"],
                record["Name"],
                record["Father Name"],
                record["CGPA"],
                record["Contact"],
                record["Address"],
            ))

    # Root window
    root = tk.Tk()
    root.title("Student Records")

    # Treeview widget
    columns = ("Rollno", "Name", "Father Name", "CGPA", "Contact", "Address")
    tree = ttk.Treeview(root, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.CENTER)

    tree.pack(fill=tk.BOTH, expand=True)

    # Populate tree with initial data
    refresh_tree()

    # Buttons
    button_frame = tk.Frame(root)
    button_frame.pack(fill=tk.X)

    tk.Button(button_frame, text="Add Record", command=add_record).pack(side=tk.LEFT, padx=10, pady=10)
    tk.Button(button_frame, text="Add Multiple Records", command=add_multiple_records).pack(side=tk.LEFT, padx=10, pady=10)
    tk.Button(button_frame, text="Delete Record", command=delete_record).pack(side=tk.LEFT, padx=10, pady=10)
    tk.Button(button_frame, text="Update Record", command=update_record).pack(side=tk.LEFT, padx=10, pady=10)

    root.mainloop()

# Run the GUI
create_student_records_gui()

