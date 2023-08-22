from tkinter import *

# Screem
screen = Tk()
screen.title("Mile to KM converter")
screen.minsize(width=400,height=100)
screen.config(padx=100,pady=50)

# Labels
miles_label = Label(text="Miles",font=("Arial",15))
miles_label.grid(column=11,row=5)
km_label = Label(text="KM", font=("Arial",15))
km_label.grid(column=11,row=6)
info_label = Label(text="is equal to:", font=("Arial",15))
info_label.grid(column=9,row=6)

#KM converted label

converted_km = Label(text="0",font=("Arial",15))
converted_km.grid(column=10,row=6)

# Entry bok
input_box = Entry(width=10)
input_box.grid(column=10,row=5)

# Button

def calculate():
    mile = input_box.get()
    km = round(int(mile) * 1.609)
    converted_km.config(text=str(km))

button = Button(text="Calculate", command=calculate)
button.grid(column=10,row=7)

screen.mainloop()