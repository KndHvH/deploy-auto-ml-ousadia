import streamlit as st


def page_cfg():

    st.set_page_config( page_title = 'Simulador - Case Ifood - Grupo OusadIa',
                    page_icon = './images/logo_fiap.png',
                    layout='centered',
                    initial_sidebar_state = 'expanded')

    st.markdown("""
                <style>
                    button.step-up {display: none;}
                    button.step-down {display: none;}
                    div[data-baseweb] {border-radius: 4px;}
                </style>""",
                unsafe_allow_html=True)

    


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