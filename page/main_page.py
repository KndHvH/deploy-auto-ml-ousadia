import streamlit as st

LOGO_PATH='./images/logo_fiap.png'

def page_cfg():

    st.set_page_config( page_title = 'Simulador - Case Ifood - Grupo OusadIa',
                    page_icon = LOGO_PATH,
                    layout='centered',
                    initial_sidebar_state = 'expanded')

    st.markdown("""
                <style>
                    button.step-up {display: none;}
                    button.step-down {display: none;}
                    div[data-baseweb] {border-radius: 4px;}
                    .css-1y4p8pa {
                      width: 100%;
                      padding: 6rem 1rem 10rem;
                      max-width: 60rem;
                    }
                </style>""",
                unsafe_allow_html=True)
