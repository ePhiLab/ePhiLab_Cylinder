from pathlib import Path
import streamlit as st
from PIL import Image

from modules.prediction import build_prediction
from ui.components import app_footer, page_header, section_header
from ui.forms import prediction_form
from ui.results import show_prediction_results

BASE_DIR = Path(__file__).resolve().parents[1]
LOGO_PATH = BASE_DIR / "assets" / "EphiCiencia_Logo.png"
SCHEME_PATH = BASE_DIR / "assets" / "scheme_cylinder.png"

EXCEL_PATH = (
    BASE_DIR
    / "assets"
    / "downloads"
    / "Simulador_Cilindro.xlsx"
)

page_header(
    eyebrow="eΦLab · Módulo 1",
    title="Predicción del movimiento",
    subtitle=(
        "Calcula la aceleración teórica del sistema cilindro–contrapeso "
        "y las componentes rectangulares esperadas en FizziQ."
    ),
    logo_path=LOGO_PATH,
)

# ======================================================
# DESCARGA DEL SIMULADOR ORIGINAL EN EXCEL
# ======================================================

with st.container(border=True):
    download_col, button_col = st.columns(
        [3, 1],
        gap="large",
        vertical_alignment="center",
    )

    with download_col:
        st.markdown("### Simulador original en Excel")

        st.write(
            "Esta pestaña se basa en el simulador desarrollado originalmente "
            "en Microsoft Excel. Puede descargarlo para revisar las ecuaciones, "
            "comparar los resultados o utilizarlo como recurso complementario."
        )

    with button_col:
        if EXCEL_PATH.exists():
            with EXCEL_PATH.open("rb") as excel_file:
                st.download_button(
                    label="Descargar Excel",
                    data=excel_file.read(),
                    file_name="Simulador_Cilindro.xlsx",
                    mime=(
                        "application/vnd.openxmlformats-officedocument."
                        "spreadsheetml.sheet"
                    ),
                    type="primary",
                    use_container_width=True,
                )
        else:
            st.warning(
                "El archivo Excel todavía no está disponible."
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
                caption="Sistema cilindro–contrapeso en una rampa inclinada",
                use_container_width=True,
            )
        else:
            st.info("Añada `assets/scheme_cylinder.png`.")

    with model_col:
        st.markdown("#### Modelo matemático")
        st.latex(
            r"""
            a =
            \frac{
                g\left[m_1-(M+Nm)\sin(\theta)\right]
            }{
                \frac{3M}{2}
                +Nm\left(1+\frac{r_x^2}{R^2}\right)
                +m_1
            }
            """
        )

section_header(
    "1. Parámetros experimentales",
    "Ingrese los valores medidos antes de realizar la experiencia.",
)

parameters = prediction_form()

if parameters is None:
    st.info("Complete los datos y presione **Calcular predicción**.")
else:
    try:
        prediction = build_prediction(parameters)
        show_prediction_results(prediction)
    except ValueError as error:
        st.error(str(error))

app_footer()
