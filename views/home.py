from pathlib import Path
import streamlit as st
from ui.components import (
    app_footer, callout, module_card, page_header, section_header
)

BASE_DIR = Path(__file__).resolve().parents[1]
LOGO_PATH = BASE_DIR / "assets" / "EphiCiencia_Logo.png"

page_header(
    eyebrow="eΦLab · Laboratorio digital",
    title="Movimiento del cilindro",
    subtitle=(
        "Aplicación educativa para predecir el movimiento, analizar datos "
        "experimentales y comparar resultados obtenidos mediante FizziQ."
    ),
    logo_path=LOGO_PATH,
)

callout("Seleccione una herramienta desde el menú lateral para comenzar.")

section_header(
    "Módulos disponibles",
    "Cada módulo aborda una etapa distinta de la experiencia.",
)

left, right = st.columns(2, gap="large")

with left:
    module_card(
        "⚙️",
        "Predicción del movimiento",
        "Calcula la aceleración teórica y predice el sentido del movimiento.",
        status="Disponible",
    )

with right:
    module_card(
        "📈",
        "Análisis de datos FizziQ",
        "Importa archivos CSV, grafica datos y aplica ajustes matemáticos.",
        status="En desarrollo",
    )

app_footer()

