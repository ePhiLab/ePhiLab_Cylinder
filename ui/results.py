import streamlit as st

from modules.prediction import PredictionViewModel
from ui.components import section_header


def show_motion_message(prediction: PredictionViewModel) -> None:
    motion = prediction.motion
    text = f"**{motion.title}.** {motion.message}"

    if motion.status == "equilibrium":
        st.warning(text)
    elif motion.status == "counterweight":
        st.success(text)
    else:
        st.info(text)


def show_prediction_metrics(
    prediction: PredictionViewModel,
) -> None:
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Aceleración sobre la rampa",
        prediction.acceleration_label,
    )

    col2.metric(
        "Componente horizontal, aₓ",
        prediction.acceleration_x_label,
    )

    col3.metric(
        "Componente vertical, aᵧ",
        prediction.acceleration_y_label,
    )


def show_model_details(
    prediction: PredictionViewModel,
) -> None:
    result = prediction.result
    parameters = prediction.parameters

    with st.expander("Detalles del cálculo", expanded=False):
        detail1, detail2, detail3 = st.columns(3)

        detail1.metric(
            "Masa total de varillas",
            f"{result.total_rods_mass_kg:.5f} kg",
        )

        detail2.metric(
            "Radio seleccionado",
            f"{parameters.rods_radius_m:.4f} m",
        )

        detail3.metric(
            "Término impulsor",
            f"{result.driving_term_kg:.6f} kg",
        )

        st.caption(
            "El término impulsor corresponde a la diferencia entre "
            "el efecto del contrapeso y la componente del peso del "
            "cilindro y las varillas sobre la rampa."
        )


def show_fizziq_prediction(
    prediction: PredictionViewModel,
) -> None:
    section_header(
        "3. Predicción para FizziQ",
        (
            "Compare estos coeficientes con el ajuste cuadrático "
            "de las gráficas de posición en función del tiempo."
        ),
    )

    st.write(
        "Si FizziQ ajusta los datos mediante "
        r"$x(t)=A_x t^2+B_x t+C_x$ y "
        r"$y(t)=A_y t^2+B_y t+C_y$, entonces:"
    )

    col1, col2 = st.columns(2)

    col1.metric(
        "Coeficiente esperado, Aₓ = aₓ/2",
        prediction.fizziq_ax_label,
    )

    col2.metric(
        "Coeficiente esperado, Aᵧ = aᵧ/2",
        prediction.fizziq_ay_label,
    )

    st.latex(
        rf"""
        x(t)\approx
        ({prediction.result.fizziq_ax_coefficient:.5f})t^2
        +B_x t+C_x
        """
    )

    st.latex(
        rf"""
        y(t)\approx
        ({prediction.result.fizziq_ay_coefficient:.5f})t^2
        +B_y t+C_y
        """
    )

    st.caption(
        "Los signos dependen de la orientación de los ejes "
        "seleccionados durante el análisis del video."
    )


def show_prediction_results(
    prediction: PredictionViewModel,
) -> None:
    section_header(
        "2. Resultado de la predicción",
        (
            "El modelo calcula la aceleración del sistema y "
            "sus componentes rectangulares."
        ),
    )

    show_prediction_metrics(prediction)
    show_motion_message(prediction)
    show_model_details(prediction)
    show_fizziq_prediction(prediction)
