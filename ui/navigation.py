from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).resolve().parents[1]

def build_navigation() -> dict[str, list[st.Page]]:
    home = st.Page(
        BASE_DIR / "views" / "home.py",
        title="Inicio",
        icon=":material/home:",
        url_path="inicio",
        default=True,
    )

    prediction = st.Page(
        BASE_DIR / "views" / "prediction.py",
        title="Predicción del movimiento",
        icon=":material/settings_motion_mode:",
        url_path="prediccion",
    )

    fizziq = st.Page(
        BASE_DIR / "views" / "fizziq.py",
        title="Análisis de datos FizziQ",
        icon=":material/query_stats:",
        url_path="fizziq",
    )

    about = st.Page(
        BASE_DIR / "views" / "about.py",
        title="Acerca de eΦLab",
        icon=":material/info:",
        url_path="acerca-de",
    )

    return {
        "Principal": [home],
        "Herramientas": [prediction, fizziq],
        "Información": [about],
    }

def render_sidebar_footer() -> None:
    with st.sidebar:
        st.divider()
        st.caption("eΦCiencia")
        st.caption("Laboratorio digital de experimentación")
        st.caption("Versión 0.1.0")

