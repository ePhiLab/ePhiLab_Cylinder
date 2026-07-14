from pathlib import Path

import streamlit as st


def hero_header(
    title: str,
    subtitle: str,
    logo_path: str | Path | None = None,
    eyebrow: str = "eΦLab",
) -> None:
    """
    Encabezado principal construido únicamente
    con componentes nativos de Streamlit.
    """

    logo_column, text_column = st.columns(
        [1, 7],
        gap="medium",
        vertical_alignment="center",
    )

    with logo_column:
        if logo_path:
            path = Path(logo_path)

            if path.exists():
                st.image(
                    str(path),
                    width=92,
                )
            else:
                st.info("Logo")
        else:
            st.info("eΦ")

    with text_column:
        st.caption(eyebrow)
        st.title(title)
        st.write(subtitle)

    st.divider()


def section_header(
    title: str,
    description: str | None = None,
) -> None:
    """Encabezado reutilizable para las secciones."""

    st.subheader(title)

    if description:
        st.caption(description)


def feature_card(
    icon: str,
    title: str,
    text: str,
    badge: str | None = None,
) -> None:
    """Tarjeta informativa usando un contenedor nativo."""

    with st.container(border=True):
        st.markdown(f"### {icon} {title}")
        st.write(text)

        if badge:
            st.caption(badge)


def callout(
    text: str,
    callout_type: str = "info",
) -> None:
    """Caja destacada con estilos nativos de Streamlit."""

    if callout_type == "success":
        st.success(text)

    elif callout_type == "warning":
        st.warning(text)

    elif callout_type == "error":
        st.error(text)

    else:
        st.info(text)


def footer(
    text: str = "eΦLab · Herramientas para el aprendizaje experimental",
) -> None:
    """Pie de página común."""

    st.divider()
    st.caption(text)
