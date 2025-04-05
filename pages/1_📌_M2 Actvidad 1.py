import streamlit as st
import pandas as pd
import numpy as np
import sqlite3

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")


st.title("📘 Actividad 1 - Creación de DataFrames")
st.markdown("En esta actividad exploramos diferentes formas de crear y mostrar DataFrames con Pandas y Streamlit.")

# 1. Diccionario
st.header("📚 DataFrame de Libros (desde diccionario)")
libros_dict = {
    "título": ["Cien Años de Soledad", "El Principito", "1984", "Rayuela"],
    "autor": ["Gabriel García Márquez", "Antoine de Saint-Exupéry", "George Orwell", "Julio Cortázar"],
    "año de publicación": [1967, 1943, 1949, 1963],
    "género": ["Realismo mágico", "Fábula", "Distopía", "Narrativa"]
}
df_libros = pd.DataFrame(libros_dict)
st.dataframe(df_libros)

# 2. Lista de diccionarios
st.header("🏙️ Información de Ciudades (desde lista de diccionarios)")
ciudades = [
    {"nombre": "Bogotá", "población": 8000000, "país": "Colombia"},
    {"nombre": "Buenos Aires", "población": 3000000, "país": "Argentina"},
    {"nombre": "Lima", "población": 9000000, "país": "Perú"}
]
df_ciudades = pd.DataFrame(ciudades)
st.dataframe(df_ciudades)

# 3. Lista de listas
st.header("🏪 Productos en Inventario (desde lista de listas)")
productos = [
    ["Laptop", 3000, 10],
    ["Mouse", 25, 100],
    ["Teclado", 50, 50]
]
df_productos = pd.DataFrame(productos, columns=["Producto", "Precio", "Stock"])
st.dataframe(df_productos)

# 4. Series
st.header("👥 Datos de Personas (desde Series)")
nombres = pd.Series(["Ana", "Luis", "María", "Jorge"])
edades = pd.Series([25, 30, 28, 22])
ciudades = pd.Series(["Bogotá", "Medellín", "Cali", "Barranquilla"])
df_personas = pd.DataFrame({"nombre": nombres, "edad": edades, "ciudad": ciudades})
st.dataframe(df_personas)

# 5. Archivo CSV local
st.header("🗃️ Datos desde CSV")
try:
    df_csv = pd.read_csv("static/datasets/data.csv")
    st.dataframe(df_csv)
except FileNotFoundError:
    st.warning("⚠️ El archivo 'data.csv' no se encuentra en el directorio del proyecto.")

# 6. Archivo Excel local
st.header("📊 Datos desde Excel")
try:
    df_excel = pd.read_excel("static/datasets/data.xlsx", engine="openpyxl")
    st.dataframe(df_excel)
except FileNotFoundError:
    st.warning("⚠️ El archivo 'data.xlsx' no se encuentra en el directorio del proyecto.")
except ImportError:
    st.error("❌ Falta el módulo 'openpyxl'. Instálalo con `pip install openpyxl`.")

# 7. Archivo JSON local
st.header("📁 Datos de Usuarios desde JSON")
try:
    df_json = pd.read_json("static/datasets/data.json")
    st.dataframe(df_json)
except FileNotFoundError:
    st.warning("⚠️ El archivo 'data.json' no se encuentra en el directorio del proyecto.")

# 8. Datos desde URL (CSV en línea)
st.header("🌐 Datos desde URL")
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"
try:
    df_url = pd.read_csv(url)
    st.dataframe(df_url)
except Exception as e:
    st.error(f"❌ Error al cargar CSV desde URL: {e}")

# 9. Base de datos SQLite
st.header("🗄️ Datos desde SQLite")
try:
    conn = sqlite3.connect("estudiantes.db")
    conn.execute("CREATE TABLE IF NOT EXISTS estudiantes (nombre TEXT, calificación REAL)")
    conn.execute("DELETE FROM estudiantes")  # Limpiar por si acaso
    conn.executemany("INSERT INTO estudiantes VALUES (?, ?)", [
        ("Carlos", 4.5),
        ("Lucía", 3.9),
        ("Andrés", 4.2)
    ])
    conn.commit()
    df_sqlite = pd.read_sql("SELECT * FROM estudiantes", conn)
    st.dataframe(df_sqlite)
except Exception as e:
    st.error(f"❌ Error con SQLite: {e}")
finally:
    conn.close()

# 10. Array de NumPy
st.header("🔢 Datos desde NumPy")
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
df_numpy = pd.DataFrame(arr, columns=["Columna A", "Columna B", "Columna C"])
st.dataframe(df_numpy)

# 11. Firebase y 12. MongoDB no se implementan por defecto
st.header("🌩️ Firebase y MongoDB")
st.info("La conexión a Firebase o MongoDB requiere configuración avanzada y acceso a servicios externos, no incluidos en esta actividad.")

# Footer
st.markdown("---")
st.caption("Módulo 2 - Actividad 1 | Streamlit + Pandas")
