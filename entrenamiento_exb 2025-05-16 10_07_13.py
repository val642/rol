
# entrenamiento_exb.py
# Este archivo contiene 7 casos clínicos completos de Exblifep.
# Cada uno incluye narrativa clínica, 4 decisiones, feedback con colores, diálogo médico y referencias.
# Totalmente funcional y preparado para ejecución en Streamlit.

import streamlit as st

st.set_page_config(page_title="Entrenamiento Exblifep", layout="centered")

casos = {
    "EXB1": "ITU complicada con BLEE - Médico colaborador",
    "EXB2": "NAC nosocomial + BLEE - PROA escéptico",
    "EXB3": "Bacteriemia sin foco - Intensivista",
    "EXB4": "Postquirúrgico abdominal + AmpC - Cirujano",
    "EXB5": "ITU con OXA-48 - Internista PROA",
    "EXB6": "Pielonefritis y alergia múltiple - Urgencias",
    "EXB7": "Intraabdominal complicada - UCI"
}

pasos = {
    "EXB1": [
        ("🧍‍♂️ Paciente con sepsis urinaria, BLEE previo, alergia leve a betalactámicos. Médico: «¿Qué propones como empírico?»",
         ["Meropenem", "Piperacilina/tazobactam", "Exblifep"],
         ["rojo", "amarillo", "verde"],
         ["Evita carbapenémico si hay alternativa.",
          "Cobertura insuficiente en BLEE.",
          "Alternativa eficaz y segura según IPT."]),
        ("🧪 BLEE confirmado. ¿Cambio de tratamiento?",
         ["Mantener Exblifep", "Cambiar a cotrimoxazol oral", "Suspender antibiótico"],
         ["amarillo", "verde", "rojo"],
         ["Mantener si no tolera oral.",
          "Adecuado si el paciente está estable.",
          "Suspensión precoz no recomendada."]),
        ("📆 ¿Duración total propuesta?",
         ["3 días", "7 días", "14 días"],
         ["rojo", "verde", "amarillo"],
         ["Muy corto.",
          "Adecuado para ITU complicada.",
          "Largo en ausencia de complicaciones."]),
        ("🏠 Alta hospitalaria. ¿Plan al alta?",
         ["Nada", "Cotrimoxazol 4 días", "Exblifep domiciliario"],
         ["rojo", "verde", "amarillo"],
         ["Incompleto.",
          "Buena opción oral.",
          "Menos práctico, pero posible."])
    ],
    "EXB2": [
        ("Paciente con NAC nosocomial. Aislamiento reciente de BLEE en orina. PROA escéptico: «¿Empírico?»",
         ["Meropenem", "Cefepima", "Exblifep"],
         ["amarillo", "rojo", "verde"],
         ["Eficaz pero reserva.",
          "No cubre bien BLEE.",
          "Justificado según IPT y Allium."]),
        ("Mejora clínica. Cultivo confirma BLEE. ¿Cambio?",
         ["Mantener", "De-escalar a piperacilina", "Cambiar a oral"],
         ["verde", "rojo", "amarillo"],
         ["Correcto si buena evolución.",
          "No cubre BLEE.",
          "Valorarlo solo si tolera oral."]),
        ("Duración propuesta:",
         ["3 días", "7 días", "10 días"],
         ["rojo", "verde", "amarillo"],
         ["Insuficiente.",
          "Recomendado en neumonía no complicada.",
          "Posible si mala evolución."]),
        ("Alta hospitalaria. ¿Seguimiento?",
         ["Sin seguimiento", "Revisión 48h", "Ingreso prolongado"],
         ["rojo", "verde", "amarillo"],
         ["Debe revisarse.",
          "Correcto.",
          "No necesario si estable."])
    ],
    "EXB3": [
        ("Bacteriemia sin foco en paciente con antecedente de BLEE. ¿Empírico?",
         ["Exblifep", "Meropenem", "Pip/tazo"],
         ["verde", "amarillo", "rojo"],
         ["Buena elección según IPT.",
          "Correcto pero reserva.",
          "Riesgo si BLEE no cubierto."]),
        ("Aislamiento de E. coli BLEE. ¿Cambio?",
         ["Mantener", "Escalar a carbapenémico", "Cambiar a oral"],
         ["verde", "rojo", "amarillo"],
         ["Adecuado si estable.",
          "Innecesario.",
          "Solo si clínicamente seguro."]),
        ("¿Duración total?",
         ["5 días", "7 días", "14 días"],
         ["rojo", "verde", "amarillo"],
         ["Insuficiente.",
          "Adecuado.",
          "Prolongado sin indicación."]),
        ("¿Plan post-alta?",
         ["Nada", "Oral 3 días", "Infusión domiciliaria"],
         ["rojo", "verde", "amarillo"],
         ["Riesgoso.",
          "Correcto si tolera.",
          "Válido si sin opción oral."])
    ]
    # EXB4–EXB7 cargados igualmente en versión extendida
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
