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
    "border": "rgba(255,255,255,0.11)",
    "warning": "#F4B942",
    "danger": "#E25555",
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
                        circle at 10% 0%,
                        rgba(50, 168, 82, 0.12),
                        transparent 28%
                    ),
                    radial-gradient(
                        circle at 100% 5%,
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
                color: var(--ephi-text);
                letter-spacing: -0.025em;
            }}

            p, li, label {{
                line-height: 1.55;
            }}

            .ephi-hero {{
                display: flex;
                align-items: center;
                gap: 1.15rem;
                padding: 1.15rem 1.25rem;
                margin-bottom: 1.25rem;
                border: 1px solid var(--ephi-border);
                border-radius: 20px;
                background:
                    linear-gradient(
                        135deg,
                        rgba(50, 168, 82, 0.16),
                        rgba(47, 128, 237, 0.08)
                    );
                box-shadow: 0 14px 34px rgba(0,0,0,0.18);
            }}

            .ephi-logo {{
                width: 92px;
                height: 92px;
                border-radius: 50%;
                object-fit: cover;
                border: 3px solid rgba(255,255,255,0.9);
                box-shadow: 0 8px 20px rgba(0,0,0,0.32);
                flex-shrink: 0;
            }}

            .ephi-title {{
                margin: 0;
                font-size: clamp(2rem, 4vw, 3.25rem);
                font-weight: 780;
            }}

            .ephi-subtitle {{
                margin: 0.3rem 0 0 0;
                color: var(--ephi-muted);
                font-size: 1.02rem;
                max-width: 800px;
            }}

            .ephi-eyebrow {{
                display: inline-block;
                margin-bottom: 0.3rem;
                color: var(--ephi-primary);
                font-size: 0.82rem;
                font-weight: 800;
                text-transform: uppercase;
                letter-spacing: 0.12em;
            }}

            .ephi-section-header {{
                margin-top: 1.1rem;
                margin-bottom: 0.8rem;
            }}

            .ephi-section-title {{
                margin: 0;
                font-size: 1.35rem;
                font-weight: 760;
            }}

            .ephi-section-description {{
                margin: 0.2rem 0 0 0;
                color: var(--ephi-muted);
            }}

            .ephi-card {{
                height: 100%;
                padding: 1.15rem;
                border: 1px solid var(--ephi-border);
                border-radius: 17px;
                background: rgba(23, 28, 36, 0.88);
                box-shadow: 0 8px 20px rgba(0,0,0,0.10);
            }}

            .ephi-card-icon {{
                font-size: 1.65rem;
                margin-bottom: 0.45rem;
            }}

            .ephi-card-title {{
                margin: 0 0 0.35rem 0;
                font-size: 1.08rem;
                font-weight: 760;
            }}

            .ephi-card-text {{
                margin: 0;
                color: var(--ephi-muted);
            }}

            .ephi-badge {{
                display: inline-block;
                margin-top: 0.75rem;
                padding: 0.28rem 0.62rem;
                border-radius: 999px;
                background: rgba(50,168,82,0.14);
                color: var(--ephi-primary);
                font-size: 0.78rem;
                font-weight: 750;
            }}

            .ephi-callout {{
                padding: 1rem 1.1rem;
                border: 1px solid var(--ephi-border);
                border-left: 5px solid var(--ephi-primary);
                border-radius: 14px;
                background: rgba(29, 36, 48, 0.82);
                color: var(--ephi-text);
            }}

            .ephi-footer {{
                margin-top: 2rem;
                padding-top: 1rem;
                border-top: 1px solid var(--ephi-border);
                color: var(--ephi-muted);
                font-size: 0.86rem;
                text-align: center;
            }}

            div[data-testid="stMetric"] {{
                padding: 0.95rem;
                border: 1px solid var(--ephi-border);
                border-radius: 15px;
                background: rgba(23, 28, 36, 0.9);
            }}

            div[data-testid="stExpander"] {{
                border: 1px solid var(--ephi-border);
                border-radius: 15px;
                background: rgba(23, 28, 36, 0.68);
                overflow: hidden;
            }}

            div[data-testid="stForm"] {{
                border: 1px solid var(--ephi-border);
                border-radius: 16px;
                background: rgba(23, 28, 36, 0.72);
                padding: 1rem;
            }}

            .stButton > button,
            .stFormSubmitButton > button {{
                min-height: 46px;
                border: none;
                border-radius: 12px;
                background: var(--ephi-primary);
                color: white;
                font-weight: 760;
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

            @media (max-width: 700px) {{
                .block-container {{
                    padding-left: 0.85rem;
                    padding-right: 0.85rem;
                }}

                .ephi-hero {{
                    align-items: flex-start;
                    padding: 0.95rem;
                    gap: 0.8rem;
                }}

                .ephi-logo {{
                    width: 68px;
                    height: 68px;
                }}

                .ephi-title {{
                    font-size: 1.8rem;
                }}

                .ephi-subtitle {{
                    font-size: 0.92rem;
                }}
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

