import tkinter as tk
from tkinter import ttk, messagebox
from modelos.vehiculo import Vehiculo


class GarajeApp:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio
        self.root.title("Sistema de Gestión de Garaje")
        self.root.geometry("500x450")

        # --- Formulario ---
        frame_form = tk.LabelFrame(self.root, text="Registro de Vehículo", padx=10, pady=10)
        frame_form.pack(fill="x", padx=20, pady=10)

        tk.Label(frame_form, text="Placa:").grid(row=0, column=0, sticky="w")
        self.ent_placa = tk.Entry(frame_form)
        self.ent_placa.grid(row=0, column=1, pady=5)

        tk.Label(frame_form, text="Marca:").grid(row=1, column=0, sticky="w")
        self.ent_marca = tk.Entry(frame_form)
        self.ent_marca.grid(row=1, column=1, pady=5)

        tk.Label(frame_form, text="Propietario:").grid(row=2, column=0, sticky="w")
        self.ent_propietario = tk.Entry(frame_form)
        self.ent_propietario.grid(row=2, column=1, pady=5)

        # --- Botones ---
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        self.btn_agregar = tk.Button(btn_frame, text="Agregar Vehículo", command=self.agregar, bg="#4CAF50", fg="white")
        self.btn_agregar.pack(side="left", padx=5)

        self.btn_limpiar = tk.Button(btn_frame, text="Limpiar Campos", command=self.limpiar_campos)
        self.btn_limpiar.pack(side="left", padx=5)

        # --- Tabla (Treeview) ---
        self.tabla = ttk.Treeview(self.root, columns=("Placa", "Marca", "Propietario"), show="headings")
        self.tabla.heading("Placa", text="Placa")
        self.tabla.heading("Marca", text="Marca")
        self.tabla.heading("Propietario", text="Propietario")
        self.tabla.column("Placa", width=100)
        self.tabla.pack(fill="both", expand=True, padx=20, pady=10)

    def agregar(self):
        placa = self.ent_placa.get()
        marca = self.ent_marca.get()
        propietario = self.ent_propietario.get()

        if placa and marca and propietario:
            nuevo_v = Vehiculo(placa, marca, propietario)
            self.servicio.registrar_vehiculo(nuevo_v)
            self.actualizar_tabla()
            self.limpiar_campos()
        else:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")

    def actualizar_tabla(self):
        # Limpiar tabla actual
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Cargar datos del servicio
        for v in self.servicio.obtener_vehiculos():
            self.tabla.insert("", "end", values=(v.placa, v.marca, v.propietario))

    def limpiar_campos(self):
        self.ent_placa.delete(0, tk.END)
        self.ent_marca.delete(0, tk.END)
        self.ent_propietario.delete(0, tk.END)