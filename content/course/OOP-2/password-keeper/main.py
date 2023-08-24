from tkinter import *
from tkinter import messagebox
import random as rd
import pyperclip


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
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Opps", 
                            message="Please don't leave any fields empty!")
    else:
        is_ok =messagebox.askokcancel(title="Website", 
                                    message=f"These are the details entered:"
                                            f"\nEmail: {email}"
                                            f"\nPassword: {password}\n"
                                            "Is it ok to save?")
        
        if is_ok:
            with open("records.txt",mode="a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
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

password_generate_button = Button(text="Generate Password", command=generate_password)
password_generate_button.grid(column=2,row=3)
password_generate_button.config(width=10)

add_button = Button(text="ADD",width=33,command=save)
add_button.grid(column=1,row=6,columnspan=2)

ui.mainloop()