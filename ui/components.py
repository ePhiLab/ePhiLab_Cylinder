import base64
import html
from pathlib import Path

import streamlit as st


def _encode_image(image_path: str | Path) -> str:
    path = Path(image_path)
    with path.open("rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def hero_header(
    title: str,
    subtitle: str,
    logo_path: str | Path | None = None,
    eyebrow: str = "eΦLab",
) -> None:
    """Encabezado principal reutilizable."""

    logo_html = ""

    if logo_path:
        path = Path(logo_path)

        if path.exists():
            encoded = _encode_image(path)
            logo_html = (
                f'<img class="ephi-logo" '
                f'src="data:image/png;base64,{encoded}" '
                f'alt="Logo ePhiCiencia">'
            )

    st.markdown(
        f"""
        <section class="ephi-hero">
            {logo_html}
            <div>
                <span class="ephi-eyebrow">{html.escape(eyebrow)}</span>
                <h1 class="ephi-title">{html.escape(title)}</h1>
                <p class="ephi-subtitle">{html.escape(subtitle)}</p>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def section_header(title: str, description: str | None = None) -> None:
    """Encabezado compacto para las secciones."""

    description_html = (
        f'<p class="ephi-section-description">{html.escape(description)}</p>'
        if description
        else ""
    )

    st.markdown(
        f"""
        <div class="ephi-section-header">
            <h2 class="ephi-section-title">{html.escape(title)}</h2>
            {description_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def feature_card(
    icon: str,
    title: str,
    text: str,
    badge: str | None = None,
) -> None:
    """Tarjeta informativa para módulos o características."""

    badge_html = (
        f'<span class="ephi-badge">{html.escape(badge)}</span>'
        if badge
        else ""
    )

    st.markdown(
        f"""
        <article class="ephi-card">
            <div class="ephi-card-icon">{html.escape(icon)}</div>
            <h3 class="ephi-card-title">{html.escape(title)}</h3>
            <p class="ephi-card-text">{html.escape(text)}</p>
            {badge_html}
        </article>
        """,
        unsafe_allow_html=True,
    )


def callout(text: str) -> None:
    """Caja destacada para mensajes importantes."""

    st.markdown(
        f'<div class="ephi-callout">{html.escape(text)}</div>',
        unsafe_allow_html=True,
    )


def footer(text: str = "eΦLab · Herramientas para el aprendizaje experimental") -> None:
    """Pie de página común."""

    st.markdown(
        f'<footer class="ephi-footer">{html.escape(text)}</footer>',
        unsafe_allow_html=True,
    )

