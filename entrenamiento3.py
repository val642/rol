
import streamlit as st

st.set_page_config(page_title="Entrenamiento clínico interactivo", layout="centered")

casos = {
    "EXB1": ("Exblifep", "ITU complicada con BLEE - Médico colaborador"),
    "ZEV1": ("Zevtera", "NAC grave por S. pneumoniae resistente - Urgenciólogo"),
}

pasos = {
    "EXB1": [
        ("""🧍‍♂️ Paciente de 68 años, DM2, HTA, ingreso por fiebre, hipotensión y desorientación. Aislamiento previo de BLEE.

👨‍⚕️ Médico: «Probable sepsis urinaria. Alergia leve a penicilinas. ¿Qué propones como empírico?»""",
         ["Meropenem", "Piperacilina/tazobactam", "Exblifep"],
         ["rojo", "amarillo", "verde"],
         ["Evita meropenem salvo necesidad crítica.",
          "Riesgo de ineficacia frente a BLEE.",
          "Cubres BLEE sin carbapenémicos. IPT Exblifep y estudio ALLIUM lo respaldan."]),
        ("""🧪 Cultivo confirma E. coli BLEE. Paciente mejora.

👨‍⚕️ Médico: «¿Cambiarías algo?»""",
         ["Mantener Exblifep", "Cambiar a cotrimoxazol oral", "Suspender antibiótico"],
         ["amarillo", "verde", "rojo"],
         ["Podría mantenerse si no hay vía oral.",
          "Correcto si el paciente tolera oral.",
          "Riesgo de recaída sin completar ciclo."]),
        ("📆 Día 3 de tratamiento. ¿Cuánto tiempo total propones?",
         ["3 días", "7 días", "14 días"],
         ["rojo", "verde", "amarillo"],
         ["Demasiado corto.",
          "Duración recomendada para ITU complicada con buena evolución.",
          "Podría ser excesivo según GPC."]),
        ("🏠 El paciente está para alta. ¿Plan terapéutico?",
         ["Nada", "Cotrimoxazol oral 4 días", "Exblifep domiciliario"],
         ["rojo", "verde", "amarillo"],
         ["No completar ciclo favorece recaídas.",
          "Buena opción si tolera oral.",
          "Más incómodo, pero válido si no hay oral."])
    ],
    "ZEV1": [
        ("""🧍‍♀️ Mujer de 74 años, EPOC, NAC grave con hipotensión, satO2 <90%, sin alergias. Rx con consolidación. Previos aislamientos de S. pneumoniae resistente.

👨‍⚕️ Urgenciólogo: «¿Qué damos empírico?»""",
         ["Levofloxacino", "Vancomicina", "Ceftobiprole"],
         ["rojo", "amarillo", "verde"],
         ["Fluoroquinolonas no cubren bien neumococo resistente.",
          "Solo cubre Gram+, falta betalactámico.",
          "Buena opción empírica. Cubres S. pneumoniae resistente y S. aureus. IPT Ceftobiprole."]),
        ("""🧪 Cultivo: S. pneumoniae resistente a penicilina, sensible a ceftobiprole.

👨‍⚕️ Urgenciólogo: «¿Mantenemos o cambiamos?»""",
         ["Mantener ceftobiprole", "Escalar a linezolid", "Suspender y dar alta"],
         ["verde", "rojo", "rojo"],
         ["Correcto. Buena evolución y sensibilidad.",
          "Linezolid no es necesario ni primera línea.",
          "Alta sin completar ciclo puede ser riesgoso."]),
        ("📆 ¿Cuánto tiempo total propones?",
         ["3 días", "5 días", "10 días"],
         ["rojo", "verde", "amarillo"],
         ["Muy corto.",
          "Adecuado en neumonía sin complicaciones.",
          "Podría ser largo si buena evolución."]),
        ("🏥 ¿Qué seguimiento haces?",
         ["Alta sin revisión", "Revisión en 48h", "Ingreso hospitalario prolongado"],
         ["rojo", "verde", "amarillo"],
         ["No revisar puede ser peligroso.",
          "Correcto. Garantiza evolución tras antibiótico.",
          "No es necesario si hay buena evolución."])
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
    st.session_state.filtro = "Todos"

st.title("🧪 Entrenamiento clínico interactivo")
filtro = st.radio("Filtrar por producto:", ["Todos", "Exblifep", "Zevtera"])
st.session_state.filtro = filtro

casos_filtrados = {k: v[1] for k, v in casos.items() if filtro == "Todos" or v[0] == filtro}
seleccion = st.selectbox("Selecciona un caso:", [""] + [f"{k} - {v}" for k, v in casos_filtrados.items()])

if seleccion and st.button("Iniciar caso"):
    st.session_state.caso = seleccion.split(" - ")[0]
    st.session_state.step = 0
    st.rerun()

if st.session_state.caso:
    st.subheader(f"Caso: {casos[st.session_state.caso][1]}")
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
