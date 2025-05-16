
# entrenamiento_exb5.py
# 5 casos clínicos completos de Exblifep con narrativa, 4 decisiones, feedback con colores y diálogo clínico

import streamlit as st

st.set_page_config(page_title="Casos Exblifep", layout="centered")

casos = {
    "EXB1": "Sepsis urinaria por BLEE en paciente pluripatológico",
    "EXB2": "NAC nosocomial por BLEE en paciente con EPOC",
    "EXB3": "Bacteriemia secundaria a ITU en paciente institucionalizado",
    "EXB4": "Peritonitis postquirúrgica por AmpC en cirugía digestiva",
    "EXB5": "ITU complicada con aislamiento OXA-48"
}

pasos = {
    "EXB1": [
        ("🧍‍♂️ Hombre de 72 años, DM2, EPOC. Ingresa con fiebre, hipotensión, desorientación. Antecedente de BLEE. ¿Qué propones empíricamente?",
        ["Meropenem", "Pip/tazo", "Exblifep"],
        ["rojo", "amarillo", "verde"],
        ["Reserva estratégica.", "Insuficiente frente a BLEE.", "Adecuado según IPT y Allium."]),
        ("🧪 E. coli BLEE confirmado. ¿Cambio?",
        ["Mantener", "Cotrimoxazol oral", "Suspender"],
        ["verde", "amarillo", "rojo"],
        ["Correcto si estable.", "Válido si tolera.", "Riesgoso."]),
        ("🕐 ¿Duración total propuesta?",
        ["3 días", "7 días", "14 días"],
        ["rojo", "verde", "amarillo"],
        ["Muy corta.", "Recomendada para ITUc.", "Prolongada."]),
        ("📤 Plan al alta:",
        ["Nada", "Cotrimoxazol oral", "Infusión domiciliaria"],
        ["rojo", "verde", "amarillo"],
        ["Incompleto.", "Adecuado.", "Menos práctico."])
    ],
    "EXB2": [
        ("🧓 Varón 68 años, EPOC, NAC grave, antecedente de BLEE. ¿Empírico?",
        ["Meropenem", "Ceftriaxona", "Exblifep"],
        ["amarillo", "rojo", "verde"],
        ["Alternativa útil pero de reserva.", "No cubre BLEE.", "Opción racional sin carba."]),
        ("📄 Cultivo: BLEE. ¿Cambio?",
        ["Mantener", "Escalar", "Oral"],
        ["verde", "rojo", "amarillo"],
        ["Correcto.", "Innecesario.", "Solo si tolera."]),
        ("📆 ¿Duración ideal?",
        ["3 días", "7 días", "10 días"],
        ["rojo", "verde", "amarillo"],
        ["Corta.", "Recomendada.", "Prolongada sin complicaciones."]),
        ("🔎 Seguimiento post alta:",
        ["Revisión médica", "Nada", "Ingreso domiciliario"],
        ["verde", "rojo", "amarillo"],
        ["Adecuado.", "No recomendable.", "Excesivo."])
    ],
    "EXB3": [
        ("👵 Mujer 84 años, institucionalizada, ITU previa, desorientada. ¿Empírico?",
        ["Cefepima", "Ciprofloxacino", "Exblifep"],
        ["rojo", "amarillo", "verde"],
        ["Resistencia probable.", "Riesgo de resistencia BLEE.", "Adecuado y seguro."]),
        ("🧪 Cultivo: BLEE. ¿Cambio?",
        ["Mantener", "Suspender", "Oral"],
        ["verde", "rojo", "amarillo"],
        ["Correcto.", "Insuficiente.", "Solo si estable."]),
        ("🕐 ¿Duración adecuada?",
        ["3 días", "5 días", "7 días"],
        ["rojo", "amarillo", "verde"],
        ["Insuficiente.", "Válido en leves.", "Recomendado."]),
        ("🏥 ¿Alta y seguimiento?",
        ["Sin revisión", "Revisión médica", "Alta y llamada"],
        ["rojo", "verde", "amarillo"],
        ["Falta control.", "Correcto.", "Válido si no hay síntomas."])
    ],
    "EXB4": [
        ("👨‍⚕️ Paciente 58 años, cirugía colorrectal. Fiebre y dolor abdominal. Cultivo previo: Enterobacter. ¿Empírico?",
        ["Meropenem", "Pip/tazo", "Exblifep"],
        ["amarillo", "rojo", "verde"],
        ["Alternativa de reserva.", "Insuficiente frente a AmpC.", "Adecuado según IPT."]),
        ("🧪 AmpC confirmado. ¿Cambio?",
        ["Mantener", "Escalar", "Suspender"],
        ["verde", "amarillo", "rojo"],
        ["Correcto.", "No indicado sin fallo clínico.", "No justificado."]),
        ("📆 ¿Duración propuesta?",
        ["5 días", "7 días", "14 días"],
        ["amarillo", "verde", "rojo"],
        ["Posible.", "Adecuado.", "Demasiado larga."]),
        ("🏁 Seguimiento:",
        ["Alta sin control", "Revisión clínica", "Cultivos repetidos"],
        ["rojo", "verde", "amarillo"],
        ["Insuficiente.", "Correcto.", "No necesarios si evolución buena."])
    ],
    "EXB5": [
        ("🧔 Hombre 75 años, OXA-48 previo, ITU complicada. ¿Empírico?",
        ["Ceftriaxona", "Exblifep", "Ceftazidima-avibactam"],
        ["rojo", "verde", "verde"],
        ["No cubre OXA-48.", "Opción válida según IPT.", "También eficaz."]),
        ("🧪 Cultivo OXA-48. ¿Cambio?",
        ["Mantener", "Suspender", "Oral"],
        ["verde", "rojo", "amarillo"],
        ["Correcto.", "Riesgoso.", "Solo si sensible."]),
        ("📆 ¿Duración estimada?",
        ["3 días", "5 días", "7 días"],
        ["rojo", "amarillo", "verde"],
        ["Corta.", "Posible si leve.", "Adecuado."]),
        ("📤 ¿Qué seguimiento propones?",
        ["Alta sin control", "Revisión médica", "Visita domiciliaria"],
        ["rojo", "verde", "amarillo"],
        ["Falta control.", "Correcto.", "Solo si paciente frágil."])
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

st.title("🧪 Casos clínicos - Exblifep")
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
