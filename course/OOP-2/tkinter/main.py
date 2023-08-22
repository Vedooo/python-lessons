from tkinter import *


#Window

window = Tk()
window.title("GUI")
window.minsize(width=400, height=400)
window.config(padx=100,pady=100)

# Label

label = Label(text="Label", font=("Arial",24,"bold"))
label["text"] = "TEXT"
label.config(text="TEXT")
label.grid(column=0,row=0)
# label.pack()

# Buttons 

def button_clicked():
    new_text = input.get()
    label.config(text=new_text)

button = Button(text="Button", command=button_clicked)
button2 = Button(text="New Button")
button.grid(column=2,row=2)
button2.grid(column=4, row=0)

# button.pack()
#button.grid(column=5, row=5)

# Entry

input = Entry(width=10)
print(input.get())
input.grid(column=10,row=10)
# input.pack()

window.mainloop()