from pathlib import Path
import streamlit as st
from ui.navigation import build_navigation, render_sidebar_footer
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

if LOGO_PATH.exists():
    st.logo(LOGO_PATH, size="large", icon_image=LOGO_PATH)

render_sidebar_footer()

page = st.navigation(
    build_navigation(),
    position="sidebar",
    expanded=True,
)
page.run()
