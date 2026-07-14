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
        "Aplicación educativa para predecir el movimiento, "
        "analizar datos experimentales y comparar resultados "
        "obtenidos mediante FizziQ."
    ),
    logo_path=LOGO_PATH,
)


callout(
    "La plataforma complementa el trabajo experimental, "
    "el análisis de video y la interpretación física de los resultados."
)


section_header(
    "Módulos de la aplicación",
    "Seleccione una herramienta desde el menú lateral.",
)


module_col1, module_col2 = st.columns(
    2,
    gap="large",
)

with module_col1:
    feature_card(
        icon="⚙️",
        title="Predicción del movimiento",
        text=(
            "Calcula la aceleración teórica del sistema "
            "cilindro–contrapeso y predice el sentido del movimiento."
        ),
        badge="Módulo disponible",
    )

with module_col2:
    feature_card(
        icon="📈",
        title="Análisis de datos FizziQ",
        text=(
            "Importará archivos CSV y permitirá aplicar ajustes "
            "lineales, cuadráticos, cúbicos y exponenciales."
        ),
        badge="Próximamente",
    )


section_header(
    "Objetivo educativo",
    "La aplicación apoya la experiencia, pero no reemplaza el trabajo experimental.",
)

st.write(
    """
    eΦLab facilita la predicción, el procesamiento de datos y la comparación
    entre el modelo teórico y los resultados experimentales. Los estudiantes
    continúan realizando el montaje, la medición y la discusión colaborativa
    de la práctica.
    """
)

footer()
