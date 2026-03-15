# Clase que maneja la lógica del garaje
# Aquí se almacenan y gestionan los vehículos registrados

class GarajeServicio:
    def __init__(self):
        self._vehiculos = []

    def registrar_vehiculo(self, vehiculo):
        # Aquí podrías agregar validaciones en el futuro
        self._vehiculos.append(vehiculo)

    def obtener_vehiculos(self):
        return self._vehiculos