import cv2
from pyzbar.pyzbar import decode
from tkinter import Tk, Label
from PIL import Image, ImageTk  # Importar Pillow
import threading
import pyttsx3
from playsound import playsound
import os  # Importar os para manejar rutas absolutas

# Definir la palabra clave que se debe validar al escanear
KEY_WORD = "CASAentrada"

# Función de lectura de voz
def leer_texto(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

# Ventana de alertas de Tkinter
def iniciar_ventana_alertas(alertas):
    root = Tk()
    root.title("Alertas")
    root.geometry("400x300")

    label_alerta = Label(root, text="Esperando escaneo...", font=("Helvetica", 14))
    label_alerta.pack(pady=20)

    def actualizar_alerta():
        if alertas:
            label_alerta.config(text=alertas[-1])
        root.after(500, actualizar_alerta)  # Actualiza cada 500 ms para respuesta más rápida

    actualizar_alerta()
    root.mainloop()

# Función para mostrar imágenes, leer texto y reproducir sonido en paralelo
def mostrar_alerta_con_voz(imagen_path, mensaje, audio_path=None):
    def mostrar_imagen():
        try:
            root = Tk()
            root.title(mensaje)
            imagen_path_absoluta = os.path.abspath(imagen_path)
            img = Image.open(imagen_path_absoluta)
            img_tk = ImageTk.PhotoImage(img)
            label = Label(root, image=img_tk)
            label.image = img_tk  # Mantener la referencia de la imagen
            label.pack()
            root.mainloop()
        except Exception as e:
            print(f"Error al mostrar la imagen: {e}")

    def reproducir_sonido():
        if audio_path:
            audio_absoluto = os.path.abspath(audio_path)
            playsound(audio_absoluto)

    hilo_imagen = threading.Thread(target=mostrar_imagen)
    hilo_voz = threading.Thread(target=leer_texto, args=(mensaje,))
    hilo_sonido = threading.Thread(target=reproducir_sonido)

    hilo_imagen.start()
    hilo_voz.start()
    hilo_sonido.start()

    hilo_imagen.join()
    hilo_voz.join()
    hilo_sonido.join()

# Lector de QR que envía alertas a la lista
def iniciar_lector_qr(alertas):
    cap = cv2.VideoCapture(0)
    intentos_fallidos = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Verifica si la cámara no está capturando correctamente

        for barcode in decode(frame):
            data = barcode.data.decode('utf-8')
            alertas.append(f'Datos del QR: {data}')
            
            if data == KEY_WORD:
                alertas.append("Acceso concedido. Puedes entrar.")
                mostrar_alerta_con_voz('src/assets/check.jpg', "Acceso concedido. Puedes entrar.", 'src/assets/sonido_acceso.mp3')
                intentos_fallidos = 0  # Reiniciar los intentos fallidos
            else:
                alertas.append("Código no válido. Por favor, inténtelo de nuevo.")
                mostrar_alerta_con_voz('src/assets/denied.jpg', "Código no válido. Por favor, inténtelo de nuevo.", 'src/assets/sonido_denegado.mp3')
                intentos_fallidos += 1

            if intentos_fallidos >= 5:
                alertas.append("Alerta: Llamando a la policía por múltiples intentos fallidos.")
                mostrar_alerta_con_voz('src/assets/police.jpeg', "Alerta: Llamando a la policía por múltiples intentos fallidos.", 'src/assets/sonido_sirena.mp3')
                intentos_fallidos = 0  # Reinicia el contador después de la alerta

        cv2.imshow('Lector de QR', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    alertas = []
    
    # Crear hilos para la cámara y la ventana de alertas
    hilo_ventana_alertas = threading.Thread(target=iniciar_ventana_alertas, args=(alertas,))
    hilo_lector_qr = threading.Thread(target=iniciar_lector_qr, args=(alertas,))

    # Iniciar los hilos
    hilo_ventana_alertas.start()
    hilo_lector_qr.start()

    # Esperar a que los hilos terminen
    hilo_ventana_alertas.join()
    hilo_lector_qr.join()
