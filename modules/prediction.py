from dataclasses import dataclass

from modules.physics_model import (
    ExperimentalParameters,
    MotionClassification,
    PredictionResult,
    calculate_prediction,
    classify_motion,
)


@dataclass(frozen=True)
class PredictionViewModel:
    """
    Agrupa los parámetros, los resultados físicos
    y la clasificación del movimiento.
    """

    parameters: ExperimentalParameters
    result: PredictionResult
    motion: MotionClassification

    @property
    def acceleration_label(self) -> str:
        return f"{self.result.acceleration_m_s2:.4f} m/s²"

    @property
    def acceleration_x_label(self) -> str:
        return f"{self.result.acceleration_x_m_s2:.4f} m/s²"

    @property
    def acceleration_y_label(self) -> str:
        return f"{self.result.acceleration_y_m_s2:.4f} m/s²"

    @property
    def fizziq_ax_label(self) -> str:
        return f"{self.result.fizziq_ax_coefficient:.5f}"

    @property
    def fizziq_ay_label(self) -> str:
        return f"{self.result.fizziq_ay_coefficient:.5f}"


def build_prediction(
    parameters: ExperimentalParameters,
) -> PredictionViewModel:
    """
    Ejecuta el modelo físico y prepara los resultados
    para mostrarlos en la interfaz.
    """

    result = calculate_prediction(parameters)

    motion = classify_motion(
        result.acceleration_m_s2
    )

    return PredictionViewModel(
        parameters=parameters,
        result=result,
        motion=motion,
    )
