import os
import qrcode

# Definir la palabra clave que será codificada en el QR
KEY_WORD = "CASAentrada"

def generar_qr(data=KEY_WORD, filename=None):
    """Genera un código QR con los datos proporcionados y lo guarda como un archivo PNG."""
    if filename is None:
        # Construir la ruta al archivo dentro de la carpeta src/assets
        base_path = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(base_path, '../assets/codigo_qr.png')

    qr = qrcode.make(data)
    qr.save(filename)
    print(f'Código QR generado con la palabra clave "{data}" y guardado como {filename}')

if __name__ == "__main__":
    generar_qr()
