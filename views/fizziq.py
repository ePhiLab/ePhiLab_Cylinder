from pathlib import Path
import streamlit as st
from ui.components import app_footer, page_header, section_header

BASE_DIR = Path(__file__).resolve().parents[1]
LOGO_PATH = BASE_DIR / "assets" / "EphiCiencia_Logo.png"

page_header(
    eyebrow="eΦLab",
    title="Acerca de la plataforma",
    subtitle=(
        "Herramientas digitales para acompañar experiencias "
        "de aprendizaje activo en ciencias."
    ),
    logo_path=LOGO_PATH,
)

section_header("Alcance")
st.write(
    """
    eΦLab apoya la predicción física, el análisis de datos y la comparación
    entre resultados teóricos y experimentales.
    """
)

section_header("Versión")
st.code("0.1.0 — Framework visual y navegación", language=None)

app_footer()

