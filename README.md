# Arquitectura Híbrida Pasiva para el Manejo de la Diabetes 🩸🧬
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18668319.svg)](https://doi.org/10.5281/zenodo.18668319)

> **Repositorio complementario para el whitepaper / preprint publicado en Zenodo.**
> Concepto de bio-implante sin batería mediado por telemetría NFC para la escisión enzimática de proinsulina *in situ*.

## 📌 Resumen del Proyecto (Abstract)
Los sistemas actuales de bombas de insulina dependen de componentes electromecánicos activos (baterías, motores, catéteres), lo que los hace susceptibles a fallas de hardware, problemas de calibración y altos costos de mantenimiento. 

Este proyecto propone una **arquitectura híbrida pasiva**. En lugar de inyectar insulina exógena mecánicamente, el concepto plantea el uso de un implante subcutáneo sin batería que almacena proinsulina. Mediante telemetría **NFC (Near Field Communication)** desde un dispositivo móvil, se induce una micro-corriente que activa un proceso de escisión enzimática, convirtiendo la proinsulina en insulina activa fisiológicamente solo en el momento exacto en que se requiere.

## 💻 Contenido del Repositorio
Este repositorio contiene los scripts en **Python** desarrollados como prueba de concepto computacional y modelado matemático para respaldar la viabilidad teórica de la investigación.

* `modelos_cineticos/`: Scripts para simular la tasa de conversión enzimática de proinsulina a insulina.
* `simulacion_nfc/`: Modelado de la inducción electromagnética pasiva y cálculo de miliamperios requeridos para la activación del implante.
* `analisis_datos/`: Herramientas utilizadas para procesar las gráficas y datos presentados en el preprint.

*(Nota: Ajusta los nombres de las carpetas/archivos de arriba según lo que tengas exactamente en tu repositorio).*

## 🏗️ Arquitectura del Sistema
El modelo se divide en tres capas fundamentales:
1.  **Capa de Telemetría (Activa):** Un smartphone (o lector NFC) que envía la señal electromagnética de corto alcance.
2.  **Capa del Implante (Pasiva):** Un circuito RLC resonante en el implante que cosecha la energía del campo NFC para generar voltaje.
3.  **Capa Bioquímica:** Micro-válvulas o estímulos termo-eléctricos que liberan las enzimas convertidoras (PC1/3 y PC2) en el reservorio de proinsulina.

## 📄 Citar esta Investigación
Si utilizas los conceptos teóricos o el código de este repositorio, por favor cita la publicación original:

> Amezcua Cepeda, J. A. (2026). *Arquitectura Híbrida Pasiva para el Manejo de la Diabetes: Escisión Enzimática de Proinsulina in situ mediada por Telemetría NFC*. Zenodo. https://doi.org/10.5281/zenodo.18668319

## ⚠️ Aviso Legal (Disclaimer Médico)
*Este repositorio y el documento asociado son de naturaleza puramente conceptual, académica y de investigación (TRL-1 / TRL-2). No constituyen consejo médico, no están aprobados por la FDA ni ninguna otra entidad regulatoria, y los modelos computacionales aquí descritos no deben utilizarse para la toma de decisiones clínicas ni en humanos.*

---
**Desarrollado por:** Johan Amezcua | Ingeniería de Software & Medicina Humana.
