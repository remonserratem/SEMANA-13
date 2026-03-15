import tkinter as tk
from servicios.garaje_servicio import GarajeServicio
from ui.app_tkinter import GarajeApp


def main():
    root = tk.Tk()

    # Instanciamos el servicio (Lógica)
    servicio = GarajeServicio()

    # Instanciamos la UI pasándole el servicio (Inyección de dependencias)
    app = GarajeApp(root, servicio)

    root.mainloop()


if __name__ == "__main__":
    main()