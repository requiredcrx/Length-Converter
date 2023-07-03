from tkinter import *

FONT = ("Arial", 20,)

screen = Tk()
screen.title("Length Converter by Required")
screen.minsize(width=200, height=200)
screen.config(padx=50, pady=50)

label = Label(text="Is equal to", font=("Times in Roman", 20))
label.grid(row=1, column=0)
label.config(padx=5, pady=5)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(row=0, column=1)


label2 = Label(text="Miles", font=FONT)
label2.grid(row=0, column=2)
label2.config(padx=5, pady=5)

label3 = Label(text="Km", font=FONT)
label3.grid(row=1, column=2)
label3.config(padx=5, pady=5)

result = Label(text="0", font=FONT)
result.grid(row=1, column=1)
label.config(padx=5, pady=5)


def calculate():
    mile = float(entry.get())
    km = mile * 1.609344
    result.config(text=f"{km}")


button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)
button.config(padx=5, pady=5)


screen.mainloop()
