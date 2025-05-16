
import streamlit as st

st.set_page_config(page_title="Entrenamiento clínico", layout="centered")

casos = {
    "EXB1": "Exblifep - ITU complicada con BLEE",
    "EXB2": "Exblifep - NAC nosocomial + BLEE",
    "EXB3": "Exblifep - Bacteriemia sin foco",
    "EXB4": "Exblifep - Postquirúrgico abdominal + AmpC",
    "EXB5": "Exblifep - ITU + OXA-48",
    "EXB6": "Exblifep - Pielonefritis con alergia múltiple",
    "EXB7": "Exblifep - Infección intraabdominal complicada",
    "EXB8": "Exblifep - Rotación antibiótica en planta",
    "EXB9": "Exblifep - Sepsis urinaria con mal control glucémico",
    "EXB10": "Exblifep - ITU en paciente paliativo",
    "ZEV1": "Zevtera - NAC grave + S. pneumoniae",
    "ZEV2": "Zevtera - Neumonía nosocomial con SARM",
    "ZEV3": "Zevtera - Bacteriemia por SCN",
    "ZEV4": "Zevtera - Endocarditis por S. aureus",
    "ZEV5": "Zevtera - Celulitis en inmunodeprimido",
    "ZEV6": "Zevtera - VIH + NAC moderada",
    "ZEV7": "Zevtera - Hemodiálisis con S. aureus",
    "ZEV8": "Zevtera - Neumonía postintubación",
    "ZEV9": "Zevtera - Osteomielitis por SARM",
    "ZEV10": "Zevtera - NAC con alergia a glicopéptidos"
}

if "caso" not in st.session_state:
    st.session_state.caso = None
    st.session_state.step = 0

def feedback(color, texto):
    if color == "verde":
        st.success("🟢 " + texto)
    elif color == "amarillo":
        st.warning("🟡 " + texto)
    elif color == "rojo":
        st.error("🔴 " + texto)

# Menú inicial
if st.session_state.caso is None:
    st.title("🧪 Entrenamiento clínico interactivo")
    seleccion = st.selectbox("Selecciona un caso:", [""] + [f"{k} - {v}" for k, v in casos.items()])
    if seleccion and st.button("Iniciar caso"):
        st.session_state.caso = seleccion.split(" - ")[0]
        st.session_state.step = 0
        st.rerun()

# Diccionario con todos los pasos de los 20 casos (resumen simulado aquí)
pasos = {
    "EXB1": [
        ("Paciente con sepsis urinaria y BLEE previa. ¿Empírico?", ["Meropenem", "Pip/tazo", "Exblifep"],
         ["rojo", "amarillo", "verde"],
         ["Uso innecesario de carbapenem.", "Cobertura inadecuada.", "Alternativa válida a carbapenem."]),
        ("Cultivo: BLEE sensible a cotrimoxazol. ¿Ajuste?", ["Mantener Exblifep", "Cambiar a oral", "Suspender"],
         ["amarillo", "verde", "rojo"],
         ["Podría mantenerse si no hay vía oral.", "Buena opción si tolera oral.", "Suspensión prematura."]),
        ("¿Duración total?", ["3 días", "7 días", "14 días"],
         ["rojo", "verde", "amarillo"],
         ["Insuficiente.", "Duración adecuada.", "Podría ser excesivo."]),
        ("¿Plan al alta?", ["Nada", "Cotrimoxazol oral", "Exblifep domiciliario"],
         ["rojo", "verde", "amarillo"],
         ["Alta sin completar puede ser riesgosa.", "Correcto si tolera oral.", "Menos práctico en domicilio."])
    ]
    # Los 19 casos restantes se incluirían aquí con su narrativa y pasos detallados
}

# Renderizado
if st.session_state.caso:
    st.title(f"🧾 Caso: {casos[st.session_state.caso]}")
    secuencia = pasos.get(st.session_state.caso, [])
    if st.session_state.step < len(secuencia):
        pregunta, opciones, colores, textos = secuencia[st.session_state.step]
        opcion = st.radio(f"**{pregunta}**", opciones, index=None)
        if opcion:
            idx = opciones.index(opcion)
            feedback(colores[idx], textos[idx])
            st.button("Siguiente", on_click=lambda: st.session_state.update(step=st.session_state.step + 1))
    else:
        st.success("🎉 ¡Caso completado!")
        if st.button("Volver al menú"):
            st.session_state.caso = None
            st.session_state.step = 0
            st.rerun()
