
# entrenamiento_exb5.py
# Archivo funcional con 5 casos clínicos completos de Exblifep
# Incluye historia clínica, decisiones tipo rol, feedback con colores, diálogo clínico y referencias

import streamlit as st

st.set_page_config(page_title="Casos Exblifep", layout="centered")

casos = {
    "EXB1": "Sepsis urinaria por BLEE en paciente pluripatológico",
    "EXB2": "NAC nosocomial por BLEE en paciente con EPOC",
    "EXB3": "Bacteriemia secundaria a ITU en paciente institucionalizado",
    "EXB4": "Peritonitis postquirúrgica por AmpC en cirugía digestiva",
    "EXB5": "ITU en paciente con aislamiento previo de OXA-48"
}

pasos = {
    "EXB1": [
        ("""🧍‍♂️ Hombre de 72 años, DM2, EPOC, HTA. Ingresa por fiebre alta, hipotensión y desorientación. Antecedente reciente de infección urinaria por E. coli BLEE. Alergia no anafiláctica a amoxicilina.

👨‍⚕️ Médico: «Podría ser una sepsis de origen urinario. ¿Qué pondrías de forma empírica?»""",
        ["Meropenem", "Piperacilina/tazobactam", "Exblifep"],
        ["rojo", "amarillo", "verde"],
        ["Reservado para casos extremos.",
         "No adecuado frente a BLEE.",
         "Alternativa recomendada por IPT y estudio ALLIUM."])
    ],
    "EXB2": [
        ("""🧍‍♂️ Varón de 67 años con EPOC GOLD D. Ingresa por neumonía con infiltrado lobar y criterios de gravedad. Cultivo previo de BLEE en esputo. No alergias.

👨‍⚕️ PROA: «¿Carba otra vez? ¿Qué propones empíricamente?»""",
        ["Meropenem", "Exblifep", "Ceftriaxona"],
        ["amarillo", "verde", "rojo"],
        ["Solo si no hay otra opción.",
         "Buena alternativa para BLEE respiratorio.",
         "No cubre BLEE."])
    ],
    "EXB3": [
        ("""🧓 Mujer de 84 años, institucionalizada, ITU recurrente, portadora de sonda vesical. Fiebre y deterioro del nivel de conciencia. Antecedente de E. coli BLEE. Toma crónica de ADO.

👩‍⚕️ Internista: «Inestable. ¿Qué antibiótico usarías mientras llegan los cultivos?»""",
        ["Cefepima", "Exblifep", "Ciprofloxacino"],
        ["rojo", "verde", "amarillo"],
        ["Insuficiente contra BLEE.",
         "Adecuado y seguro.",
         "Riesgo alto de resistencia."])
    ],
    "EXB4": [
        ("""🧑‍⚕️ Paciente de 58 años, operado de colon perforado hace 48h. Reingresa por fiebre, dolor abdominal y leucocitosis. Cultivos anteriores con Enterobacter spp.

👨‍⚕️ Cirujano: «Esto huele a peritonitis postqx. ¿Cubres AmpC sin meropenem?»""",
        ["Piperacilina/tazobactam", "Ertapenem", "Exblifep"],
        ["rojo", "amarillo", "verde"],
        ["Insuficiente por riesgo AmpC.",
         "Buena alternativa pero de reserva.",
         "Cubres AmpC sin carbapenémico."])
    ],
    "EXB5": [
        ("""👴 Hombre de 75 años con prostatitis recurrente, BLEE y OXA-48 en orina en los últimos meses. Ingresa por fiebre y disuria. No tolera quinolonas.

👨‍⚕️ Urólogo: «OXA-48 otra vez... ¿qué propones mientras esperamos cultivo?»""",
        ["Ceftazidima-avibactam", "Exblifep", "Pip/tazo"],
        ["verde", "verde", "rojo"],
        ["Alternativa válida para OXA-48.",
         "Buena cobertura según IPT.",
         "No cubre OXA-48."])
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
