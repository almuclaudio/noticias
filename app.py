import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Datos base
empresas = ['KPMG', 'EY', 'Deloitte', 'Accenture']
menciones = [2, 2, 1, 1]

actividades = {
    'Auditoría': [0, 2, 0, 0],
    'Consultoría tecnológica': [1, 0, 0, 1],
    'Informes sectoriales / económicos': [1, 0, 1, 0],
    'IA / Digitalización avanzada': [1, 0, 0, 1]
}

# Título principal
st.title("Análisis de Consultoras en Noticias de Transformación Digital")

# Menciones por firma
st.header("Menciones por Firma")
fig1, ax1 = plt.subplots()
ax1.bar(empresas, menciones, color='skyblue')
ax1.set_ylabel('Frecuencia')
ax1.set_title('Número de menciones en noticias analizadas')
ax1.grid(axis='y')
st.pyplot(fig1)

# Actividad por firma
st.header("Tipo de Actividad Mencionada")
x = range(len(empresas))
bar_width = 0.2
fig2, ax2 = plt.subplots(figsize=(9, 5))

for i, (actividad, valores) in enumerate(actividades.items()):
    ax2.bar([p + i * bar_width for p in x], valores, bar_width, label=actividad)

ax2.set_xticks([p + 1.5 * bar_width for p in x])
ax2.set_xticklabels(empresas)
ax2.set_ylabel('Número de menciones')
ax2.set_title('Tipo de actividad mencionada por firma')
ax2.legend()
ax2.grid(axis='y')
st.pyplot(fig2)

# Comentario final
st.markdown("""
Esta aplicación permite comparar la participación de grandes consultoras en noticias sobre transformación digital,
IA, y auditoría, según su representación explícita en medios recientes. Puedes ampliar el análisis incluyendo más firmas o
cargando nuevas fuentes.
""")
