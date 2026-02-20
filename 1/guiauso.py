#Importamos librerias
import tkinter as tk

#Definimos la ventana
ven1 = tk.Tk()
#Le damos un titulo a la ventana
ven1.title("Mi primera aplicacion con tkinter")
#Programas dimensiones 
ven1.geometry("600x500")
#Crear etiqueta
etiqueta1 = tk.Label(ven1,text="Hola mi nombre es Fati", 
    font=("Arial", 14, "bold"), fg="black", bg="light blue", padx=20, pady=10)
etiqueta1.place(x=50,y=200)
etiqueta2 = tk.Label(ven1,text="Estoy en la carrera de ICC", 
    font=("Arial", 14, "bold"), fg="black", bg="light blue", padx=20, pady=10)
etiqueta2.pack()
etiqueta3 = tk.Label(ven1,text="Mi comida favorita son las hamburguesas", 
    font=("Arial", 14, "bold"), fg="black", bg="light blue", padx=20, pady=10)
etiqueta3.pack()
#etiqueta.place(x=50,y=200)
#Iniciar el bucle principal de la aplicacion 
ven1.mainloop()