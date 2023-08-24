from tkinter import *
from tkinter import messagebox
import random as rd
import pyperclip
import json


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", mode= "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title=f"Error", message="No data file found")
    else:    
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"email: {email}\n password: {password}")
        else:
            messagebox.showinfo(title=f"Error", message=f"No details for {website} exists.")
               

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    password_letters = [rd.choice(letters) for _ in range(rd.randint(8,10))]
    password_numbers = [rd.choice(numbers) for _ in range(rd.randint(8,10))]
    password_symbols = [rd.choice(symbols) for _ in range(rd.randint(8,10))]
    
    password_list = password_letters + password_numbers + password_symbols
    rd.shuffle(password_list)
    
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Opps", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json",mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:       
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", mode='w') as data_file:
            # Saving and update data.
                json.dump(data, data_file, indent=4)
        finally:   
            website_entry.delete(0, END)
            password_entry.delete(0, END)
        
# ---------------------------- UI SETUP ------------------------------- #

ui = Tk()
ui.title("Password Manager")
ui.config(padx=20,pady=20)

logo_pic = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100,100,image=logo_pic)
canvas.grid(column=1,row=0)

# Labels

website_label = Label(text="Website:", font=("Times New Roman",15))
website_label.grid(column=0,row=1)
website_label.config(padx=20)

email_label = Label(text="Email/Username:", font=("Times New Roman",15))
email_label.grid(column=0,row=2)
email_label.config(padx=35)

password_label = Label(text="Password:", font=("Times New Roman",15))
password_label.grid(column=0,row=3)

# Entries

website_entry = Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.config(border=1)

email_entry = Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.config(border=1)
email_entry.insert(END,"blabla@hotmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)
password_entry.config(border=1)

# Buttons

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2,row=1)
search_button.config(width=10)

password_generate_button = Button(text="Generate Password", command=generate_password)
password_generate_button.grid(column=2,row=3)
password_generate_button.config(width=10)

add_button = Button(text="ADD",width=33,command=save)
add_button.grid(column=1,row=6,columnspan=2)

ui.mainloop()