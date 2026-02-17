"""
Módulo de Simulación In Silico: Motor de Inferencia Clínica
Proyecto: Arquitectura Híbrida Pasiva para Páncreas Artificial (NFC)
Autor: Johan Amezcua

Descripción: 
Este script simula la lógica de backend que operaría en el smartphone del paciente.
Recibe datos simulados del sensor pasivo y determina si es seguro enviar 
el pulso magnético (NFC) para iniciar la escisión enzimática in situ.
"""

from typing import Dict, Union

def calcular_bolo_nfc(glucosa_actual: float, glucosa_objetivo: float, factor_sensibilidad: float) -> Dict[str, Union[str, float]]:
    """
    Evalúa la lectura del sensor NFC y calcula la dosis de insulina requerida.
    
    Args:
        glucosa_actual (float): Nivel de glucosa actual detectado por el sensor (mg/dL).
        glucosa_objetivo (float): Nivel de glucosa ideal configurado para el paciente (mg/dL).
        factor_sensibilidad (float): Constante metabólica del paciente (mg/dL por unidad de insulina).
        
    Returns:
        Dict: Diccionario con el estado clínico, la dosis exacta y la autorización de hardware.
    """
    
    # 1. Validación de seguridad (Cortafuegos de software contra hipoglucemia)
    if glucosa_actual <= glucosa_objetivo:
        estado = "SEGURO: Niveles en rango o bajos."
        dosis_unidades = 0.0
        accion_nfc = "DENEGADA (Riesgo de Hipoglucemia)"
        
    # 2. Cálculo de corrección algorítmica para hiperglucemia
    else:
        dosis_unidades = (glucosa_actual - glucosa_objetivo) / factor_sensibilidad
        estado = "ALERTA: Hiperglucemia detectada."
        accion_nfc = "AUTORIZADA (Emitiendo pulso NFC...)"
        
    # 3. Empaquetado de la instrucción de hardware
    respuesta = {
        "estado_clinico": estado,
        "dosis_calculada_UI": round(dosis_unidades, 2),
        "pulso_activacion_nfc": accion_nfc
    }
    
    return respuesta

if __name__ == "__main__":
    # ==========================================
    # PRUEBAS DEL ENTORNO DE SIMULACIÓN
    # ==========================================
    print("--- Iniciando Simulación NFC del Páncreas Artificial ---\n")
    
    # Prueba 1: Paciente con hiperglucemia (Requiere acción)
    print("[CASO 1: Paciente con pico glucémico postprandial]")
    resultado_hiper = calcular_bolo_nfc(glucosa_actual=210.0, glucosa_objetivo=100.0, factor_sensibilidad=35.0)
    print(f"Estado: {resultado_hiper['estado_clinico']}")
    print(f"Dosis a sintetizar: {resultado_hiper['dosis_calculada_UI']} Unidades")
    print(f"Transferencia al efector: {resultado_hiper['pulso_activacion_nfc']}\n")
    
    # Prueba 2: Paciente en rango normal (Prueba de seguridad del software)
    print("[CASO 2: Paciente en rango normal (Validación de Seguridad Activa)]")
    resultado_seguro = calcular_bolo_nfc(glucosa_actual=95.0, glucosa_objetivo=100.0, factor_sensibilidad=35.0)
    print(f"Estado: {resultado_seguro['estado_clinico']}")
    print(f"Dosis a sintetizar: {resultado_seguro['dosis_calculada_UI']} Unidades")
    print(f"Transferencia al efector: {resultado_seguro['pulso_activacion_nfc']}")