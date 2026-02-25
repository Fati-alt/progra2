import tkinter as tk
from tkinter import messagebox

def estatus():
    if var.get()==1:
        messagebox.showinfo("Estado ", "Checkbutton seleccionado")
    else:
        messagebox.showinfo("Estado", "checkbutton no esta seleccionado")

ventana1=tk.Tk()
ventana1.title("uso del checkbutton")
ventana1.geometry("500x700")

etiqueta1=tk.Label(ventana1, text="Aqui va a haber un checkbutton")
etiqueta1.pack(pady=20)
var=tk.IntVar()
bcheck=tk.Checkbutton(ventana1, text="Elegir opcion", variable=var)
bcheck.pack(pady=10)
boton1=tk.Button(ventana1, text="Verificar status", command=estatus)
boton1.pack()


ventana1.mainloop()