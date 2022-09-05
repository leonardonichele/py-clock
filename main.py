from tkinter import *
from tkinter.ttk import *
from time import strftime

main = Tk()
main.title("PyClock - by Leonardo Nichele")

def view():
    info = strftime('%H:%M:%S %p')
    info += ' - PYTHON CLOCK'
    container.config(text=info)
    container.after(1000, view)

container = Label(main, font=("ds-digital", 80), background="black", foreground="cyan")
container.pack(anchor='center')
view()
mainloop()
