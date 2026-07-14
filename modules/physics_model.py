from dataclasses import dataclass
import math

from modules.constants import (
    EQUILIBRIUM_TOLERANCE_M_S2,
    GRAVITY_M_S2,
)
from modules.validators import (
    validate_angle,
    validate_non_negative_mass,
    validate_positive_value,
    validate_rods_number,
    validate_rods_radius,
)


@dataclass(frozen=True)
class ExperimentalParameters:
    angle_deg: float
    counterweight_mass_kg: float
    cylinder_mass_kg: float
    cylinder_radius_m: float
    rods_number: int
    rod_mass_kg: float
    rods_radius_m: float


@dataclass(frozen=True)
class PredictionResult:
    acceleration_m_s2: float
    acceleration_x_m_s2: float
    acceleration_y_m_s2: float
    fizziq_ax_coefficient: float
    fizziq_ay_coefficient: float
    total_rods_mass_kg: float
    driving_term_kg: float
    denominator_kg: float


@dataclass(frozen=True)
class MotionClassification:
    status: str
    title: str
    message: str


def validate_parameters(parameters: ExperimentalParameters) -> None:
    validate_angle(parameters.angle_deg)

    validate_non_negative_mass(
        parameters.counterweight_mass_kg,
        "La masa del contrapeso",
    )

    validate_positive_value(
        parameters.cylinder_mass_kg,
        "La masa del cilindro",
    )

    validate_positive_value(
        parameters.cylinder_radius_m,
        "El radio del cilindro",
    )

    validate_rods_number(parameters.rods_number)

    validate_non_negative_mass(
        parameters.rod_mass_kg,
        "La masa de cada varilla",
    )

    validate_rods_radius(
        parameters.rods_radius_m,
        parameters.cylinder_radius_m,
    )


def calculate_prediction(
    parameters: ExperimentalParameters,
    gravity_m_s2: float = GRAVITY_M_S2,
) -> PredictionResult:
    validate_parameters(parameters)

    theta_rad = math.radians(parameters.angle_deg)
    total_rods_mass_kg = (
        parameters.rods_number * parameters.rod_mass_kg
    )

    driving_term_kg = (
        parameters.counterweight_mass_kg
        - (
            parameters.cylinder_mass_kg
            + total_rods_mass_kg
        )
        * math.sin(theta_rad)
    )

    denominator_kg = (
        1.5 * parameters.cylinder_mass_kg
        + total_rods_mass_kg
        * (
            1.0
            + (
                parameters.rods_radius_m
                / parameters.cylinder_radius_m
            ) ** 2
        )
        + parameters.counterweight_mass_kg
    )

    if denominator_kg <= 0.0:
        raise ValueError(
            "El denominador del modelo físico debe ser mayor que cero."
        )

    acceleration_m_s2 = (
        gravity_m_s2 * driving_term_kg / denominator_kg
    )

    acceleration_x_m_s2 = (
        acceleration_m_s2 * math.cos(theta_rad)
    )

    acceleration_y_m_s2 = (
        acceleration_m_s2 * math.sin(theta_rad)
    )

    return PredictionResult(
        acceleration_m_s2=acceleration_m_s2,
        acceleration_x_m_s2=acceleration_x_m_s2,
        acceleration_y_m_s2=acceleration_y_m_s2,
        fizziq_ax_coefficient=acceleration_x_m_s2 / 2.0,
        fizziq_ay_coefficient=acceleration_y_m_s2 / 2.0,
        total_rods_mass_kg=total_rods_mass_kg,
        driving_term_kg=driving_term_kg,
        denominator_kg=denominator_kg,
    )


def classify_motion(
    acceleration_m_s2: float,
    tolerance_m_s2: float = EQUILIBRIUM_TOLERANCE_M_S2,
) -> MotionClassification:
    if abs(acceleration_m_s2) <= tolerance_m_s2:
        return MotionClassification(
            status="equilibrium",
            title="Sistema próximo al equilibrio",
            message=(
                "La aceleración calculada es muy pequeña. "
                "La fricción y pequeñas variaciones experimentales "
                "pueden cambiar el sentido observado."
            ),
        )

    if acceleration_m_s2 > 0.0:
        return MotionClassification(
            status="counterweight",
            title="Domina el contrapeso",
            message=(
                "El cilindro debería desplazarse hacia arriba de la rampa, "
                "según la convención de signos utilizada por el modelo."
            ),
        )

    return MotionClassification(
        status="cylinder",
        title="Domina el cilindro",
        message=(
            "El cilindro debería desplazarse hacia abajo de la rampa, "
            "según la convención de signos utilizada por el modelo."
        ),
    )
