from tkinter import Tk, Label
from PIL import Image, ImageTk
import os



def mostrar_imagen(imagen_path):
    root = Tk()
    root.title("Prueba de Imagen")
    img = Image.open(imagen_path)
    img_tk = ImageTk.PhotoImage(img)
    
    label = Label(root, image=img_tk)
    label.image = img_tk  # Mantener la referencia de la imagen
    label.pack()

    root.mainloop()

# Prueba con una ruta absoluta o verifica que la ruta relativa sea correcta
ruta_absoluta = os.path.abspath('src/assets/check.jpg')
mostrar_imagen(ruta_absoluta)
