from pathlib import Path

import streamlit as st
from PIL import Image

from modules.prediction import build_prediction
from ui.components import (
    footer,
    hero_header,
    section_header,
)
from ui.forms import prediction_form
from ui.results import show_prediction_results
from ui.theme import apply_theme


st.set_page_config(
    page_title="Predicción del movimiento",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_theme()

BASE_DIR = Path(__file__).resolve().parents[1]
LOGO_PATH = BASE_DIR / "assets" / "EphiCiencia_Logo.png"
SCHEME_PATH = BASE_DIR / "assets" / "scheme_cylinder.png"

hero_header(
    eyebrow="eΦLab · Módulo 1",
    title="Predicción del movimiento",
    subtitle=(
        "Calcula la aceleración teórica del sistema cilindro–contrapeso "
        "y las componentes que deberían observarse mediante FizziQ."
    ),
    logo_path=LOGO_PATH,
)

with st.expander("Modelo físico implementado", expanded=False):
    image_col, model_col = st.columns(
        [0.9, 1.35],
        gap="large",
        vertical_alignment="center",
    )

    with image_col:
        st.markdown("#### Esquema experimental")

        if SCHEME_PATH.exists():
            image = Image.open(SCHEME_PATH)
            st.image(
                image,
                caption=(
                    "Sistema cilindro–contrapeso "
                    "en una rampa inclinada"
                ),
                use_container_width=True,
            )
        else:
            st.info(
                "Añada la imagen del montaje en "
                "`assets/scheme_cylinder.png`."
            )

    with model_col:
        st.markdown("#### Modelo matemático")

        st.latex(
            r"""
            a =
            \frac{
                g\left[
                    m_1-(M+Nm)\sin(\theta)
                \right]
            }{
                \frac{3M}{2}
                +Nm\left(
                    1+\frac{r_x^2}{R^2}
                \right)
                +m_1
            }
            """
        )

        st.markdown(
            r"""
            - \(a\): aceleración sobre la rampa.
            - \(g\): aceleración de la gravedad.
            - \(m_1\): masa del contrapeso.
            - \(M\): masa del cilindro.
            - \(N\): número de varillas.
            - \(m\): masa de cada varilla.
            - \(R\): radio externo del cilindro.
            - \(r_x\): radio de ubicación de las varillas.
            - \(\theta\): ángulo de la rampa.
            """
        )

section_header(
    "1. Parámetros experimentales",
    (
        "Ingrese los valores medidos antes de realizar "
        "la experiencia."
    ),
)

parameters = prediction_form()

if parameters is None:
    st.info(
        "Complete o revise los datos y presione "
        "**Calcular predicción**."
    )
else:
    try:
        prediction = build_prediction(parameters)
        show_prediction_results(prediction)

    except ValueError as error:
        st.error(str(error))

footer()

