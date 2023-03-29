import streamlit as st

def format_form_data():
    format_form_data_cmps()
    format_form_data_date()
    format_form_data_complain()
    st.session_state.formated = True
    st.experimental_rerun()


def format_form_data_complain():
    st.session_state.client['complain'] = 1 if st.session_state.client['complain'] else 0


def format_form_data_date():
    date = st.session_state.client['registered']
    today = datetime.date.today()
    date = today - date
    st.session_state.client['registered'] = date.days / 365.25
    
def format_form_data_cmps():
    st.session_state.client['Cmp1'] = 0
    st.session_state.client['Cmp2'] = 0
    st.session_state.client['Cmp3'] = 0
    st.session_state.client['Cmp4'] = 0
    st.session_state.client['Cmp5'] = 0

    if 'Cmp1' in st.session_state.client['cmps']:
        st.session_state.client['Cmp1'] = 1

    if 'Cmp2' in st.session_state.client['cmps']:
        st.session_state.client['Cmp2'] = 1

    if 'Cmp3' in st.session_state.client['cmps']:
        st.session_state.client['Cmp3'] = 1

    if 'Cmp4' in st.session_state.client['cmps']:
        st.session_state.client['Cmp4'] = 1

    if 'Cmp5' in st.session_state.client['cmps']:
        st.session_state.client['Cmp5'] = 1
    st.session_state.client.pop('cmps')