import streamlit as st
import pandas as pd
import numpy as np
from pycaret.classification import *

from service.model import predict
from helpers.plot import *

def csv_pred(file):

    Xtest = pd.read_csv(file)
    ypred = predict(Xtest)

    with st.expander('Visualizar CSV carregado:', expanded = True):
        c1, _ = st.columns([2,4])
        qtd_linhas = c1.slider('Visualizar quantas linhas do CSV:', 
                                min_value = 5, 
                                max_value = Xtest.shape[0], 
                                step = 10,
                                value = 5)
        st.dataframe(Xtest.head(qtd_linhas))

    with st.expander('Visualizar Predições:', expanded = False):
        c1, _, c2, c3 = st.columns([2,.5,1,1])
        treshold = c1.slider('Treshold (ponto de corte para considerar predição como True)',
                            min_value = 0.0,
                            max_value = 1.0,
                            step = .1,
                            value = .5)
        qtd_true = ypred.loc[ypred['prediction_score_1'] > treshold].shape[0]
        ypred['prediction_label'] = ypred['prediction_score_1'].apply(lambda x: 1 if x > treshold else 0)

        c2.metric('Qtd clientes True', value = qtd_true)
        c3.metric('Qtd clientes False', value = len(ypred) - qtd_true)

        tipo_view = st.radio('', ('Completo', 'Apenas predições'))
        df_view = pd.DataFrame(ypred.iloc[:,-1].copy())

        def color_pred(val):
          color = '#65ab65' if val > treshold else '#fa8373'
          return f'background-color: {color}'
        
        if tipo_view == 'Completo': df_view = ypred.copy()

        st.dataframe(df_view.style.applymap(color_pred, subset = ['prediction_score_1']))

        csv = df_view.to_csv(sep = ';', decimal = ',', index = True)
        st.markdown(f'Shape do CSV a ser baixado: {df_view.shape}')
        st.download_button(label = 'Download CSV',
                        data = csv,
                        file_name = 'Predicoes.csv',
                        mime = 'text/csv')
        


    if treshold != 0 and treshold != 1:
        with st.expander('Plots', expanded=True):
            plot_type = st.radio('',('Absolute values','Relative values'))
            ypred_dataframe = pd.DataFrame(ypred)
            
            education_marital_plots(plot_type,ypred_dataframe)
            
            # plot 3

            purchase_campaign_plots(plot_type,ypred_dataframe)
            