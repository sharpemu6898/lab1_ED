interfaz py
import tkinter as tk
from tkinter import messagebox, simpledialog

# --- Código original para gestionar películas, clientes y compras ---
indexadoPeliculas = {}
indexadoClientes = {}
indexadoCompras = {}

# Manejo de archivos
def cargarDatos():
    try:
        with open("archivoPeliculas.txt", "r") as archivo:
            contenido = archivo.readlines()
            for linea in contenido:
                linea = linea.replace("\n", "")
                pelicula = linea.split(";")
                id = pelicula[0]
                indexadoPeliculas[id] = linea
    except FileNotFoundError:
        with open("archivoPeliculas.txt", "w") as archivo:
            pass

    try:
        with open("archivoClientes.txt", "r") as archivo:
            contenido = archivo.readlines()
            for linea in contenido:
                linea = linea.replace("\n", "")
                cliente = linea.split(";")
                indexadoClientes[cliente[0]] = linea
    except FileNotFoundError:
        with open("archivoClientes.txt", "w") as archivo:
            pass

    try:
        with open("archivoCompras.txt", "r") as archivo:
            contenido = archivo.readlines()
            for linea in contenido:
                linea = linea.replace("\n", "")
                compra = linea.split(";")
                indexadoCompras[compra[0]] = linea
    except FileNotFoundError:
        with open("archivoCompras.txt", "w") as archivo:
            pass

# Funciones de la lógica
def buscarPorID(id):
    return indexadoPeliculas.get(id, "No se encontró la película.")

def buscarPorGenero(genero):
    return [pelicula for pelicula in indexadoPeliculas.values() if pelicula.split(";")[4] == genero]

def buscarPorDirector(director):
    return [pelicula for pelicula in indexadoPeliculas.values() if pelicula.split(";")[2] == director]

def buscarPorCliente(id):
    return [compra for compra in indexadoCompras.values() if compra.split(";")[1] == id]

def idClienteExiste(id):
    return id in indexadoClientes

def realizarCompra(idCompra, idCliente, idPelicula, fecha):
    if idClienteExiste(idCliente):
        if idCompra not in indexadoCompras:
            compra = f"{idCompra};{idCliente};{idPelicula};{fecha}"
            indexadoCompras[idCompra] = compra
            with open("archivoCompras.txt", "a") as archivo:
                archivo.write(f"{compra}\n")
            return "Compra realizada con éxito."
        else:
            return "El ID de compra ya está registrado."
    else:
        return "El cliente no se encuentra registrado."

def agregarPelicula(idPelicula, titulo, director, anio, genero, precio):
    if idPelicula not in indexadoPeliculas:
        pelicula = f"{idPelicula};{titulo};{director};{anio};{genero};{precio}"
        indexadoPeliculas[idPelicula] = pelicula
        with open("archivoPeliculas.txt", "a") as archivo:
            archivo.write(f"{pelicula}\n")
        return "Película agregada correctamente."
    else:
        return "La película ya fue registrada."

def agregarCliente(idCliente, nombre, correo, direccion):
    if idCliente not in indexadoClientes:
        cliente = f"{idCliente};{nombre};{correo};{direccion}"
        indexadoClientes[idCliente] = cliente
        with open("archivoClientes.txt", "a") as archivo:
            archivo.write(f"{cliente}\n")
        return "Cliente agregado correctamente."
    else:
        return "El ID del cliente ya existe."

def modificarPelicula(idEncontrar, idPelicula, titulo, director, anio, genero, precio):
    if idEncontrar in indexadoPeliculas:
        pelicula = indexadoPeliculas[idEncontrar].split(";")
        if idPelicula:
            pelicula[0] = idPelicula
        if titulo:
            pelicula[1] = titulo
        if director:
            pelicula[2] = director
        if anio:
            pelicula[3] = anio
        if genero:
            pelicula[4] = genero
        if precio:
            pelicula[5] = precio
        peliculaUnida = ";".join(pelicula)
        indexadoPeliculas[idEncontrar] = peliculaUnida

        with open("archivoPeliculas.txt", "w") as archivo:
            for p in indexadoPeliculas.values():
                archivo.write(f"{p}\n")
        return "Película modificada correctamente."
    else:
        return "Película no encontrada."

def eliminarPelicula(idPelicula):
    if idPelicula in indexadoPeliculas:
        del indexadoPeliculas[idPelicula]
        with open("archivoPeliculas.txt", "w") as archivo:
            for pelicula in indexadoPeliculas.values():
                archivo.write(f"{pelicula}\n")
        return "Película eliminada correctamente."
    else:
        return "Película no encontrada."

# ---- A partir de aquí, añado la interfaz de usuario y los reportes ----

import tkinter as tk
from tkinter import messagebox, simpledialog
import matplotlib.pyplot as plt
from datetime import datetime

# Función para mostrar mensajes consolidados
def mostrarMensaje(mensaje, es_error=False):
    if es_error:
        messagebox.showerror("Error", mensaje)
    else:
        messagebox.showinfo("Resultado", mensaje)

# Función para agregar película desde la interfaz
def agregarPeliculaGUI():
    idPelicula = idPeliculaEntry.get()
    titulo = tituloEntry.get()
    director = directorEntry.get()
    anio = anioEntry.get()
    genero = generoEntry.get()
    precio = precioEntry.get()
    
    mensaje = agregarPelicula(idPelicula, titulo, director, anio, genero, precio)
    mostrarMensaje(mensaje, es_error=("ya fue registrada" in mensaje))

# Función para buscar película por ID y mostrar en un mensaje
def buscarPeliculaGUI():
    idPelicula = buscarPeliculaIDEntry.get()
    pelicula = buscarPorID(idPelicula)
    
    if pelicula != "No se encontró la película.":
        mostrarMensaje(f"Película encontrada:\n{pelicula}")
    else:
        mostrarMensaje("Película no encontrada.", es_error=True)

# Función para agregar cliente desde la interfaz
def agregarClienteGUI():
    idCliente = idClienteEntry.get()
    nombre = nombreEntry.get()
    apellido = apellidoEntry.get()
    celular = celularEntry.get()
    direccion = direccionEntry.get()
    correo = correoEntry.get()
    
    mensaje = agregarCliente(idCliente, nombre, correo, direccion)
    mostrarMensaje(mensaje, es_error=("ya existe" in mensaje))

# Función para realizar una compra desde la interfaz
def realizarCompraGUI():
    idCompra = idCompraEntry.get()
    idCliente = idClienteCompraEntry.get()
    idPelicula = idPeliculaCompraEntry.get()
    fecha = fechaEntry.get()
    
    mensaje = realizarCompra(idCompra, idCliente, idPelicula, fecha)
    mostrarMensaje(mensaje, es_error=("El" in mensaje and "registrado" in mensaje))

# Función para mostrar el reporte de las películas más vendidas
def peliculasMasVendidas():
    # Aquí deberías implementar la lógica para contar y mostrar las películas más vendidas
    mostrarMensaje("Este reporte mostrará las películas más vendidas.")

# Función para mostrar el reporte de los clientes con más compras
def clientesConMasCompras():
    # Aquí deberías implementar la lógica para contar y mostrar los clientes con más compras
    mostrarMensaje("Este reporte mostrará los clientes con más compras.")

# Función para mostrar el reporte de ventas por intervalos de tiempo
def ventasPorIntervaloTiempo():
    # Aquí deberías implementar la lógica para mostrar las ventas por intervalo de tiempo
    mostrarMensaje("Este reporte mostrará las ventas por intervalo de tiempo.")

# Configuración de la interfaz gráfica con Tkinter
ventana = tk.Tk()
ventana.title("Gestión de Películas")

# Gestión de Películas
tk.Label(ventana, text="Gestión de Películas").grid(row=0, column=0, columnspan=2)

tk.Label(ventana, text="ID Película").grid(row=1, column=0)
idPeliculaEntry = tk.Entry(ventana)
idPeliculaEntry.grid(row=1, column=1)

tk.Label(ventana, text="Título").grid(row=2, column=0)
tituloEntry = tk.Entry(ventana)
tituloEntry.grid(row=2, column=1)

tk.Label(ventana, text="Director").grid(row=3, column=0)
directorEntry = tk.Entry(ventana)
directorEntry.grid(row=3, column=1)

tk.Label(ventana, text="Año").grid(row=4, column=0)
anioEntry = tk.Entry(ventana)
anioEntry.grid(row=4, column=1)

tk.Label(ventana, text="Género").grid(row=5, column=0)
generoEntry = tk.Entry(ventana)
generoEntry.grid(row=5, column=1)

tk.Label(ventana, text="Precio").grid(row=6, column=0)
precioEntry = tk.Entry(ventana)
precioEntry.grid(row=6, column=1)

tk.Button(ventana, text="Agregar Película", command=agregarPeliculaGUI).grid(row=7, column=1)

# Buscar Película
tk.Label(ventana, text="Buscar Película por ID").grid(row=8, column=0)
buscarPeliculaIDEntry = tk.Entry(ventana)
buscarPeliculaIDEntry.grid(row=8, column=1)
tk.Button(ventana, text="Buscar", command=buscarPeliculaGUI).grid(row=9, column=1)

# Gestión de Clientes
tk.Label(ventana, text="Gestión de Clientes").grid(row=10, column=0, columnspan=2)

tk.Label(ventana, text="ID Cliente").grid(row=11, column=0)
idClienteEntry = tk.Entry(ventana)
idClienteEntry.grid(row=11, column=1)

tk.Label(ventana, text="Nombre").grid(row=12, column=0)
nombreEntry = tk.Entry(ventana)
nombreEntry.grid(row=12, column=1)

tk.Label(ventana, text="Apellido").grid(row=13, column=0)
apellidoEntry = tk.Entry(ventana)
apellidoEntry.grid(row=13, column=1)

tk.Label(ventana, text="Celular").grid(row=14, column=0)
celularEntry = tk.Entry(ventana)
celularEntry.grid(row=14, column=1)

tk.Label(ventana, text="Dirección").grid(row=15, column=0)
direccionEntry = tk.Entry(ventana)
direccionEntry.grid(row=15, column=1)

tk.Label(ventana, text="Correo Electrónico").grid(row=16, column=0)
correoEntry = tk.Entry(ventana)
correoEntry.grid(row=16, column=1)

tk.Button(ventana, text="Agregar Cliente", command=agregarClienteGUI).grid(row=17, column=1)

# Gestión de Compras
tk.Label(ventana, text="Gestión de Compras").grid(row=18, column=0, columnspan=2)

tk.Label(ventana, text="ID Compra").grid(row=19, column=0)
idCompraEntry = tk.Entry(ventana)
idCompraEntry.grid(row=19, column=1)

tk.Label(ventana, text="ID Cliente").grid(row=20, column=0)
idClienteCompraEntry = tk.Entry(ventana)
idClienteCompraEntry.grid(row=20, column=1)

tk.Label(ventana, text="ID Película").grid(row=21, column=0)
idPeliculaCompraEntry = tk.Entry(ventana)
idPeliculaCompraEntry.grid(row=21, column=1)

tk.Label(ventana, text="Fecha (YYYY-MM-DD)").grid(row=22, column=0)
fechaEntry = tk.Entry(ventana)
fechaEntry.grid(row=22, column=1)

tk.Button(ventana, text="Realizar Compra", command=realizarCompraGUI).grid(row=23, column=1)

# Generar Reportes
tk.Label(ventana, text="Generar Reportes").grid(row=24, column=0, columnspan=2)

tk.Button(ventana, text="Películas Más Vendidas", command=peliculasMasVendidas).grid(row=25, column=0)
tk.Button(ventana, text="Clientes con Más Compras", command=clientesConMasCompras).grid(row=26, column=0)
tk.Button(ventana, text="Ventas según Intervalos de Tiempo", command=ventasPorIntervaloTiempo).grid(row=27, column=0)

# Ejecutar la ventana
ventana.mainloop()
