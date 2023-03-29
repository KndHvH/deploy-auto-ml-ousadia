import streamlit as st

def init_session_state():
    if 'client' not in st.session_state:
        st.session_state.client = None
    if 'formated' not in st.session_state:
        st.session_state.formated = False