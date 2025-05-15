import streamlit as st

st.title('Exblifep - ITU complicada BLEE (médico colaborador)')
if 'step' not in st.session_state:
    st.session_state.step = 0

if st.session_state.step == 0:
    st.markdown('### Paso 1')
    st.write('''Paciente con sepsis urinaria, BLEE conocida, sin alergias. ¿Antibiótico empírico?''')
    opcion = st.radio('Selecciona una opción:', ['A. Meropenem', 'B. Piperacilina/tazobactam', 'C. Exblifep (cefepime/enmetazobactam)'], index=None)
    if opcion:
        st.markdown('#### Feedback:')
        if opcion == 'A. Meropenem':
            st.write('''Uso innecesario de carbapenémico.''')
        if opcion == 'B. Piperacilina/tazobactam':
            st.write('''No cubre BLEE de forma fiable.''')
        if opcion == 'C. Exblifep (cefepime/enmetazobactam)':
            st.write('''Buena cobertura frente a BLEE y opción ecológica.''')
        st.button('Siguiente', on_click=lambda: st.session_state.update(step=1))

if st.session_state.step == 1:
    st.markdown('### Paso 2')
    st.write('''Cultivo confirma E. coli BLEE. ¿Ajustas el tratamiento?''')
    opcion = st.radio('Selecciona una opción:', ['A. Mantener Exblifep', 'B. Cambiar a meropenem', 'C. Cambiar a cotrimoxazol oral'], index=None)
    if opcion:
        st.markdown('#### Feedback:')
        if opcion == 'A. Mantener Exblifep':
            st.write('''Adecuado si respuesta clínica es buena.''')
        if opcion == 'B. Cambiar a meropenem':
            st.write('''No aporta más beneficio que Exblifep.''')
        if opcion == 'C. Cambiar a cotrimoxazol oral':
            st.write('''Solo si el paciente tolera oral.''')
        st.button('Siguiente', on_click=lambda: st.session_state.update(step=2))

if st.session_state.step == 2:
    st.markdown('### Paso 3')
    st.write('''El paciente mejora. ¿Desescalas?''')
    opcion = st.radio('Selecciona una opción:', ['A. Sí, a oral si es sensible', 'B. No, mantengo IV', 'C. Suspendo antibiótico'], index=None)
    if opcion:
        st.markdown('#### Feedback:')
        if opcion == 'A. Sí, a oral si es sensible':
            st.write('''Correcto si hay respuesta clínica y oral es viable.''')
        if opcion == 'B. No, mantengo IV':
            st.write('''Mantener IV puede ser innecesario.''')
        if opcion == 'C. Suspendo antibiótico':
            st.write('''Suspender totalmente es precipitado.''')
        st.button('Siguiente', on_click=lambda: st.session_state.update(step=3))

if st.session_state.step == 3:
    st.markdown('### Paso 4')
    st.write('''Plan de alta. ¿Qué haces?''')
    opcion = st.radio('Selecciona una opción:', ['A. Alta sin antibiótico', 'B. Completar oral 5 días', 'C. Mantener Exblifep en casa'], index=None)
    if opcion:
        st.markdown('#### Feedback:')
        if opcion == 'A. Alta sin antibiótico':
            st.write('''Riesgo de recaída.''')
        if opcion == 'B. Completar oral 5 días':
            st.write('''Buena opción si tolera oral.''')
        if opcion == 'C. Mantener Exblifep en casa':
            st.write('''IV en casa no siempre es factible.''')
        st.button('Siguiente', on_click=lambda: st.session_state.update(step=4))

if st.session_state.step == 4:
    st.success('¡Caso completado!')
    if st.button('Volver a empezar'):
        st.session_state.step = 0
