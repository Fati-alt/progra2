import tkinter as tk
from PIL import Image, ImageTk

def ventana_principal():
    global ven1
    ven1 = tk.Tk()
    ven1.title("Ventana principal")
    ven1.geometry("300x500")
    ven1.config(bg="light blue")

    etiqueta1 = tk.Label(ven1, text="Reino animal")
    etiqueta1.pack()

    # Aquí llamamos a la ventana 2
    boton1 = tk.Button(ven1, text="Ir a Ventana 2", command=ventana_2)
    boton1.pack()

    ven1.mainloop()
def ventana_2():
    global ven2
    # Eliminamos la principal para "cambiar" de pantalla
    ven1.destroy() 
    
    ven2 = tk.Tk()
    ven2.title("Ventana secundaria")
    ven2.geometry("300x500")
    ven2.config(bg="light green")

    etiqueta2 = tk.Label(ven2, text="Esta es la ventana 2")
    etiqueta2.pack()

    # Al cerrar la 2, regresamos a la principal
    boton2 = tk.Button(ven2, text="Ir a ventana 3", command=ventana_3)
    boton2.pack()

    ven2.mainloop()
def ventana_3():
    global ven3
    # Eliminamos la principal para "cambiar" de pantalla
    ven2.destroy()
    ven3 = tk.Tk()
    ven3.title("Ventana terciaria")
    ven3.geometry("300x500")
    ven3.config(bg="pink")

    etiqueta3 = tk.Label(ven3, text="Esta es la ventana 3")
    etiqueta3.pack()

    # Al cerrar la 2, regresamos a la principal
    boton3 = tk.Button(ven3, text="Ir a la ventana 4", command=ventana_4)
    boton3.pack()

    ven3.mainloop()
def ventana_4():
    global ven4
    # Eliminamos la principal para "cambiar" de pantalla
    ven3.destroy()
    ven4 = tk.Tk()
    ven4.title("Ventana cuarta")
    ven4.geometry("300x500")
    ven4.config(bg="light yellow")

    etiqueta4 = tk.Label(ven4, text="Esta es la ventana 4")
    etiqueta4.pack()

    # Al cerrar la 2, regresamos a la principal
    boton4 = tk.Button(ven4, text="Ir a ventana 5", command=ventana_5)
    boton4.pack(pady=20)

    ven4.mainloop()
def ventana_5():
    # Eliminamos la principal para "cambiar" de pantalla 
    ven4.destroy()
    ven5 = tk.Tk()
    ven5.title("Ventana quinta")
    ven5.geometry("300x500")
    ven5.config(bg="red")

    etiqueta5 = tk.Label(ven5, text="Esta es la ventana 5")
    etiqueta5.pack()

    # Al cerrar la 2, regresamos a la principal
    boton5 = tk.Button(ven5, text="Regresar", command=lambda: destruir_ventana(ven5))
    boton5.pack(pady=20)

    ven5.mainloop()

def destruir_ventana(ventana_actual):
    ventana_actual.destroy()
    ventana_principal()

# SOLO llama a la principal para iniciar el ciclo
ventana_principal()

