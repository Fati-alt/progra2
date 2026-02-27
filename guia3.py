import tkinter as tk

#Crear ventana
root=tk.Tk()
root.title("Ejemplo de grid")
root.geometry("500x200")
root.config(bg="light blue")

#Crear etiquetas y campos de entarda con grid
etiqueta1=tk.Label(root, text="Nombre:", bg="light blue", fg="white", font=('Arial', 12, 'bold'))
etiqueta1.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entrada1=tk.Entry(root, width=60)
entrada1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Correo:", bg="light blue", fg="white", font=('Arial', 12, 'bold')).grid(row=1, column=0, padx=5, pady=5, sticky="w")
entrada2= tk.Entry(root, width=45)
entrada2.grid(row=1, column=1, padx=5, sticky="e")

#Boton centrado en dos columnas
tk.Button(root, text="Enviar").grid(row=2, column=0, columnspan=2, pady=10)
root.mainloop()