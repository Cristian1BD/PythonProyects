import streamlit as st
import pandas as pd 
import io

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

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

@st.cache_data
def cargar_datos():
    return pd.read_csv("static\datasets\estudiantes_colombia.csv")

df = cargar_datos()

# Título de la app
st.title("📊 Análisis de Estudiantes en Colombia")

# Mostrar primeras y últimas filas
st.header("🔍 Vista del Dataset")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Primeras 5 filas")
    st.dataframe(df.head())

with col2:
    st.subheader("Últimas 5 filas")
    st.dataframe(df.tail())

# Mostrar info y describe
st.header("📋 Resumen del Dataset")

st.subheader("Información general (.info())")
# Capturamos la salida de df.info() como texto
buffer = io.StringIO()
df.info(buf=buffer)
info_str = buffer.getvalue()
st.text(info_str)

st.subheader("Estadísticas descriptivas (.describe())")
st.dataframe(df.describe())

# Selección de columnas
st.header("📌 Selecciona columnas para mostrar")
columnas_disponibles = df.columns.tolist()
columnas_seleccionadas = st.multiselect("Selecciona las columnas:", columnas_disponibles, default=["nombre", "edad", "promedio"])

st.dataframe(df[columnas_seleccionadas])

# Filtro por promedio
st.header("🎯 Filtrar estudiantes por promedio")
promedio_min = st.slider("Selecciona el promedio mínimo:", min_value=0.0, max_value=5.0, step=0.1, value=4.0)

df_filtrado = df[df["promedio"] >= promedio_min]
st.subheader(f"Estudiantes con promedio mayor o igual a {promedio_min}")
st.dataframe(df_filtrado)

# Footer
st.markdown("---")
st.caption("Actividad práctica - Módulo 2")
#

