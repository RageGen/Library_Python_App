from tkinter import ttk
from tkinter import constants
from tkinter import messagebox
import tkinter as tk
import postgresql_commands_books
import postgresql_commands_readers
import postgresql_commands_magazine
import re
def show_table_data_books():
    index = 0
    books_table.delete(*books_table.get_children())
    for rows in postgresql_commands_books.fetch_data():
        books_table.insert("", index, values=rows)
        index = index + 1
    return
    
def insert_book():
    if  not re.match(r'\d\d\d\d\d\d\d\d\d\d\d\d\d',entry_isbn.get()):
        messagebox.showerror("Error!","Wrong ISBN!")
        return
    if not re.match(r'[A-Za-z]{2,25}( [A-Za-z]{2,25})?',entry_author.get()):
        messagebox.showerror("Error!","Wrong Author!")
        return
    if not re.match(r'([A-Za-z]{1,50})',entry_name.get()):
        messagebox.showerror("Error!","Wrong Name!")
        return
    if not re.match(r'[\d]{1,9}',entry_volume.get()):
        messagebox.showerror("Error!","Wrong Volume!")
        return
    if not re.match(r'^(soft|hard|Soft|Hard)$',entry_binding.get()):
        messagebox.showerror("Error!","Wrong Binding only 'soft' or 'hard'!")
        return
    if not re.match(r'^(\d{1,5}|\d{1,4}\.\d{2})$',entry_cost.get()):
        messagebox.showerror("Error!","Wrong Cost!")
        return
    postgresql_commands_books.insert_data_book(entry_isbn.get(),entry_author.get(),
    entry_name.get(),entry_volume.get(),entry_binding.get(),entry_cost.get())
    show_table_data_books()
    clear_item_book()
    return

def delete_book():
    if  not re.match(r'\d\d\d\d\d\d\d\d\d\d\d\d\d',entry_isbn.get()):
        messagebox.showerror("Error!","Wrong ISBN!")
        return
    value = entry_isbn.get()
    postgresql_commands_books.remove_data_book(value)
    show_table_data_books()
    clear_item_book()
    return

def update_book():
    if  not re.match(r'\d\d\d\d\d\d\d\d\d\d\d\d\d',entry_isbn.get()):
        messagebox.showerror("Error!","Wrong ISBN!")
        return
    if not re.match(r'[A-Za-z]{2,25}( [A-Za-z]{2,25})?',entry_author.get()):
        messagebox.showerror("Error!","Wrong Author!")
        return
    if not re.match(r'([A-Za-z]{1,50})',entry_name.get()):
        messagebox.showerror("Error!","Wrong Name!")
        return
    if not re.match(r'[\d]{1,9}',entry_volume.get()):
        messagebox.showerror("Error!","Wrong Volume!")
        return
    if not re.match(r'^(soft|hard|Soft|Hard)$',entry_binding.get()):
        messagebox.showerror("Error!","Wrong Binding only 'soft' or 'hard'!")
        return
    if not re.match(r'^(\d{1,5}|\d{1,4}\.\d{2})$',entry_cost.get()):
        messagebox.showerror("Error!","Wrong Cost!")
        return
    postgresql_commands_books.update_data_book(entry_author.get(),
    entry_name.get(),entry_volume.get(),entry_binding.get(),entry_cost.get(),entry_isbn.get())
    show_table_data_books()
    clear_item_book()
    return

def average_book_cost():
    value=postgresql_commands_books.average_cost()
    value=float(str(value[0]))
    value=round(value,3)
    messagebox.showinfo("Result",f"Average cost is {value}")

root = tk.Tk()
root.title("Library Base")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f"{width}x{height}")



def clear_item_book():
    entry_isbn.configure(state='normal')
    entry_isbn.delete(0, constants.END)
    entry_author.delete(0, constants.END)
    entry_name.delete(0, constants.END)
    entry_volume.delete(0, constants.END)
    entry_binding.delete(0, constants.END)
    entry_cost.delete(0, constants.END)

def select_item_book(event):
    global item_id
    global selected_item
    index = books_table.selection()
    selected_item = books_table.item(index)
    item_id = selected_item['values'][0]
    entry_isbn.configure(state='normal')
    entry_isbn.delete(0, constants.END)
    entry_isbn.insert(constants.END, selected_item['values'][0])
    entry_isbn.configure(state='readonly')
    entry_author.delete(0, constants.END)
    entry_author.insert(constants.END, selected_item['values'][1])
    entry_name.delete(0, constants.END)
    entry_name.insert(constants.END, selected_item['values'][2])
    entry_volume.delete(0, constants.END)
    entry_volume.insert(constants.END, selected_item['values'][3])
    entry_binding.delete(0, constants.END)
    entry_binding.insert(constants.END, selected_item['values'][4])
    entry_cost.delete(0, constants.END)
    entry_cost.insert(constants.END, selected_item['values'][5])


tabs_holder = ttk.Notebook(root)
books_tab = ttk.Frame(tabs_holder)
tabs_holder.add(books_tab,text="Books")

readers_tab = ttk.Frame(tabs_holder)
tabs_holder.add(readers_tab,text="Readers")

magazine_tab = ttk.Frame(tabs_holder)
tabs_holder.add(magazine_tab,text="Magazine")

label_isbn = tk.Label(books_tab,text='ISBN:')
label_isbn.grid(row=0,column=0)
entry_isbn = tk.Entry(books_tab)
entry_isbn.grid(row=1,column=0)

label_author = tk.Label(books_tab,text='Author:')
label_author.grid(row=0,column=1)
entry_author = tk.Entry(books_tab)
entry_author.grid(row=1,column=1)

label_name = tk.Label(books_tab,text='Name:')
label_name.grid(row=0,column=2)
entry_name = tk.Entry(books_tab)
entry_name.grid(row=1,column=2)

label_volume = tk.Label(books_tab,text='Volume:')
label_volume.grid(row=0,column=3)
entry_volume= tk.Entry(books_tab)
entry_volume.grid(row=1,column=3)

label_binding = tk.Label(books_tab,text='Binding:')
label_binding.grid(row=0,column=4)
entry_binding = tk.Entry(books_tab)
entry_binding.grid(row=1,column=4)

label_cost = tk.Label(books_tab,text='Cost:')
label_cost.grid(row=0,column=5)
entry_cost = tk.Entry(books_tab)
entry_cost.grid(row=1,column=5)

insert_book_button = tk.Button(books_tab,text="Insert Book",command=insert_book)
insert_book_button.grid(row=3,column=0,columnspan=12,sticky=constants.W,padx=5)

delete_book_button = tk.Button(books_tab,text="Delete Book",command=delete_book)
delete_book_button.grid(row=3,column=0,columnspan=12,sticky=constants.W,padx=150)

update_book_button = tk.Button(books_tab,text = 'Update Book',command=update_book)
update_book_button.grid(row=3,column=0,columnspan=12,sticky=constants.W,padx=300)

fetch_book_button = tk.Button(books_tab,text = 'Fetch Data',command=show_table_data_books)
fetch_book_button.grid(row=3,column=0,columnspan=12,sticky=constants.W,padx=460)

average_cost_button = tk.Button(books_tab,text = 'Average Cost',command=average_book_cost)
average_cost_button.grid(row=3,column=0,columnspan=12,sticky=constants.W,padx=600)

clear_magazine_button = tk.Button(books_tab,text = 'Clear',command=clear_item_book)
clear_magazine_button.grid(row=3,column=0,columnspan=12,sticky=constants.W,padx=770)

books_table = ttk.Treeview(books_tab,height=72)
books_table.grid(row=5, column=0, columnspan=20, rowspan=5, padx=5, sticky=constants.W)
books_table["columns"] = ("ISBN", "Author", "Name", "Volume", "Binding", "Cost")
books_table["show"] = "headings"
books_table.heading("ISBN",text="ISBN", anchor="w")
books_table.column("ISBN", width=300)
books_table.heading("Author", text="Author", anchor="w")
books_table.column("Author", width=300)
books_table.heading("Name", text="Name", anchor="w")
books_table.column("Name", width=800)
books_table.heading("Volume", text="Volume", anchor="w")
books_table.column("Volume", width=400)
books_table.heading("Binding", text="Binding", anchor="w")
books_table.column("Binding", width=800)
books_table.heading("Cost", text="Cost", anchor="w")
books_table.column("Cost", width=260)

books_table.bind("<<TreeviewSelect>>", select_item_book)



def show_table_data_readers():
    index = 0
    readers_table.delete(*readers_table.get_children())
    for rows in postgresql_commands_readers.fetch_data():
        readers_table.insert("", index, values=rows)
        index = index + 1
    return

def insert_reader():
    if not re.match(r'^\d{8}$',entry_passport_data.get()):
        messagebox.showerror("Error!","Wrong Passport Data!")
        return
    if not re.match(r'^[A-Za-z]+ [A-Za-z]+ [A-Za-z]+$',entry_full_name.get()):
        messagebox.showerror("Error!","Wrong Full Name!")
        return
    if not re.match(r'^(\+1\s?)?(\d{3}[-.\s]?)?\d{3}[-.\s]?\d{4}$',entry_phone_number.get()):
        messagebox.showerror("Error!","Wrong Phone Number!")
        return
    if not re.match(r'^\d{4}-\d{2}-\d{2}$',entry_registration_date.get()):
        messagebox.showerror("Error!","Wrong Registration Date!")
        return
    postgresql_commands_readers.insert_data_reader(entry_passport_data.get(),entry_full_name.get(),
    entry_phone_number.get(),entry_registration_date.get())
    show_table_data_readers()
    clear_item_reader()
    return

def delete_reader():
    if not re.match(r'^\d{8}$',entry_passport_data.get()):
        messagebox.showerror("Error!","Wrong Passport Data!")
        return
    value = entry_passport_data.get()
    postgresql_commands_readers.remove_data_reader(value)
    show_table_data_readers()
    clear_item_reader()
    return


        
def update_reader():
    if not re.match(r'^\d{8}$',entry_passport_data.get()):
        messagebox.showerror("Error!","Wrong Passport Data!")
        return
    if not re.match(r'^[A-Za-z]+ [A-Za-z]+ [A-Za-z]+$',entry_full_name.get()):
        messagebox.showerror("Error!","Wrong Full Name!")
        return
    if not re.match(r'^(\+1\s?)?(\d{3}[-.\s]?)?\d{3}[-.\s]?\d{4}$',entry_phone_number.get()):
        messagebox.showerror("Error!","Wrong Phone Number!")
        return
    if not re.match(r'^\d{4}-\d{2}-\d{2}$',entry_registration_date.get()):
        messagebox.showerror("Error!","Wrong Registration Date!")
        return
    postgresql_commands_readers.update_data_reader(entry_passport_data.get(),entry_full_name.get(),
    entry_phone_number.get(),entry_registration_date.get())
    show_table_data_readers()
    clear_item_reader()
    return


def clear_item_reader():
    entry_passport_data.configure(state="normal")
    entry_passport_data.delete(0, constants.END)
    entry_full_name.delete(0, constants.END)
    entry_phone_number.delete(0, constants.END)
    entry_registration_date.delete(0, constants.END)
    
def select_item_reader(event):
    global item_id
    global selected_item
    index = readers_table.selection()
    selected_item = readers_table.item(index)
    item_id = selected_item['values'][0]
    entry_passport_data.configure(state="normal")
    entry_passport_data.delete(0, constants.END)
    entry_passport_data.insert(constants.END, selected_item['values'][0])
    entry_passport_data.configure(state="readonly")
    entry_full_name.delete(0, constants.END)
    entry_full_name.insert(constants.END, selected_item['values'][1])
    entry_phone_number.delete(0, constants.END)
    entry_phone_number.insert(constants.END, selected_item['values'][2])
    entry_registration_date.delete(0, constants.END)
    entry_registration_date.insert(constants.END, selected_item['values'][3])

label_passport_data = tk.Label(readers_tab,text='Pasport:')
label_passport_data.grid(row=0,column=0)
entry_passport_data = tk.Entry(readers_tab)
entry_passport_data.grid(row=1,column=0)

label_full_name = tk.Label(readers_tab,text='Full Name:')
label_full_name.grid(row=0,column=1)
entry_full_name = tk.Entry(readers_tab)
entry_full_name.grid(row=1,column=1)

label_phone_number = tk.Label(readers_tab,text='Phone:')
label_phone_number.grid(row=0,column=2)
entry_phone_number = tk.Entry(readers_tab)
entry_phone_number.grid(row=1,column=2)

label_registration_date = tk.Label(readers_tab,text='Registration Date:')
label_registration_date.grid(row=0,column=3)
entry_registration_date = tk.Entry(readers_tab)
entry_registration_date.grid(row=1,column=3)

insert_reader_button = tk.Button(readers_tab,text="Insert Reader",command=insert_reader)
insert_reader_button.grid(row=3,column=0,columnspan=12,sticky=constants.W,padx=5)

delete_reader_button = tk.Button(readers_tab,text="Delete Reader",command=delete_reader)
delete_reader_button.grid(row=3,column=0,columnspan=12,sticky=constants.W,padx=170)

update_reader_button = tk.Button(readers_tab,text = 'Update Reader',command=update_reader)
update_reader_button.grid(row=3,column=0,columnspan=12,sticky=constants.W,padx=340)

fetch_reader_button = tk.Button(readers_tab,text = 'Fetch Data',command=show_table_data_readers)
fetch_reader_button.grid(row=3,column=0,columnspan=12,sticky=constants.W,padx=520)

clear_magazine_button = tk.Button(readers_tab,text = 'Clear',command=clear_item_reader)
clear_magazine_button.grid(row=3,column=0,columnspan=12,sticky=constants.W,padx=650)


readers_table = ttk.Treeview(readers_tab, height=72)
readers_table.grid(row=5, column=0, columnspan=20, rowspan=5, padx=5, sticky=constants.W)
readers_table["columns"] = ("Passport", "Full Name", "Phone", "Registration date")
readers_table["show"] = "headings"
readers_table.heading("Passport",text="Passport", anchor="w")
readers_table.column("Passport", width=700)
readers_table.heading("Full Name", text="Full Name", anchor="w")
readers_table.column("Full Name", width=800)
readers_table.heading("Phone", text="Phone", anchor="w")
readers_table.column("Phone", width=600)
readers_table.heading("Registration date", text="Registration date", anchor="w")
readers_table.column("Registration date", width=760)
readers_table.bind("<<TreeviewSelect>>", select_item_reader)

def show_table_data_magazine():
    index = 0
    magazine_table.delete(*magazine_table.get_children())
    for rows in postgresql_commands_magazine.fetch_data():
        magazine_table.insert("", index, values=rows)
        index = index + 1
    return

def insert_magazine():
    if  not re.match(r'\d\d\d\d\d\d\d\d\d\d\d\d\d',entry_book_isbn.get()):
        messagebox.showerror("Error!","Wrong ISBN!")
        return
    if not re.match(r'^\d{8}$',entry_reader_passport_data.get()):
        messagebox.showerror("Error!","Wrong Passport Data!")
        return
    if not re.match(r'^\d{4}-\d{2}-\d{2}$',entry_issue_date.get()):
        messagebox.showerror("Error!","Wrong Issue Date!")
        return
    if not re.match(r'^\d{4}-\d{2}-\d{2}$',entry_deadline.get()):
        messagebox.showerror("Error!","Wrong Deadline!")
        return
    postgresql_commands_magazine.insert_data_magazine(entry_book_isbn.get(),entry_reader_passport_data.get(),
    entry_issue_date.get(),entry_deadline.get())
    show_table_data_magazine()
    clear_item_magazine()
    return

def delete_magazine():
    if  not re.match(r'\d\d\d\d\d\d\d\d\d\d\d\d\d',entry_book_isbn.get()):
        messagebox.showerror("Error!","Wrong ISBN!")
        return
    value = entry_book_isbn.get()
    postgresql_commands_magazine.remove_data_magazine(value)
    show_table_data_magazine()
    clear_item_magazine()
    return


        
def update_magazine():
    if  not re.match(r'\d\d\d\d\d\d\d\d\d\d\d\d\d',entry_book_isbn.get()):
        messagebox.showerror("Error!","Wrong ISBN!")
        return
    if not re.match(r'^\d{8}$',entry_reader_passport_data.get()):
        messagebox.showerror("Error!","Wrong Passport Data!")
        return
    if not re.match(r'^\d{4}-\d{2}-\d{2}$',entry_issue_date.get()):
        messagebox.showerror("Error!","Wrong Issue Date!")
        return
    if not re.match(r'^\d{4}-\d{2}-\d{2}$',entry_deadline.get()):
        messagebox.showerror("Error!","Wrong Deadline!")
        return
    postgresql_commands_magazine.update_data_magazine(entry_book_isbn.get(),entry_reader_passport_data.get(),entry_issue_date.get(),
    entry_deadline.get())
    show_table_data_magazine()
    clear_item_magazine()
    return

def show_expired_readers():
    window = tk.Toplevel(root)
    window.title("Expired Readers")

    tree = ttk.Treeview(window,height=72)
    tree["columns"] = ("ISBN", "Passport", "Issue date", "Deadline")
    tree.grid(row=0, column=0, columnspan=20, rowspan=5, padx=5, sticky=constants.W)
    tree["show"] = "headings"
    tree.heading("ISBN",text="ISBN", anchor="w")
    tree.column("ISBN", width=700)
    tree.heading("Passport", text="Passport", anchor="w")
    tree.column("Passport", width=800)
    tree.heading("Issue date", text="Issue date", anchor="w")
    tree.column("Issue date", width=600)
    tree.heading("Deadline", text="Deadline", anchor="w")
    tree.column("Deadline", width=760)
    tree.pack(expand=True, fill=tk.BOTH)
    index = 0
    tree.delete(*tree.get_children())
    for rows in postgresql_commands_magazine.expired_readers():
        tree.insert("", index, values=rows)
        index = index + 1
    return


def clear_item_magazine():
    entry_book_isbn.configure(state="normal")
    entry_book_isbn.delete(0, constants.END)
    entry_reader_passport_data.configure(state="normal")
    entry_reader_passport_data.delete(0, constants.END)
    entry_issue_date.delete(0, constants.END)
    entry_deadline.delete(0, constants.END)
    
def select_item_magazine(event):
    global item_id
    global selected_item
    index = magazine_table.selection()
    selected_item = magazine_table.item(index)
    item_id = selected_item['values'][0]
    entry_book_isbn.configure(state="normal")
    entry_book_isbn.delete(0, constants.END)
    entry_book_isbn.insert(constants.END, selected_item['values'][0])
    entry_book_isbn.configure(state="readonly")
    entry_reader_passport_data.configure(state="normal")
    entry_reader_passport_data.delete(0, constants.END)
    entry_reader_passport_data.insert(constants.END, selected_item['values'][1])
    entry_reader_passport_data.configure(state="readonly")
    entry_issue_date.delete(0, constants.END)
    entry_issue_date.insert(constants.END, selected_item['values'][2])
    entry_deadline.delete(0, constants.END)
    entry_deadline.insert(constants.END, selected_item['values'][3])

label_book_isbn = tk.Label(magazine_tab,text='ISBN:')
label_book_isbn.grid(row=0,column=0)
entry_book_isbn = tk.Entry(magazine_tab)
entry_book_isbn.grid(row=1,column=0)

label_reader_passport_data = tk.Label(magazine_tab,text='Passport:')
label_reader_passport_data.grid(row=0,column=1)
entry_reader_passport_data = tk.Entry(magazine_tab)
entry_reader_passport_data.grid(row=1,column=1)

label_issue_date = tk.Label(magazine_tab,text='Issue date:')
label_issue_date.grid(row=0,column=2)
entry_issue_date = tk.Entry(magazine_tab)
entry_issue_date.grid(row=1,column=2)

label_deadline = tk.Label(magazine_tab,text='Deadline:')
label_deadline.grid(row=0,column=3)
entry_deadline = tk.Entry(magazine_tab)
entry_deadline.grid(row=1,column=3)

insert_magazine_button = tk.Button(magazine_tab,text="Insert Magazine",command=insert_magazine)
insert_magazine_button.grid(row=3,column=0,columnspan=12,sticky=constants.W,padx=5)

delete_magazine_button = tk.Button(magazine_tab,text="Delete Magazine",command=delete_magazine)
delete_magazine_button.grid(row=3,column=0,columnspan=12,sticky=constants.W,padx=200)

update_magazine_button = tk.Button(magazine_tab,text = 'Update Magazine',command=update_magazine)
update_magazine_button.grid(row=3,column=0,columnspan=12,sticky=constants.W,padx=400)

fetch_magazine_button = tk.Button(magazine_tab,text = 'Fetch Data',command=show_table_data_magazine)
fetch_magazine_button.grid(row=3,column=0,columnspan=12,sticky=constants.W,padx=600)

expired_readers_button = tk.Button(magazine_tab,text = 'Expired Readers',command=show_expired_readers)
expired_readers_button.grid(row=3,column=0,columnspan=12,sticky=constants.W,padx=740)

clear_magazine_button = tk.Button(magazine_tab,text = 'Clear',command=clear_item_magazine)
clear_magazine_button.grid(row=3,column=0,columnspan=12,sticky=constants.W,padx=940)


magazine_table = ttk.Treeview(magazine_tab,height=72)
magazine_table.grid(row=5, column=0, columnspan=20, rowspan=5, padx=5, sticky=constants.W)
magazine_table["columns"] = ("ISBN", "Passport", "Issue date", "Deadline")
magazine_table["show"] = "headings"
magazine_table.heading("ISBN",text="ISBN", anchor="w")
magazine_table.column("ISBN", width=700)
magazine_table.heading("Passport", text="Passport", anchor="w")
magazine_table.column("Passport", width=800)
magazine_table.heading("Issue date", text="Issue date", anchor="w")
magazine_table.column("Issue date", width=600)
magazine_table.heading("Deadline", text="Deadline", anchor="w")
magazine_table.column("Deadline", width=760)
magazine_table.bind("<<TreeviewSelect>>", select_item_magazine)


tabs_holder.pack(expand=1,fill="both")
show_table_data_books()
show_table_data_readers()
show_table_data_magazine()


root.mainloop()