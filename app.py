from pathlib import Path

import streamlit as st

from ui.components import (
    callout,
    feature_card,
    footer,
    hero_header,
    section_header,
)
from ui.theme import apply_theme


st.set_page_config(
    page_title="eΦLab: Cilindro",
    page_icon="🐢",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_theme()

BASE_DIR = Path(__file__).resolve().parent
LOGO_PATH = BASE_DIR / "assets" / "EphiCiencia_Logo.png"

hero_header(
    eyebrow="eΦLab · Laboratorio digital",
    title="Movimiento del cilindro",
    subtitle=(
        "Aplicación educativa para predecir el movimiento, analizar datos "
        "experimentales y comparar resultados obtenidos mediante FizziQ."
    ),
    logo_path=LOGO_PATH,
)

callout(
    "Esta versión establece la identidad visual y la estructura general de la app. "
    "Los módulos experimentales se incorporarán progresivamente."
)

section_header(
    "Módulos de la aplicación",
    "La plataforma se organizará en herramientas independientes y conectadas.",
)

col1, col2 = st.columns(2, gap="large")

with col1:
    feature_card(
        icon="⚙️",
        title="Predicción del movimiento",
        text=(
            "Calcula la aceleración teórica del sistema cilindro–contrapeso "
            "y predice el sentido del movimiento."
        ),
        badge="Primer módulo",
    )

with col2:
    feature_card(
        icon="📈",
        title="Análisis de datos FizziQ",
        text=(
            "Importa archivos CSV, permite seleccionar variables y aplica "
            "ajustes lineales, cuadráticos, cúbicos y exponenciales."
        ),
        badge="Próximamente",
    )

section_header(
    "Objetivo educativo",
    "La aplicación complementa el trabajo experimental, sin reemplazarlo.",
)

st.write(
    """
    eΦLab busca facilitar la preparación de la experiencia, el análisis de datos
    y la interpretación de resultados. Los estudiantes continuarán realizando
    el montaje, la medición y la discusión colaborativa de la práctica.
    """
)

footer()

