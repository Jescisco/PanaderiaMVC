from customtkinter import *
from view.mainView import *

if __name__ == "__main__":
    pantalla = CTk()
    pantalla.title("Panaderia SUS")
    pantalla.geometry("300x500")
    pantalla.resizable(width=False, height=False)
    Menu(pantalla)
    pantalla.mainloop()