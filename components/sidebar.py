import streamlit as st

def sidebar():
    file = None
    with st.sidebar:
        c1, c2 = st.columns(2)
        c1.image('./images/logo_fiap.png', width = 100)
        c2.write('')
        c2.subheader('Auto ML - Fiap [v1.1-OuIa]')

        database = st.radio('Fonte dos dados de entrada (X):', ('CSV', 'Online'))

        if database == 'CSV':
            st.info('Upload do CSV')
            file = st.file_uploader('Selecione o arquivo CSV', type='csv')
            
    return database, file