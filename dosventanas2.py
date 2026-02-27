import tkinter as tk

def ventana_principal():
    global ven1
    ven1 = tk.Tk()
    ven1.title("Ventana principal")
    ven1.geometry("300x500")
    ven1.config(bg="light blue")

    etiqueta1 = tk.Label(ven1, text="Esta es la ventana principal")
    etiqueta1.pack()

    # Aquí llamamos a la ventana 2
    boton1 = tk.Button(ven1, text="Ir a Ventana 2", command=ventana_2)
    boton1.pack(pady=20)

    ven1.mainloop()

def ventana_2():
    # Eliminamos la principal para "cambiar" de pantalla
    ven1.destroy() 
    
    ven2 = tk.Tk()
    ven2.title("Ventana secundaria")
    ven2.geometry("300x500")
    ven2.config(bg="light green")

    etiqueta2 = tk.Label(ven2, text="Esta es la ventana 2")
    etiqueta2.pack()

    # Al cerrar la 2, regresamos a la principal
    boton2 = tk.Button(ven2, text="Regresar", command=lambda: destruir_ventana(ven2))
    boton2.pack(pady=20)

    ven2.mainloop()

def destruir_ventana(ventana_actual):
    ventana_actual.destroy()
    ventana_principal()

# SOLO llama a la principal para iniciar el ciclo
ventana_principal()
