from src.components.QRGenerator import generar_qr
from src.components.CameraReader import iniciar_lector_qr, iniciar_ventana_alertas
import threading

def main():
    # Generar el código QR al inicio del programa
    generar_qr()

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

if __name__ == "__main__":
    main()
