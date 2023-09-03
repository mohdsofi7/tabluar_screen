import tkinter as tk
from tkinter import ttk

# Create an empty list to store student data
students = []

# Function to add a new student
def add_student():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    dob = dob_entry.get()
    parent_name = parent_name_entry.get()
    address = address_entry.get()
    city = city_entry.get()
    phone = phone_entry.get()

    student = {
        'First Name': first_name,
        'Last Name': last_name,
        'DOB': dob,
        "Parent's Name": parent_name,
        'Address': address,
        'City': city,
        'Phone': phone
    }

    students.append(student)
    update_student_table()
    clear_entries()

# Function to clear entry fields
def clear_entries():
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)
    parent_name_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

# Function to update the student table
def update_student_table():
    for row in student_table.get_children():
        student_table.delete(row)
    
    for student in students:
        student_table.insert('', 'end', values=(
            student['First Name'],
            student['Last Name'],
            student['DOB'],
            student["Parent's Name"],
            student['Address'],
            student['City'],
            student['Phone']
        ))

# Create the main application window
root = tk.Tk()
root.title("Student Management System")

# Create labels and entry fields for student details
first_name_label = tk.Label(root, text="First Name:")
first_name_label.grid(row=0, column=0)
first_name_entry = tk.Entry(root)
first_name_entry.grid(row=0, column=1)

last_name_label = tk.Label(root, text="Last Name:")
last_name_label.grid(row=1, column=0)
last_name_entry = tk.Entry(root)
last_name_entry.grid(row=1, column=1)

dob_label = tk.Label(root, text="Date of Birth:")
dob_label.grid(row=2, column=0)
dob_entry = tk.Entry(root)
dob_entry.grid(row=2, column=1)

parent_name_label = tk.Label(root, text="Parent's Name:")
parent_name_label.grid(row=3, column=0)
parent_name_entry = tk.Entry(root)
parent_name_entry.grid(row=3, column=1)

address_label = tk.Label(root, text="Address:")
address_label.grid(row=4, column=0)
address_entry = tk.Entry(root)
address_entry.grid(row=4, column=1)

city_label = tk.Label(root, text="City:")
city_label.grid(row=5, column=0)
city_entry = tk.Entry(root)
city_entry.grid(row=5, column=1)

phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=6, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=6, column=1)

# Create buttons to add students and clear entries
add_button = tk.Button(root, text="Add Student", command=add_student)
add_button.grid(row=7, column=0, columnspan=2)

clear_button = tk.Button(root, text="Clear Entries", command=clear_entries)
clear_button.grid(row=8, column=0, columnspan=2)

# Create a table to display student data
columns = ("First Name", "Last Name", "DOB", "Parent's Name", "Address", "City", "Phone")
student_table = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    student_table.heading(col, text=col)
    student_table.column(col, width=100)

student_table.grid(row=9, column=0, columnspan=2)

# Start the main event loop
root.mainloop()
