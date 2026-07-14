from pathlib import Path
import streamlit as st

def page_header(
    title: str,
    subtitle: str,
    *,
    eyebrow: str = "eΦLab",
    logo_path: str | Path | None = None,
) -> None:
    logo_col, text_col = st.columns(
        [1, 7],
        gap="medium",
        vertical_alignment="center",
    )

    with logo_col:
        path = Path(logo_path) if logo_path else None
        if path and path.exists():
            st.image(path, width=88)
        else:
            st.markdown("## eΦ")

    with text_col:
        st.caption(eyebrow)
        st.title(title)
        st.write(subtitle)

    st.divider()

def section_header(title: str, description: str | None = None) -> None:
    st.subheader(title)
    if description:
        st.caption(description)

def module_card(
    icon: str,
    title: str,
    description: str,
    *,
    status: str | None = None,
) -> None:
    with st.container(border=True):
        st.markdown(f"### {icon} {title}")
        st.write(description)
        if status:
            st.caption(status)

def callout(text: str, *, kind: str = "info") -> None:
    messages = {
        "success": st.success,
        "warning": st.warning,
        "error": st.error,
        "info": st.info,
    }
    messages.get(kind, st.info)(text)

def app_footer() -> None:
    st.divider()
    st.caption(
        "eΦLab · Herramientas digitales para el aprendizaje experimental"
    )
