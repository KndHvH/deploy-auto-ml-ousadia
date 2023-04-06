import streamlit as st
import pandas as pd
import datetime

from service.model import predict

def single_consult_form():
    with st.form("Single Consult"):

        client = {}
        
        st.subheader("Client Info")
        col1,col2,col3,col4 =  st.columns(4)
        with col1:
            client['Age'] = st.number_input("Age",step=1, min_value=0, max_value=100)
        with col2:
            client['Income'] = st.number_input("Income",step=0.01)
        with col3:
            client['Kidhome'] = st.number_input("Number Of Kids",step=1, min_value=0, max_value=15)
        with col4:
            client['Teenhome'] = st.number_input("Number Of Teens",step=1, min_value=0, max_value=15)
        
        
        
        col5,col6,col7 =  st.columns([1,1,2])
        with col5:
            client['Education'] = st.selectbox(
                'Education Level',
                options=['Basic','2n Cycle','Graduation','Master','Doctor']
            )
        with col6:
            client['Marital_Status'] = st.selectbox(
                'Marital Status',
                options=['Single','Married','Together','Divorced','Widow']
            )
        with col7:
            client['cmps'] = st.multiselect(
                        'Accepted Cmps',
                        ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4','AcceptedCmp5'])
        
    
        client['Time_Customer'] = st.date_input(
            "Date registered",
            datetime.date(2019, 7, 6))
        
        client['Complain'] = st.checkbox("Recent Complain")
            
        
        st.subheader('Spents')
        col1,col2,col3,col4,col5,col6 =  st.columns(6)
        
        with col1:
            client['MntFishProducts'] = st.number_input("Fish",step=0.01)
        with col2:
            client['MntFruits'] = st.number_input("Fruits",step=0.01)
        with col3:
            client['MntGoldProds'] = st.number_input("GoldProds",step=0.01)
        with col4:
            client['MntMeatProducts'] = st.number_input("Meat",step=0.01)
        with col5:
            client['MntSweetProducts'] = st.number_input("Sweet",step=0.01)
        with col6:
            client['MntWines'] = st.number_input("Wines",step=0.01)

        
        st.subheader("Purchases Info")
        col1,col2,col3, = st.columns(3)
        with col1:
            client['NumCatalogPurchases'] = st.number_input("NumCatalogPurchases",step=1)
        with col2:
            client['NumDealsPurchases'] = st.number_input("NumDealsPurchases",step=1)
        with col3:
            client['NumStorePurchases'] = st.number_input("NumStorePurchases",step=1)

        col1,col2,col3, = st.columns(3)
        with col1:
            client['NumWebPurchases'] = st.number_input("NumWebPurchases",step=1)
        with col2:
            client['NumWebVisitsMonth'] = st.number_input("NumWebVisitsMonth",step=1)
        with col3:
            client['Recency'] = st.number_input("DaysLastPurchase",step=1)

        
        

        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.client = client
            st.session_state.formated = False
            st.experimental_rerun()


def single_consult_predict():

    Xtest = pd.DataFrame(st.session_state.client, index=[0])
    ypred = predict(Xtest)


    with st.expander('Visualizar Form carregado:', expanded = False):
        st.dataframe(Xtest)


    with st.expander('Visualizar Predição:', expanded = True):
        c1, _, _, c3 = st.columns([2,.5,.5,1.5])
        treshold = c1.slider('Treshold (ponto de corte para considerar predição como True)',
                            min_value = 0.0,
                            max_value = 1.0,
                            step = .1,
                            value = .5)
        result = ypred.loc[ypred['prediction_score_1'] > treshold].shape[0]

        c3.markdown(f'# **{result==1}**')

        tipo_view = st.radio('', ('Completo', 'Apenas predições'))
        df_view = pd.DataFrame(ypred.iloc[:,-1].copy())
        
        if tipo_view == 'Completo': df_view = ypred.copy()

        st.dataframe(df_view)

    