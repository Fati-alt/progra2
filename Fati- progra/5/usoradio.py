import tkinter as tk
from tkinter import messagebox

def opcion():
    if var.get()==1:
        messagebox.showinfo("opcion", "Tu comida favorita son los tacos")
    elif var.get()==2:
        messagebox.showinfo("opcion", "Tu comida favorita son las hamburguesas")
    elif var.get()==3:
        messagebox.showinfo("opcion", "Tu comida favorita son las chanclas")
    elif var.get()==4:
        messagebox.showinfo("opcion", "Tu comida favorita son las milanesas") 
    else:
        messagebox.showinfo("Opcion elegida", "No seleccionaste nada ")   
ven1=tk.Tk()
ven1.title("Uso de radiobutton")
ven1.geometry("500x700")
etiqueta1=tk.Label(ven1, text="¿Cual es tu comida favorita?")
etiqueta1.pack(pady=20)

var=tk.IntVar()
but1=tk.Radiobutton(ven1, text="Tacos", variable=var, value=1)
but1.pack()
but2=tk.Radiobutton(ven1, text="Hamburguesas", variable=var, value=2)
but2.pack()
but3=tk.Radiobutton(ven1, text="Chanclas", variable=var, value=3)
but3.pack()
but4=tk.Radiobutton(ven1, text="Milanesas", variable=var, value=4)
but4.pack()

boton1=tk.Button(ven1, text="Verificar", command=opcion)
boton1.pack(pady=30)

ven1.mainloop()