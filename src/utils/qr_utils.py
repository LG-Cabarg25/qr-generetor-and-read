### src/utils/qr_utils.py
import qrcode

def generar_qr_con_configuracion(data, filename='../assets/codigo_qr_configurado.png', box_size=10, border=4):
    """Genera un código QR con configuraciones personalizadas y lo guarda como un archivo PNG."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f'Código QR con configuración guardado como {filename}')

if __name__ == "__main__":
    generar_qr_con_configuracion("Prueba de QR personalizado")
