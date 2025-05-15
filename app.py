import streamlit as st

st.title("Minihistoria Interactiva - Exblifep en infección BLEE (Visita PROA)")

st.markdown("""
👨‍⚕️ Te reúnes con un clínico del equipo PROA para comentar un caso reciente de infección grave por BLEE.

🧑‍⚕️ **El clínico te comenta**:
> “Tenemos un paciente en planta con sepsis de origen urinario. Tiene antecedentes de colonización por BLEE y alergia a penicilinas. Estamos planteando la terapia empírica.”
""")

st.subheader("¿Qué enfoque propones tú como visitador médico de Exblifep?")
opcion = st.radio(
    "Selecciona una opción:",
    [
        "A. Carbapenémico (meropenem), es lo más seguro.",
        "B. Piperacilina/tazobactam, aunque haya BLEE, si es ITU puede valer.",
        "C. Exblifep: buena cobertura frente a BLEE, alternativa al carbapenem, y no afecta tanto al microbioma."
    ]
)

if opcion:
    st.markdown("### ✅ Feedback:")

    if opcion.startswith("A"):
        st.error("""
Aunque los carbapenémicos son eficaces frente a BLEE, su uso indiscriminado se asocia a mayor selección de resistencias, especialmente carbapenemasas. PROA busca alternativas cuando es posible.
""")
    elif opcion.startswith("B"):
        st.warning("""
Piperacilina/tazobactam no es fiable frente a BLEE, incluso en ITUs. Hay riesgo de fallo clínico y microbiológico. Además, hay alergia a penicilinas.
""")
    elif opcion.startswith("C"):
        st.success("""
💡 ¡Buena propuesta! Exblifep es activo frente a BLEE y AmpC, y en infecciones graves (como esta ITU complicada con sepsis) es una alternativa válida al carbapenem.

✔️ Evita el uso de carbapenémicos  
✔️ Tiene buena penetración urinaria  
✔️ Su perfil de seguridad y su menor impacto ecológico son ventajas clave en contexto PROA
""")
        
st.markdown("---")
st.info("Este es el primer caso. En futuras versiones podrás continuar con nuevos escenarios clínicos.")
