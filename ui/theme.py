import streamlit as st

PALETTE = {
    "primary": "#36B45A",
    "primary_dark": "#25843F",
    "secondary": "#3388F0",
    "background": "#0D1117",
    "surface": "#161C25",
    "text": "#F5F7FA",
    "muted": "#AAB4C3",
    "border": "rgba(255,255,255,0.12)",
}

def apply_theme() -> None:
    variables = f"""
    :root {{
        --ephi-primary: {PALETTE["primary"]};
        --ephi-primary-dark: {PALETTE["primary_dark"]};
        --ephi-secondary: {PALETTE["secondary"]};
        --ephi-background: {PALETTE["background"]};
        --ephi-surface: {PALETTE["surface"]};
        --ephi-text: {PALETTE["text"]};
        --ephi-muted: {PALETTE["muted"]};
        --ephi-border: {PALETTE["border"]};
    }}
    """

    styles = """
    .stApp {
        background:
            radial-gradient(circle at 8% 0%, rgba(54,180,90,.11), transparent 26%),
            radial-gradient(circle at 100% 4%, rgba(51,136,240,.08), transparent 22%),
            var(--ephi-background);
    }

    .block-container {
        max-width: 1180px;
        padding-top: 1.35rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3, h4 {
        letter-spacing: -0.025em;
    }

    p, li, label {
        line-height: 1.55;
    }

    [data-testid="stSidebar"] {
        border-right: 1px solid var(--ephi-border);
        background:
            linear-gradient(180deg, rgba(54,180,90,.07), rgba(13,17,23,0)),
            #111720;
    }

    [data-testid="stSidebarNav"] a {
        border-radius: 10px;
        margin: .12rem .4rem;
    }

    [data-testid="stSidebarNav"] a:hover {
        background: rgba(54,180,90,.10);
    }

    div[data-testid="stMetric"] {
        min-height: 118px;
        padding: .95rem;
        border: 1px solid var(--ephi-border);
        border-radius: 15px;
        background: rgba(22,28,37,.92);
        box-shadow: 0 8px 20px rgba(0,0,0,.10);
    }

    div[data-testid="stExpander"] {
        border: 1px solid var(--ephi-border);
        border-radius: 15px;
        background: rgba(22,28,37,.72);
        overflow: hidden;
    }

    div[data-testid="stForm"] {
        padding: 1rem;
        border: 1px solid var(--ephi-border);
        border-radius: 16px;
        background: rgba(22,28,37,.76);
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-color: var(--ephi-border);
        border-radius: 16px;
        background: rgba(22,28,37,.72);
    }

    .stButton > button,
    .stFormSubmitButton > button {
        min-height: 46px;
        border: none;
        border-radius: 12px;
        background: var(--ephi-primary);
        color: white;
        font-weight: 700;
    }

    .stButton > button:hover,
    .stFormSubmitButton > button:hover {
        background: var(--ephi-primary-dark);
        transform: translateY(-1px);
    }

    div[data-testid="stImage"] img {
        border-radius: 12px;
        object-fit: contain;
    }

    @media (max-width: 700px) {
        .block-container {
            padding-left: .85rem;
            padding-right: .85rem;
        }

        h1 {
            font-size: 1.85rem !important;
        }

        div[data-testid="stMetric"] {
            min-height: auto;
        }
    }
    """

    st.markdown(
        f"<style>{variables}{styles}</style>",
        unsafe_allow_html=True,
    )
