### README.md

# Proyecto de Generación y Lectura de Códigos QR

## Descripción

Este proyecto permite la generación y lectura de códigos QR utilizando Python. La aplicación incluye:

- Generación de códigos QR personalizados.
- Lectura de códigos QR a través de la cámara de la PC.
- Alertas de acceso y manejo de múltiples intentos fallidos.
- (Opcional) Comunicación con hardware externo para controlar dispositivos como chapas electrónicas.

## Estructura del Proyecto

```
proyecto-qr/
│
├── main.py                  # Archivo principal de ejecución
├── requirements.txt         # Lista de dependencias
├── .gitignore               # Archivos y carpetas a ignorar
├── README.md                # Documentación del proyecto
│
└── src/
    ├── assets/              # Archivos de imágenes generadas
    ├── components/          # Módulos de generación y lectura de QR, alertas
    ├── services/            # Lógica de control de hardware (comentada para pruebas)
    ├── utils/               # Funciones auxiliares para manejo de QR
    └── styles/              # Archivos de estilo (si se usan)
```

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/proyecto-qr.git
   cd proyecto-qr
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Ejecuta `main.py` para iniciar la aplicación:
   ```bash
   python main.py
   ```
2. Sigue las instrucciones en la consola y utiliza la cámara para escanear los códigos QR.

## Dependencias

- `qrcode[pil]`
- `opencv-python`
- `pyzbar`
- `tkinter` (incluido en Python)
- `pyserial` (opcional, para comunicación con hardware)

## Notas

- El módulo `HardwareControl.py` está comentado por defecto y debe ser habilitado si se va a probar con hardware externo.
- Los archivos generados se guardan en la carpeta `assets/`.

## Licencia

Este proyecto se distribuye bajo la Licencia MIT.
