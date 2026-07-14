import streamlit as st

from modules.constants import (
    DEFAULT_ANGLE_DEG,
    DEFAULT_COUNTERWEIGHT_MASS_KG,
    DEFAULT_CYLINDER_MASS_KG,
    DEFAULT_CYLINDER_RADIUS_M,
    DEFAULT_ROD_MASS_KG,
    DEFAULT_RODS_NUMBER,
    INNER_RODS_RADIUS_M,
    OUTER_RODS_RADIUS_M,
)
from modules.physics_model import ExperimentalParameters


def prediction_form() -> ExperimentalParameters | None:
    with st.form("prediction_form"):
        left, right = st.columns(2, gap="large")

        with left:
            angle_deg = st.number_input(
                "Ángulo de la rampa, θ (°)",
                min_value=0.0,
                max_value=89.9,
                value=DEFAULT_ANGLE_DEG,
                step=0.1,
                format="%.2f",
                help="Ángulo de inclinación de la rampa respecto a la horizontal.",
            )

            counterweight_mass_kg = st.number_input(
                "Masa del contrapeso, m₁ (kg)",
                min_value=0.0,
                value=DEFAULT_COUNTERWEIGHT_MASS_KG,
                step=0.001,
                format="%.5f",
            )

            cylinder_mass_kg = st.number_input(
                "Masa del cilindro, M (kg)",
                min_value=0.00001,
                value=DEFAULT_CYLINDER_MASS_KG,
                step=0.001,
                format="%.5f",
            )

            cylinder_radius_m = st.number_input(
                "Radio del cilindro, R (m)",
                min_value=0.00001,
                value=DEFAULT_CYLINDER_RADIUS_M,
                step=0.001,
                format="%.4f",
            )

        with right:
            rods_number = st.number_input(
                "Número de varillas, N",
                min_value=0,
                max_value=20,
                value=DEFAULT_RODS_NUMBER,
                step=1,
            )

            rod_mass_kg = st.number_input(
                "Masa de cada varilla, m (kg)",
                min_value=0.0,
                value=DEFAULT_ROD_MASS_KG,
                step=0.001,
                format="%.6f",
            )

            radius_mode = st.radio(
                "Ubicación radial de las varillas",
                options=(
                    "Radio interior",
                    "Radio exterior",
                    "Personalizado",
                ),
            )

            if radius_mode == "Radio interior":
                rods_radius_m = INNER_RODS_RADIUS_M
                st.caption(
                    f"Se utilizará rₐ = {INNER_RODS_RADIUS_M:.3f} m."
                )

            elif radius_mode == "Radio exterior":
                rods_radius_m = OUTER_RODS_RADIUS_M
                st.caption(
                    f"Se utilizará rᵦ = {OUTER_RODS_RADIUS_M:.3f} m."
                )

            else:
                rods_radius_m = st.number_input(
                    "Radio personalizado, rₓ (m)",
                    min_value=0.0,
                    max_value=float(cylinder_radius_m),
                    value=min(
                        INNER_RODS_RADIUS_M,
                        float(cylinder_radius_m),
                    ),
                    step=0.001,
                    format="%.4f",
                )

        submitted = st.form_submit_button(
            "Calcular predicción",
            type="primary",
            use_container_width=True,
        )

    if not submitted:
        return None

    return ExperimentalParameters(
        angle_deg=float(angle_deg),
        counterweight_mass_kg=float(counterweight_mass_kg),
        cylinder_mass_kg=float(cylinder_mass_kg),
        cylinder_radius_m=float(cylinder_radius_m),
        rods_number=int(rods_number),
        rod_mass_kg=float(rod_mass_kg),
        rods_radius_m=float(rods_radius_m),
    )
