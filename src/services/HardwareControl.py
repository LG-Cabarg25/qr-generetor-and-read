### src/services/HardwareControl.py
import serial
import time

def enviar_senal_chapa(puerto='COM3', baud_rate=9600, comando='abrir'):
    """Envía una señal al hardware de la chapa mediante comunicación serial."""
    try:
        with serial.Serial(puerto, baud_rate, timeout=1) as arduino:
            print("Conectado al hardware de la chapa.")
            arduino.write(comando.encode())
            time.sleep(1)  # Esperar para asegurar que el comando se envíe
            print(f"Comando '{comando}' enviado correctamente.")
    except serial.SerialException as e:
        print(f"Error de conexión con el hardware: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    enviar_senal_chapa()