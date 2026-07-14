import streamlit as st


PALETTE = {
    "primary": "#32A852",
    "primary_dark": "#247A3A",
    "secondary": "#2F80ED",
    "background": "#0E1117",
    "surface": "#171C24",
    "surface_soft": "#1D2430",
    "text": "#F5F7FA",
    "muted": "#AAB3C2",
    "border": "rgba(255, 255, 255, 0.11)",
}


def apply_theme() -> None:
    """Aplica el estilo visual global de eΦLab."""

    st.markdown(
        f"""
        <style>
            :root {{
                --ephi-primary: {PALETTE["primary"]};
                --ephi-primary-dark: {PALETTE["primary_dark"]};
                --ephi-secondary: {PALETTE["secondary"]};
                --ephi-background: {PALETTE["background"]};
                --ephi-surface: {PALETTE["surface"]};
                --ephi-surface-soft: {PALETTE["surface_soft"]};
                --ephi-text: {PALETTE["text"]};
                --ephi-muted: {PALETTE["muted"]};
                --ephi-border: {PALETTE["border"]};
            }}

            .stApp {{
                background:
                    radial-gradient(
                        circle at 8% 0%,
                        rgba(50, 168, 82, 0.12),
                        transparent 26%
                    ),
                    radial-gradient(
                        circle at 100% 4%,
                        rgba(47, 128, 237, 0.08),
                        transparent 22%
                    ),
                    var(--ephi-background);
            }}

            .block-container {{
                max-width: 1180px;
                padding-top: 1.2rem;
                padding-bottom: 3rem;
            }}

            h1, h2, h3, h4 {{
                letter-spacing: -0.025em;
            }}

            p, li, label {{
                line-height: 1.55;
            }}

            div[data-testid="stVerticalBlockBorderWrapper"] {{
                border-radius: 18px;
            }}

            div[data-testid="stMetric"] {{
                padding: 0.95rem;
                border: 1px solid var(--ephi-border);
                border-radius: 15px;
                background: rgba(23, 28, 36, 0.92);
            }}

            div[data-testid="stMetricLabel"] {{
                color: var(--ephi-muted);
            }}

            div[data-testid="stExpander"] {{
                border: 1px solid var(--ephi-border);
                border-radius: 15px;
                background: rgba(23, 28, 36, 0.70);
                overflow: hidden;
            }}

            div[data-testid="stForm"] {{
                border: 1px solid var(--ephi-border);
                border-radius: 16px;
                background: rgba(23, 28, 36, 0.76);
                padding: 1rem;
            }}

            .stButton > button,
            .stFormSubmitButton > button {{
                min-height: 46px;
                border: none;
                border-radius: 12px;
                background: var(--ephi-primary);
                color: white;
                font-weight: 700;
                transition:
                    transform 0.15s ease,
                    background 0.15s ease;
            }}

            .stButton > button:hover,
            .stFormSubmitButton > button:hover {{
                background: var(--ephi-primary-dark);
                transform: translateY(-1px);
            }}

            div[data-baseweb="input"] > div,
            div[data-baseweb="select"] > div {{
                border-radius: 11px;
            }}

            div[data-testid="stImage"] img {{
                border-radius: 50%;
                object-fit: cover;
            }}

            @media (max-width: 700px) {{
                .block-container {{
                    padding-left: 0.85rem;
                    padding-right: 0.85rem;
                }}

                h1 {{
                    font-size: 1.85rem !important;
                }}
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )
