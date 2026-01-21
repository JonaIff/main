from tkinter import *
from tkinter.ttk import *

def exchange (waehrung,betrag):
    if waehrung == "€":
        dollar = betrag * 1.15
        print(f"Umgerechnet sind das {dollar} $ ")
        pound = betrag * 0.88
        print(f"Umgerechnet sind das {pound} £")
    if waehrung == "$":
        euro = betrag * 0.86
        print(f"Umgerechnet sind das {euro} €")
        pound = betrag * 0,76
        print(f"Umgerechnet sind das {pound} £")
    if waehrung == "£":
        dollar = betrag * 1.32
        print(f"Umgerechnet sind das {dollar} $ ")
        euro = betrag * 1.13
        print(f"Umgerechnet sind das {euro} €")

root = Tk()
root.title ("Wärungsumrechner V.2")
root.geometry (400, 300)




root.mainloop() 