import streamlit as st

st.set_page_config(page_title="Casos interactivos antibióticos", layout="centered")

# Diccionario de casos
casos = {
    "EXB1": "Exblifep - ITU complicada BLEE (médico colaborador)",
    "EXB2": "Exblifep - NAC nosocomial + BLEE (PROA escéptico)",
    "ZEV1": "Zevtera - NAC grave en urgencias (S. pneumoniae)",
    "ZEV2": "Zevtera - Bacteriemia por SCN post-cirugía (médico dudoso)"
}

# Estado inicial
if "caso" not in st.session_state:
    st.session_state.caso = None
    st.session_state.step = 0

# Función para mostrar feedback con color
def mostrar_feedback(color, texto):
    if color == "verde":
        st.success("🟢 " + texto)
    elif color == "amarillo":
        st.warning("🟡 " + texto)
    elif color == "rojo":
        st.error("🔴 " + texto)

# Menú de selección
if st.session_state.caso is None:
    st.title("🔍 Selecciona un caso clínico")
    caso_seleccionado = st.selectbox("Casos disponibles:", [""] + [f"{key} - {value}" for key, value in casos.items()])
    if caso_seleccionado and st.button("Iniciar caso"):
        st.session_state.caso = caso_seleccionado.split(" - ")[0]
        st.session_state.step = 0
        st.rerun()

# Diccionario de pasos por caso
pasos = {
    "EXB1": [
        ("Paciente con sepsis urinaria y colonización previa por BLEE. ¿Qué antibiótico empírico propones?",
         ["Meropenem", "Piperacilina/tazobactam", "Exblifep"],
         ["rojo", "amarillo", "verde"],
         ["Uso innecesario de carbapenémico.",
          "Puede fallar frente a BLEE.",
          "Buena cobertura frente a BLEE."]),

        ("Cultivo: BLEE sensible a cotrimoxazol. El paciente mejora. ¿Qué haces?",
         ["Mantienes Exblifep", "Cambias a cotrimoxazol oral", "Suspendes antibiótico"],
         ["verde", "verde", "rojo"],
         ["Puede mantenerse si no hay vía oral.",
          "Correcto si el paciente tolera vía oral.",
          "Suspender puede ser arriesgado."]),

        ("¿Cuánto tiempo de tratamiento total propones?",
         ["3 días", "7 días", "14 días"],
         ["rojo", "verde", "amarillo"],
         ["Duración insuficiente.", 
          "Duración adecuada en ITU complicada con buena evolución.",
          "Posiblemente excesivo."]),

        ("Al alta, el médico duda si continuar algo en casa. ¿Qué propones?",
         ["Nada", "Cotrimoxazol 3 días", "Exblifep en domicilio"],
         ["rojo", "verde", "amarillo"],
         ["Riesgo de recaída.",
          "Buena opción si hay buena tolerancia oral.",
          "IV domiciliaria es menos cómoda."])
    ],

    "EXB2": [
        ("Paciente con NAC nosocomial y colonización por BLEE. ¿Empírico?",
         ["Ceftriaxona", "Meropenem", "Exblifep"],
         ["rojo", "amarillo", "verde"],
         ["No cubre BLEE.",
          "Cubre pero es menos ecológico.",
          "Buena opción frente a BLEE con menor presión."]),

        ("El PROA plantea dudas sobre Exblifep. ¿Cómo respondes?",
         ["Explicas respaldo y estudios", "Aceptas y cambias", "Ignoras la objeción"],
         ["verde", "amarillo", "rojo"],
         ["Correcto, justificas su uso.",
          "Pierdes oportunidad formativa.",
          "Desacredita tu posicionamiento."]),

        ("Cultivo confirma BLEE. ¿Ajustas tratamiento?",
         ["Sí, a carbapenem", "Mantengo Exblifep", "Cambio a piperacilina/tazo"],
         ["amarillo", "verde", "rojo"],
         ["Es aceptable, pero no aporta más.",
          "Buena opción si hay buena evolución.",
          "No fiable frente a BLEE."]),

        ("El paciente está estable. ¿Qué duración propones?",
         ["5 días", "7 días", "10 días"],
         ["amarillo", "verde", "amarillo"],
         ["Puede ser suficiente en algunos casos.",
          "Duración adecuada para NAC grave con buena evolución.",
          "Podría ser más de lo necesario."])
    ]
}

# Renderizado de cada paso
if st.session_state.caso:
    st.title(f"🧪 Caso: {casos[st.session_state.caso]}")
    pasos_caso = pasos[st.session_state.caso]

    if st.session_state.step < len(pasos_caso):
        pregunta, opciones, colores, feedbacks = pasos_caso[st.session_state.step]
        opcion = st.radio(f"**{pregunta}**", opciones, index=None)
        if opcion:
            idx = opciones.index(opcion)
            mostrar_feedback(colores[idx], feedbacks[idx])
            st.button("Siguiente", on_click=lambda: st.session_state.update(step=st.session_state.step + 1))
    else:
        st.success("🎉 ¡Caso completado!")
        if st.button("Volver al menú de casos"):
            st.session_state.caso = None
            st.session_state.step = 0
            st.rerun()
