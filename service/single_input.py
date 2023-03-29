
import streamlit as st
import numpy as np
import datetime


def single_consult_form():
    with st.form("Single Consult"):

        client = {}
        
        st.subheader("Client Info")
        col1,col2,col3,col4 =  st.columns(4)
        with col1:
            client['age'] = st.number_input("Age",step=1)
        with col2:
            client['income'] = st.number_input("Income",step=0.01)
        with col3:
            client['kids'] = st.number_input("Number Of Kids",step=1)
        with col4:
            client['teens'] = st.number_input("Number Of Teens",step=1)
        
        
        
        col5,col6,col7 =  st.columns([1,1,2])
        with col5:
            client['education'] = st.selectbox(
                'Education Level',
                options=['Basic','2n Cycle','Graduation','Master','Doctor']
            )
        with col6:
            client['marital'] = st.selectbox(
                'Marital Status',
                options=['Single','Married','Together','Divorced','Widow']
            )
        with col7:
            client['cmps'] = st.multiselect(
                        'Accepted Cmps',
                        ['Cmp1', 'Cmp2', 'Cmp3', 'Cmp4','Cmp5'])
        
    
        client['registered'] = st.date_input(
            "Date registered",
            datetime.date(2019, 7, 6))
        
        client['complain'] = st.checkbox("Recent Complain")
            
        
        st.subheader('Spents')
        col1,col2,col3,col4,col5,col6 =  st.columns(6)
        
        with col1:
            client['spent_fish'] = st.number_input("Fish",step=0.01)
        with col2:
            client['spent_fruits'] = st.number_input("Fruits",step=0.01)
        with col3:
            client['spent_goldprods'] = st.number_input("GoldProds",step=0.01)
        with col4:
            client['spent_meat'] = st.number_input("Meat",step=0.01)
        with col5:
            client['spent_sweet'] = st.number_input("Sweet",step=0.01)
        with col6:
            client['spent_Wines'] = st.number_input("Wines",step=0.01)

        
        st.subheader("Purchases Info")
        col1,col2,col3, = st.columns(3)
        with col1:
            client['cata_pur'] = st.number_input("NumCatalogPurchases",step=1)
        with col2:
            client['deals_pur'] = st.number_input("NumDealsPurchases",step=1)
        with col3:
            client['store_pur'] = st.number_input("NumStorePurchases",step=1)

        col1,col2,col3, = st.columns(3)
        with col1:
            client['web_pur'] = st.number_input("NumWebPurchases",step=1)
        with col2:
            client['web_vis'] = st.number_input("NumWebVisitsMonth",step=1)
        with col3:
            client['Recency'] = st.number_input("DaysLastPurchase",step=1)

        
        

        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.client = client
            st.session_state.formated = False
            st.experimental_rerun()



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