
import streamlit as st

from cache.session_state import init_session_state
from components.sidebar import sidebar
from components.csv_input import csv_pred
from components.single_input import single_consult_form, single_consult_predict
from helpers.format_form_data import format_form_data
from page.main_page import page_cfg

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

    
        single_consult_predict()


    
        if st.button('New Submit'):
            st.session_state.client = None
            st.experimental_rerun()
    