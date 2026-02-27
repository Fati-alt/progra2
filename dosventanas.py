import tkinter as tk
def ventana_principal():
    global ven1
    ven1=tk.Tk()
    ven1.title("Ventana principal")
    ven1.geometry("300x500")
    ven1.config(bg="light blue")

    etiqueta1=tk.Label(ven1, text="Esta es la ventana principal")
    etiqueta1.pack()

    boton1=tk.Button(ven1, text="Ventana 2", command=ventana_2)
    boton1.pack(pady=20)

    ven1.mainloop()
def destruir_ventana(ventana_actual):
    ventana_actual.destroy()
    ventana_principal()

#Ventana 2
def ventana_2():
    ven1.destroy()
    ven2=tk.Tk()
    ven2.title("Ventana secundaria")
    ven2.geometry("300x500")
    ven2.config(bg="light green")

    etiqueta2=tk.Label(ven2, text="Esta es la ventana 2")
    etiqueta2.pack()

    boton2=tk.Button(ven2, text="Ventana 2", command=lambda:destruir_ventana(ven2))
    boton2.pack(pady=20)

    ven2.mainloop()
    
ventana_2()
ventana_principal()