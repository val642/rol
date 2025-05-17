
# entrenamiento_exb_parcial.py
# Casos interactivos validados de Exblifep (2 primeros)
# Formato Streamlit funcional

import streamlit as st

st.set_page_config(page_title="Casos Exblifep - Parcial", layout="centered")

casos = {
    "EXB-ERR1": "ITUc BLEE - Enfoque erradicación microbiológica",
    "EXB-ERR2": "NAH BLEE/AmpC - Enfoque penetración tisular pulmonar"
}

pasos = {
    "EXB-ERR1": [
        ("¿Qué alternativa empírica sugerirías en una ITUc por BLEE en paciente sin alergias graves?",
         ["Exblifep", "Meropenem", "Amoxicilina/clavulánico"],
         ["verde", "amarillo", "rojo"],
         ["Activo frente a BLEE y OXA-48. Demostró superioridad frente a pip/tazo en ALLIUM.",
          "Debe reservarse para infecciones críticas.",
          "No cubre BLEE."]),
        ("¿Qué resultados mostró ALLIUM frente a pip/tazo?",
         ["79,1% vs 58,9% de éxito clínico + erradicación micro", "70% vs 70%", "No se alcanzó no inferioridad"],
         ["verde", "amarillo", "rojo"],
         ["Superioridad significativa en ALLIUM.",
          "Incorrecto: la diferencia fue del 20%.",
          "Falso: superó con creces la no inferioridad."]),
        ("¿Tasa de erradicación microbiológica en ALLIUM?",
         ["Exblifep 82,9% vs pip/tazo 64,9%", "Exblifep 64% vs pip/tazo 83%", "No hubo diferencia significativa"],
         ["verde", "rojo", "rojo"],
         ["Diferencia de 18%, clínicamente relevante.",
          "Invertidos los datos.",
          "Sí hubo diferencia clara."]),
        ("¿Qué estrategia propondrías con buena evolución y sensibilidad a cotrimoxazol?",
         ["Cambio a cotrimoxazol oral", "Mantener IV 10 días", "Suspender antibiótico"],
         ["verde", "amarillo", "rojo"],
         ["Adecuado si estable.",
          "Válido si no hay opción oral.",
          "Incorrecto: debe completarse pauta."])
    ],
    "EXB-ERR2": [
        ("¿Qué opción empírica propondrías en NAH con BLEE y deterioro clínico?",
         ["Exblifep", "Meropenem", "Ceftriaxona + levofloxacino"],
         ["verde", "amarillo", "rojo"],
         ["Activo frente a BLEE, AmpC y OXA-48. Buena penetración tisular.",
          "Eficaz pero menos recomendable como empírico habitual.",
          "Insuficiente frente a BLEE."]),
        ("¿Qué datos respaldan la actividad pulmonar de Exblifep?",
         ["ELF/plasma >50%, buen %fT>MIC", "ELF/plasma del 25%", "Solo estudios animales"],
         ["verde", "amarillo", "rojo"],
         ["Das et al. 2020: buena exposición en ELF.",
          "Incorrecto: subestima la exposición real.",
          "Falso: hay estudios clínicos en humanos."]),
        ("¿Qué resistencias cubre Exblifep?",
         ["BLEE, AmpC, OXA-48 no MBL, KPC mutadas", "Solo BLEE", "BLEE y KPC, no OXA-48"],
         ["verde", "amarillo", "rojo"],
         ["Amplio espectro clínicamente relevante.",
          "Incompleto: también cubre OXA-48.",
          "Falso: cubre OXA-48 no MBL."]),
        ("¿Qué argumento usarías para su inclusión en NAH/NAV?",
         ["PK pulmonar, espectro, evitar carba", "Es más barato", "Solo si alérgico a carbapenémicos"],
         ["verde", "amarillo", "rojo"],
         ["Correcto: racional, clínico y microbiológico.",
          "Débil argumento por sí solo.",
          "Falso: no está restringido por alergias."])
    ]
}

def feedback(color, texto):
    if color == "verde":
        st.success("🟢 " + texto)
    elif color == "amarillo":
        st.warning("🟡 " + texto)
    elif color == "rojo":
        st.error("🔴 " + texto)

if "caso" not in st.session_state:
    st.session_state.caso = None
    st.session_state.step = 0

st.title("🧪 Casos Exblifep - Avanzado")
seleccion = st.selectbox("Selecciona un caso:", [""] + [f"{k} - {v}" for k, v in casos.items()])

if seleccion and st.button("Iniciar caso"):
    st.session_state.caso = seleccion.split(" - ")[0]
    st.session_state.step = 0
    st.rerun()

if st.session_state.caso:
    st.subheader(f"Caso: {casos[st.session_state.caso]}")
    secuencia = pasos.get(st.session_state.caso, [])
    if st.session_state.step < len(secuencia):
        pregunta, opciones, colores, textos = secuencia[st.session_state.step]
        respuesta = st.radio(pregunta, opciones, index=None)
        if respuesta:
            idx = opciones.index(respuesta)
            feedback(colores[idx], textos[idx])
            st.button("Siguiente", on_click=lambda: st.session_state.update(step=st.session_state.step + 1))
    else:
        st.success("🎉 ¡Caso completado!")
        if st.button("Volver al menú"):
            st.session_state.caso = None
            st.session_state.step = 0
            st.rerun()
