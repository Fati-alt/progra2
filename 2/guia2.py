import tkinter as tk
from PIL import Image, ImageTk

def boton_click():
    print("click")
def actualizar_etiqueta():
    nuevo_texto=entrada.get()#obtiene el texto en el cuadro
    etiqueta.config(text=nuevo_texto)#actualiza el texto
root = tk.Tk()
root.title("Imagen en Tkinter")
#campo de entrada
entrada=tk.Entry(root, width=60)
entrada.pack(pady=10)
#etiqueta
etiqueta=tk.Label(root, text="Texto inicial", font=("Arial", 12))
etiqueta.pack(pady=10)
#crear boton
boton = tk.Button(root, text="actualizar", command=actualizar_etiqueta)
boton.pack()
#cargar la imagen
imagen1=Image.open("Kanye-West-.png")
imagen1=imagen1.resize((400, 200)) #redimensionar
imagen1_tk=ImageTk.PhotoImage(imagen1)
label_imagen=tk.Label(root, image=imagen1_tk)
label_imagen.pack(pady=20)

root.mainloop()