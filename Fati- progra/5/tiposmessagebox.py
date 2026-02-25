import tkinter as tk
from tkinter import messagebox

def ventanas():
    if var.get()==1:
        messagebox.showinfo("Ventana de informacion", "Aca puedes escribir info al usuario")
    elif var.get()==2:
        messagebox.showwarning("Ventana de advertencia", "Esta es una advertencia")
    elif var.get()==3:
        messagebox.showerror("Ventana de error", "Has cometido un error")
    elif var.get()==4:
        respuesta=messagebox.askyesno("Ventana de opcion", "Te gusta esta clase")
        if respuesta:
            messagebox.showinfo("Ventana de respuesta", "Mas te vale")
        else:
            messagebox.showinfo("Ventana de respuesta", "Por eso vas a reprobar")
    elif var.get()==5:
        respuesta=messagebox.askokcancel("Ventana de opcion", "Te esfuerzas en esta clase? ")
        if respuesta:
            messagebox.showinfo("Ventana de respuesta", "Por eso vas a sacar 10")
        else:
            messagebox.showinfo("Ventana de respuesta", "Por eso repruebas")
    else:
        messagebox.showinfo("Vnetana de respuesta", "No diste ninguna respuesta")
def opcion():
    if var.get()==1:
        messagebox.showinfo("opcion", "Tu comida favorita son los tacos")
    else:
        messagebox.showinfo("Estado", "checkbutton no esta seleccionado")
ven1=tk.Tk()
ven1.title("Tipos de messagebox")
ven1.geometry("500x700")
ven1.config(bg="lightblue")
etiqueta1=tk.Label(ven1, text="Tipos de message")
etiqueta1.pack(pady=20)

var=tk.IntVar()
but1=tk.Radiobutton(ven1, text="Mostrar info", variable=var, value=1)
but1.pack(pady=20)
but2=tk.Radiobutton(ven1, text="Advertencia", variable=var, value=2)
but2.pack(pady=20)
but3=tk.Radiobutton(ven1, text="Error", variable=var, value=3)
but3.pack(pady=20)
but4=tk.Radiobutton(ven1, text="Pregunta si o no", variable=var, value=4)
but4.pack(pady=20)
but5=tk.Radiobutton(ven1, text="Pregunta aceptar o cancelar", variable=var, value=5)
but5.pack(pady=20)
boton1=tk.Button(ven1, text="Sacar ventana", command=ventanas)
boton1.pack(pady=30)
ven1.mainloop()
