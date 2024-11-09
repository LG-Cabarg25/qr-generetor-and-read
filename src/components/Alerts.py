### src/components/Alerts.py
from tkinter import messagebox, Tk

def mostrar_alerta(mensaje):
    """Muestra una alerta de mensaje en una ventana emergente."""
    root = Tk()
    root.withdraw()  # Ocultar la ventana principal
    messagebox.showinfo("Alerta", mensaje)
    root.destroy()

if __name__ == "__main__":
    mostrar_alerta("Este es un mensaje de prueba.")
