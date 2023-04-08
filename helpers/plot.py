import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

def create_bar_chart(x, y, title="", x_label="", y_label=""):
    plt.bar(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    return plt

def create_line_chart(x, y, title="", x_label="", y_label=""):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    return plt

def create_scatter_chart(x, y, title="", x_label="", y_label=""):
    plt.scatter(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    return plt


def education_marital_plots(plot_type, dataframe):
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    if plot_type == 'Absolute values':
        dataframe.groupby(['Education', 'prediction_label'])['prediction_label'].count().unstack().plot(kind='bar', ax=axs[0])
        axs[0].set_title('N° of Predictions by Education Level',pad=15)
        
        dataframe.groupby(['Marital_Status', 'prediction_label'])['prediction_label'].count().unstack().plot(kind='bar', ax=axs[1])
        axs[1].set_title('N° of Predictions by Marital Status',pad=15)


    else:
        prop_ed = dataframe.groupby(['Education'])['prediction_label'].value_counts(normalize=True).unstack()
        prop_ed *= 100
        prop_ed.plot(kind='bar', ax=axs[0])
        axs[0].set_title('Proportion of Predictions by Education Level',pad=15)
        
        prop_ma = dataframe.groupby(['Marital_Status'])['prediction_label'].value_counts(normalize=True).unstack()
        prop_ma *= 100
        prop_ma.plot(kind='bar', ax=axs[1])
        axs[1].set_title('Proportion of Predictions by Marital Status',pad=15)
        
        axs[0].set_ylabel('Percentage %')
        axs[1].set_ylabel('Percentage %')
        axs[0].set_ylim([0, 100])
        axs[1].set_ylim([0, 100])
        
    axs[0].set_xlabel('')
    axs[1].set_xlabel('')
    
    plt.style.use("classic")
    fig.subplots_adjust(wspace=0.5, hspace=0.2)
    fig.suptitle('')
    axs[0].legend(fontsize=12)
    axs[1].legend(fontsize=12)
    st.pyplot(fig, transparent=True)


def purchase_campaign_plots(plot_type, ypred_dataframe):
    cols = ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5']
    df_cols = ypred_dataframe[cols]

    df_grouped = df_cols.groupby(ypred_dataframe['prediction_label']).sum()

    if plot_type == 'Absolute values':
        fig, axs = plt.subplots(1, 2, figsize=(15, 8))

        labels = cols
        x = np.arange(len(labels))
        width = 0.35

        axs[0].bar(x - width/2, df_grouped.loc[0], width, label='Prediction = 0')
        axs[0].bar(x + width/2, df_grouped.loc[1], width, label='Prediction = 1')

        for i, v in enumerate(df_grouped.shape):
            axs[0].bar_label(axs[0].containers[i], label=str(v))

        axs[0].set_title('N° of Accepted Campaigns by Prediction Label',pad=20,fontdict={'fontsize':20})
        axs[0].set_xticks(x)
        axs[0].set_xticklabels(labels)
        axs[0].legend(fontsize=12)

        purchases_cols = ["NumDealsPurchases", "NumWebPurchases", "NumCatalogPurchases", "NumStorePurchases", "NumWebVisitsMonth"]
        df_purchases_cols = ypred_dataframe[purchases_cols]

        df_grouped = df_purchases_cols.groupby(ypred_dataframe['prediction_label']).sum()

        labels = purchases_cols
        x = np.arange(len(labels))
        width = 0.35

        axs[1].bar(x - width/2, df_grouped.loc[0], width, label='Prediction = 0')
        axs[1].bar(x + width/2, df_grouped.loc[1], width, width, label='Prediction = 1')

        for i, v in enumerate(df_grouped.shape):
            axs[1].bar_label(axs[1].containers[i], label=str(v))

        axs[1].set_title('Purchases Data by Prediction Label',pad=15,fontdict={'fontsize':20})
        axs[1].set_xticks(x)
        axs[1].set_xticklabels(labels)
        axs[1].legend(fontsize=12)

        
    else:
        fig, axs = plt.subplots(1, 2, figsize=(15, 8))

        prop_cam = df_cols.groupby(ypred_dataframe['prediction_label'])[cols].apply(lambda x: 100*x/float(x.sum()))
        prop_cam.plot(kind='bar', ax=axs[0])

        axs[0].set_title('Proportion of Accepted Campaigns by Prediction Label',pad=15,fontdict={'fontsize':20})
        axs[0].set_ylabel('Percentage %')
        axs[0].set_xlabel('')
        axs[0].set_ylim([0, 100])
        axs[0].legend(fontsize=12)

        prop_pur = df_purchases_cols.groupby(ypred_dataframe['prediction_label'])[purchases_cols].apply(lambda x: 100*x/float(x.sum()))
        prop_pur.plot(kind='bar', ax=axs[1])

        axs[1].set_title('Proportion of Purchases Data by Prediction Label',pad=15,fontdict={'fontsize':20})
        axs[1].set_ylabel('Percentage %')
        axs[1].set_xlabel('')
        axs[1].set_ylim([0, 100])
        axs[1].legend(fontsize=12)
    
    plt.style.use("classic")
    fig.subplots_adjust(wspace=0.5, hspace=0.2)
    fig.suptitle('')
    st.pyplot(fig, transparent=True)




