
import streamlit as st

from service.csv_input import csv_pred
from service.session_state import init_session_state
from service.single_input import format_form_data, single_consult_form
from service.streamlit_page import page_cfg,sidebar

init_session_state()
page_cfg()

st.title('Simulador - Conversão de Vendas')

database, file = sidebar()



if database == 'CSV':
    if file: csv_pred(file)
    else: st.warning('Arquivo CSV não foi carregado')
        

if database == 'Online':
    if st.session_state.client is None:
        single_consult_form()

    else:
        if not st.session_state.formated:
            format_form_data()
            
        if st.button('Delete Form'):
            st.session_state.client = None
            st.experimental_rerun()
    