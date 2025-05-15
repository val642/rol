import streamlit as st

st.title('Exblifep - NAC nosocomial con colonización BLEE (PROA escéptico)')
if 'step' not in st.session_state:
    st.session_state.step = 0

if st.session_state.step == 0:
    st.markdown('### Paso 1')
    st.write('''Paciente con neumonía nosocomial, colonización por BLEE previa. ¿Empírico?''')
    opcion = st.radio('Selecciona una opción:', ['A. Meropenem', 'B. Exblifep', 'C. Ceftriaxona'], index=None)
    if opcion:
        st.markdown('#### Feedback:')
        if opcion == 'A. Meropenem':
            st.write('''Correcto pero poco ecológico.''')
        if opcion == 'B. Exblifep':
            st.write('''Buena opción frente a BLEE, más ecológica.''')
        if opcion == 'C. Ceftriaxona':
            st.write('''Inadecuado si sospecha BLEE.''')
        st.button('Siguiente', on_click=lambda: st.session_state.update(step=1))

if st.session_state.step == 1:
    st.markdown('### Paso 2')
    st.write('''El PROA duda del uso de Exblifep. ¿Cómo respondes?''')
    opcion = st.radio('Selecciona una opción:', ['A. Explicas su espectro y respaldo clínico', 'B. Lo cambias a meropenem', 'C. Le ignoras'], index=None)
    if opcion:
        st.markdown('#### Feedback:')
        if opcion == 'A. Explicas su espectro y respaldo clínico':
            st.write('''Correcto, justificas uso racional.''')
        if opcion == 'B. Lo cambias a meropenem':
            st.write('''No demuestras valor del producto.''')
        if opcion == 'C. Le ignoras':
            st.write('''Mal enfoque ante el PROA.''')
        st.button('Siguiente', on_click=lambda: st.session_state.update(step=2))

if st.session_state.step == 2:
    st.markdown('### Paso 3')
    st.write('''Cultivo: BLEE sensible a carbapenémico. ¿Qué haces?''')
    opcion = st.radio('Selecciona una opción:', ['A. Cambias a meropenem', 'B. Mantienes Exblifep', 'C. Vas a piperacilina/tazo'], index=None)
    if opcion:
        st.markdown('#### Feedback:')
        if opcion == 'A. Cambias a meropenem':
            st.write('''Desescalar puede ser correcto.''')
        if opcion == 'B. Mantienes Exblifep':
            st.write('''Si responde bien, puede mantenerse.''')
        if opcion == 'C. Vas a piperacilina/tazo':
            st.write('''Riesgo si no cubre BLEE.''')
        st.button('Siguiente', on_click=lambda: st.session_state.update(step=3))

if st.session_state.step == 3:
    st.markdown('### Paso 4')
    st.write('''Evolución favorable. ¿Finalizas?''')
    opcion = st.radio('Selecciona una opción:', ['A. Sí, tras 7 días total', 'B. No, mantengo 14 días', 'C. Cambio a oral'], index=None)
    if opcion:
        st.markdown('#### Feedback:')
        if opcion == 'A. Sí, tras 7 días total':
            st.write('''Duración adecuada en NAC.''')
        if opcion == 'B. No, mantengo 14 días':
            st.write('''Demasiado largo.''')
        if opcion == 'C. Cambio a oral':
            st.write('''No siempre hay alternativa oral.''')
        st.button('Siguiente', on_click=lambda: st.session_state.update(step=4))

if st.session_state.step == 4:
    st.success('¡Caso completado!')
    if st.button('Volver a empezar'):
        st.session_state.step = 0
