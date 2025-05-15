import streamlit as st

# Iniciar el estado si es la primera vez
if "step" not in st.session_state:
    st.session_state.step = 1

st.title("🧪 Minihistoria interactiva - Caso Exblifep (flujo por decisiones)")

# -------- PANTALLA 1 --------
if st.session_state.step == 1:
    st.markdown("### 🧍‍♂️ Escenario clínico")
    st.write("Paciente ingresado en planta con sepsis de origen urinario, colonizado por BLEE y con alergia a penicilinas. El equipo está valorando el tratamiento empírico.")
    
    opcion = st.radio(
        "¿Qué propones como tratamiento empírico?",
        ["A. Meropenem", 
         "B. Piperacilina/tazobactam", 
         "C. Exblifep (cefepime/enmetazobactam)"],
        index=None
    )

    if opcion:
        st.markdown("#### ✅ Feedback:")
        if opcion.startswith("A"):
            st.error("Meropenem es eficaz, pero su uso indiscriminado favorece la aparición de resistencias. Se busca evitar carbapenémicos cuando sea posible.")
        elif opcion.startswith("B"):
            st.warning("Piperacilina/tazobactam no es fiable frente a BLEE, especialmente en sepsis, y el paciente tiene alergia a penicilinas.")
        elif opcion.startswith("C"):
            st.success("¡Buena elección! Exblifep es activo frente a BLEE y AmpC. Buena penetración urinaria, menor impacto ecológico y alternativa a carbapenémicos.")
        st.button("Siguiente", on_click=lambda: st.session_state.update(step=2))

# -------- PANTALLA 2 --------
elif st.session_state.step == 2:
    st.markdown("### 📋 Evolución del caso")
    st.write("Tras 48 h de tratamiento con Exblifep, el paciente mejora clínicamente. El urocultivo confirma E. coli BLEE, sensible a cotrimoxazol y nitrofurantoína.")

    opcion = st.radio(
        "¿Cambiarías el tratamiento en este momento?",
        ["A. Mantener Exblifep", 
         "B. Cambiar a cotrimoxazol oral", 
         "C. Suspender antibióticos"],
        index=None
    )

    if opcion:
        st.markdown("#### ✅ Feedback:")
        if opcion.startswith("A"):
            st.warning("Mantener Exblifep no está justificado si hay alternativa oral, el paciente mejora y está estable.")
        elif opcion.startswith("B"):
            st.success("Correcto. Puede desescalarse a cotrimoxazol oral si es sensible y hay buena respuesta clínica.")
        elif opcion.startswith("C"):
            st.error("Suspender antibióticos tan pronto no sería prudente. Es preferible ajustar tratamiento, no suspenderlo del todo.")
        st.button("Siguiente", on_click=lambda: st.session_state.update(step=3))

# -------- PANTALLA 3 --------
elif st.session_state.step == 3:
    st.markdown("### 🧾 Alta hospitalaria")
    st.write("El paciente sigue estable y se plantea el alta. ¿Qué pauta antibiótica completarías en casa?")

    opcion = st.radio(
        "Escoge la opción más adecuada:",
        ["A. Completar 10 días con Exblifep", 
         "B. Finalizar tras 3 días IV por buena evolución", 
         "C. Cambiar a cotrimoxazol oral para completar 7 días"],
        index=None
    )

    if opcion:
        st.markdown("#### ✅ Feedback:")
        if opcion.startswith("A"):
            st.error("No tiene sentido continuar un antibiótico IV como Exblifep en casa si hay opción oral segura.")
        elif opcion.startswith("B"):
            st.warning("Aunque la evolución es buena, lo más habitual es completar al menos 7 días, ajustando a evolución.")
        elif opcion.startswith("C"):
            st.success("Opción adecuada. Cambio a oral con actividad y duración razonable ajustada a la evolución clínica.")
        st.button("Ver resumen final", on_click=lambda: st.session_state.update(step=4))

# -------- PANTALLA FINAL --------
elif st.session_state.step == 4:
    st.success("🎉 ¡Caso completado!")
    st.markdown("### 📚 Resumen de aprendizaje:")
    st.markdown("""
- 💊 Exblifep es una opción empírica válida frente a BLEE con alergia a betalactámicos.
- 🧪 La desescalada a tratamiento oral debe realizarse si hay respuesta clínica y sensibilidad.
- 🏠 El alta con antibiótico oral activo permite completar tratamiento en casa sin riesgo innecesario.
""")
    if st.button("Volver a empezar"):
        st.session_state.step = 1
