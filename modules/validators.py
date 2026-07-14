from modules.constants import (
    INNER_RODS_RADIUS_M,
    OUTER_RODS_RADIUS_M,
)


def validate_angle(angle_deg: float) -> None:
    if not 0.0 <= angle_deg < 90.0:
        raise ValueError(
            "El ángulo debe estar entre 0° y un valor menor que 90°."
        )


def validate_non_negative_mass(value: float, label: str) -> None:
    if value < 0.0:
        raise ValueError(f"{label} no puede ser negativa.")


def validate_positive_value(value: float, label: str) -> None:
    if value <= 0.0:
        raise ValueError(f"{label} debe ser mayor que cero.")


def validate_rods_number(rods_number: int) -> None:
    if rods_number < 0:
        raise ValueError("El número de varillas no puede ser negativo.")


def validate_rods_radius(
    rods_radius_m: float,
    cylinder_radius_m: float,
) -> None:
    if rods_radius_m < 0.0:
        raise ValueError(
            "El radio de ubicación de las varillas no puede ser negativo."
        )

    if rods_radius_m > cylinder_radius_m:
        raise ValueError(
            "El radio de ubicación de las varillas no puede ser mayor "
            "que el radio del cilindro."
        )


def validate_standard_radii(cylinder_radius_m: float) -> None:
    if INNER_RODS_RADIUS_M > cylinder_radius_m:
        raise ValueError(
            "El radio interior definido es mayor que el radio del cilindro."
        )

    if OUTER_RODS_RADIUS_M > cylinder_radius_m:
        raise ValueError(
            "El radio exterior definido es mayor que el radio del cilindro."
        )
