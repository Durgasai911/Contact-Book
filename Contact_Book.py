import tkinter as tk
from tkinter import messagebox

# Initialize window
root = tk.Tk()
root.geometry('700x550')
root.config(bg="#D1CBCB")
root.title('Contact Book')
root.resizable(0, 0)

# Sample contact list
contact_list = [
    ['Siddharth Nigam', '369854712'],
    ['Gaurav Patil', '521155222'],
    ['Abhishek Nikam', '78945614'],
    ['Sakshi Gaikwad', '58745246'],
    ['Mohit Paul', '5846975'],
    ['Karan Patel', '5647892'],
    ['Sam Sharma', '89685320'],
    ['John Maheshwari', '98564785'],
    ['Ganesh Pawar', '85967412']
]

name_var = tk.StringVar()
number_var = tk.StringVar()

# Create frame for the contact list
frame = tk.Frame(root)
frame.pack(side=tk.RIGHT)

scroll = tk.Scrollbar(frame, orient=tk.VERTICAL)
select = tk.Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman', 16), bg="#FFFFFF", width=20, height=20, borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
select.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Function to get the index of the selected item
def get_selected_index():
    if not select.curselection():
        messagebox.showerror("Error", "Please select a contact.")
        return None
    return int(select.curselection()[0])

# Function to add a new contact
def add_contact():
    if name_var.get() and number_var.get():
        contact_list.append([name_var.get(), number_var.get()])
        update_contact_listbox()
        reset_entry_fields()
        messagebox.showinfo("Confirmation", "Contact added successfully.")
    else:
        messagebox.showerror("Error", "Please fill in all the information.")

# Function to edit an existing contact
def update_contact():
    selected_index = get_selected_index()
    if selected_index is not None and name_var.get() and number_var.get():
        contact_list[selected_index] = [name_var.get(), number_var.get()]
        messagebox.showinfo("Confirmation", "Contact updated successfully.")
        reset_entry_fields()
        update_contact_listbox()
    elif selected_index is None:
        messagebox.showerror("Error", "Please select a contact to update.")
    else:
        messagebox.showerror("Error", "Please fill in all the information to update.")

# Function to reset the entry fields
def reset_entry_fields():
    name_var.set('')
    number_var.set('')

# Function to delete a selected contact
def delete_entry():
    selected_index = get_selected_index()
    if selected_index is not None:
        result = messagebox.askyesno('Confirmation', 'Are you sure you want to delete the selected contact?')
        if result:
            del contact_list[selected_index]
            update_contact_listbox()
    else:
        messagebox.showerror("Error", "Please select a contact to delete.")

# Function to view contact details
def view_contact():
    selected_index = get_selected_index()
    if selected_index is not None:
        name, phone = contact_list[selected_index]
        name_var.set(name)
        number_var.set(phone)

# Function to exit the application
def exit_app():
    root.destroy()

# Function to populate the listbox
def update_contact_listbox():
    contact_list.sort()
    select.delete(0, tk.END)
    for name, phone in contact_list:
        select.insert(tk.END, name)

# Populate the listbox on startup
update_contact_listbox()

# Define labels, entries, and buttons
tk.Label(root, text='Name', font=("Times new roman", 25, "bold"), bg='SlateGray3').place(x=30, y=20)
tk.Entry(root, textvariable=name_var, width=30).place(x=200, y=30)
tk.Label(root, text='Contact No.', font=("Times new roman", 22, "bold"), bg='SlateGray3').place(x=30, y=70)
tk.Entry(root, textvariable=number_var, width=30).place(x=200, y=80)

tk.Button(root, text="ADD", font='Helvetica 18 bold', bg="#43A047", command=add_contact, padx=20).place(x=50, y=140)
tk.Button(root, text="EDIT", font='Helvetica 18 bold', bg='#1976D2', command=update_contact, padx=20).place(x=50, y=200)
tk.Button(root, text="DELETE", font='Helvetica 18 bold', bg='#D32F2F', command=delete_entry, padx=20).place(x=50, y=260)
tk.Button(root, text="VIEW", font='Helvetica 18 bold', bg='#4681F4', command=view_contact).place(x=50, y=325)
tk.Button(root, text="RESET", font='Helvetica 18 bold', bg='#F57C00', command=reset_entry_fields).place(x=50, y=390)
tk.Button(root, text="EXIT", font='Helvetica 24 bold', bg='#B71C1C', command=exit_app).place(x=250, y=470)

# Start the main event loop
root.mainloop()
