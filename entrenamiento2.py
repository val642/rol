
import streamlit as st

st.set_page_config(page_title="Entrenamiento clínico interactivo", layout="centered")

casos = {
    "EXB1": ("Exblifep", "ITU complicada con BLEE"),
    "EXB2": ("Exblifep", "NAC nosocomial + BLEE"),
    "EXB3": ("Exblifep", "Bacteriemia sin foco"),
    "EXB4": ("Exblifep", "Postquirúrgico abdominal + AmpC"),
    "EXB5": ("Exblifep", "ITU + OXA-48 sospechada"),
    "EXB6": ("Exblifep", "Pielonefritis con alergia múltiple"),
    "EXB7": ("Exblifep", "Infección intraabdominal complicada"),
    "EXB8": ("Exblifep", "Rotación antibiótica en planta"),
    "EXB9": ("Exblifep", "Sepsis urinaria mal control glucémico"),
    "EXB10": ("Exblifep", "ITU en paciente paliativo"),
    "ZEV1": ("Zevtera", "NAC grave + S. pneumoniae resistente"),
    "ZEV2": ("Zevtera", "Neumonía nosocomial con SARM"),
    "ZEV3": ("Zevtera", "Bacteriemia por coagulasa negativa"),
    "ZEV4": ("Zevtera", "Endocarditis derecha por S. aureus sensible"),
    "ZEV5": ("Zevtera", "Celulitis grave en inmunodeprimido"),
    "ZEV6": ("Zevtera", "Paciente con GESIDA + NAC moderada"),
    "ZEV7": ("Zevtera", "S. aureus en hemodiálisis"),
    "ZEV8": ("Zevtera", "Neumonía postintubación"),
    "ZEV9": ("Zevtera", "Osteomielitis por SARM"),
    "ZEV10": ("Zevtera", "NAC con alergia a glicopéptidos")
}

pasos = {
    "EXB1": [
        ("👨‍⚕️ El médico te comenta: Paciente con sepsis urinaria BLEE y alergia a penicilinas. ¿Qué propones?", 
        ["Meropenem", "Pip/tazo", "Exblifep"], 
        ["rojo", "amarillo", "verde"], 
        ["Evita meropenem si puedes.", "Pip/tazo no es ideal con BLEE + alergia.", "Exblifep es seguro y eficaz."]),
        ("🧪 El cultivo confirma BLEE. ¿Ajuste?", 
        ["Mantener Exblifep", "Suspender antibiótico", "Cambiar a oral"], 
        ["verde", "rojo", "amarillo"], 
        ["Correcto si estable.", "Riesgoso.", "Solo si tolera y es estable."]),
        ("⏱️ ¿Duración propuesta?", 
        ["3 días", "7 días", "14 días"], 
        ["rojo", "verde", "amarillo"], 
        ["Muy corto.", "Adecuado.", "Podría ser excesivo."]),
        ("🏠 Al alta, ¿plan?", 
        ["Nada", "Cotrimoxazol", "Exblifep domiciliario"], 
        ["rojo", "verde", "amarillo"], 
        ["Insuficiente.", "Buena opción si tolera oral.", "Menos práctico."])
    ],
    "ZEV1": [
        ("📋 NAC grave en urgencias con sospecha de S. pneumoniae resistente. ¿Empírico?", 
        ["Levofloxacino", "Vancomicina", "Ceftobiprole"], 
        ["rojo", "amarillo", "verde"], 
        ["Fluoroquinolona no cubre bien.", "Vancomicina sin betalactámico es incompleto.", "Buena opción empírica."]),
        ("🧪 Se aísla S. pneumoniae resistente a penicilina. ¿Ajuste?", 
        ["Mantener ceftobiprole", "Suspender y alta", "Escalar a linezolid"], 
        ["verde", "rojo", "rojo"], 
        ["Correcto.", "Alta precoz.", "Linezolid innecesario."]),
        ("💉 ¿Duración propuesta?", 
        ["2 días", "5 días", "10 días"], 
        ["rojo", "verde", "amarillo"], 
        ["Muy corto.", "Adecuado.", "Largo salvo complicaciones."]),
        ("📤 ¿Seguimiento?", 
        ["Alta sin más", "Revisión en 48h", "Reingreso a hospitalización"], 
        ["rojo", "verde", "amarillo"], 
        ["Falta control.", "Correcto.", "No necesario."])
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
