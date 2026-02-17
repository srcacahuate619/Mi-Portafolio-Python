# Portafolio de Ingeniería de Software & HealthTech 🧬💻

¡Hola! Soy **Johan Amezcua**. Bienvenido a mi repositorio personal. Aquí combino mi formación en **Ciencias Médicas** con la **Ingeniería de Software** para crear soluciones tecnológicas de alto impacto.

---

## 🌟 PROYECTO DESTACADO: Arquitectura Híbrida Pasiva (Diabetes T1)

> **Propuesta de sistema "Battery-less" para eliminar el riesgo de fallos mecánicos en bombas de insulina.**

### 📄 Documentación Técnica
Puedes leer el White Paper completo con la justificación fisiológica y técnica aquí:
- 📕 Publicación Oficial en Zenodo (DOI): [https://zenodo.org/records/18668319]

### 💡 El Problema
Las bombas de insulina actuales dependen de baterías internas y almacenan insulina activa. Si el hardware falla, el paciente corre riesgo de una sobredosis letal. Además, son vulnerables a ciberataques remotos.

### 🚀 Mi Solución Propuesta
Una arquitectura distribuida en 3 nodos:
1.  **Sensor Pasivo (Titanio + PEEK):** Sin batería, alimentado por inducción.
2.  **Procesamiento Edge (Smartphone):** App en Python que calcula la dosis y exige autenticación biométrica.
3.  **Efector Bioquímico:** Almacena **Proinsulina inerte** y la activa con enzimas solo cuando recibe la señal NFC segura.

### 🛠️ Tecnologías Aplicadas
* **Lenguaje:** Python 3.10+ (Lógica de inferencia clínica).
* **Hardware:** Concepto de telemetría NFC pasiva (13.56 MHz).
* **Seguridad:** Arquitectura *Air-Gapped* y validación biométrica.

---

## 💻 Cómo probar la Simulación (Script)

He incluido un script en Python (`simulacion_nfc.py`) que emula el "cerebro" del sistema. Este código recibe los datos del sensor y decide si es seguro activar el efector.

### Ejecución
Descarga el archivo `simulacion_nfc.py` y ejecútalo en tu terminal:

```bash
python simulacion_nfc.py
