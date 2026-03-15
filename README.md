# Sistema de Gestion de Garaje

Este proyecto consiste en una aplicacion de escritorio desarrollada en Python utilizando la libreria Tkinter. El sistema permite el registro y visualizacion de vehiculos en un garaje, aplicando una arquitectura modular.

## Informacion del Estudiante
* **Nombre:** Roxana Estefania Monserrate Miño
* **Materia:** Programacion Orientada a Objetos (POO)
* **Nivel:** 2do Nivel

---

## Arquitectura del Proyecto
El sistema se ha organizado siguiendo el patron de diseño modular para separar las responsabilidades del programa:

* **modelos/**: Contiene la clase Vehiculo, que define la estructura de los datos (Placa, Marca, Propietario).
* **servicios/**: Contiene la logica de negocio (GarajeServicio), encargada de gestionar la lista de vehiculos de forma independiente a la interfaz.
* **ui/**: Maneja la interfaz grafica de usuario con Tkinter, permitiendo la interaccion y visualizacion de datos en una tabla (Treeview).
* **main.py**: El punto de entrada principal que inicia la ejecucion del programa.

---

## Requisitos y Ejecucion

### Requisitos
- Python 3.x
- Libreria Tkinter

### Instalacion y Uso
1. Clonar el repositorio:
   git clone https://github.com/remonserratem/SEMANA-13.git
   
2. Navegar a la carpeta del proyecto:
   cd SEMANA-13
   
3. Ejecutar la aplicacion:
   python main.py

---

## Funcionalidades
- Registro de vehiculos (Placa, Marca, Propietario).
- Visualizacion de datos en una tabla organizada.
- Limpieza de campos del formulario.
- Estructura de codigo basada en clases y objetos.
