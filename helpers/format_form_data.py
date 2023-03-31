import streamlit as st
import datetime

def format_form_data():
    format_form_data_cmps()
    format_form_data_date()
    format_form_data_complain()
    st.session_state.formated = True
    st.experimental_rerun()


def format_form_data_complain():
    st.session_state.client['Complain'] = 1 if st.session_state.client['Complain'] else 0


def format_form_data_date():
    date = st.session_state.client['Time_Customer']
    today = datetime.date.today()
    date = today - date
    st.session_state.client['Time_Customer'] = date.days / 365.25
    
def format_form_data_cmps():
    st.session_state.client['AcceptedCmp1'] = 0
    st.session_state.client['AcceptedCmp2'] = 0
    st.session_state.client['AcceptedCmp3'] = 0
    st.session_state.client['AcceptedCmp4'] = 0
    st.session_state.client['AcceptedCmp5'] = 0

    if 'AcceptedCmp1' in st.session_state.client['cmps']:
        st.session_state.client['AcceptedCmp1'] = 1

    if 'AcceptedCmp2' in st.session_state.client['cmps']:
        st.session_state.client['AcceptedCmp2'] = 1

    if 'AcceptedCmp3' in st.session_state.client['cmps']:
        st.session_state.client['AcceptedCmp3'] = 1

    if 'AcceptedCmp4' in st.session_state.client['cmps']:
        st.session_state.client['AcceptedCmp4'] = 1

    if 'AcceptedCmp5' in st.session_state.client['cmps']:
        st.session_state.client['AcceptedCmp5'] = 1
    st.session_state.client.pop('cmps')