import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import pandas as pd
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

def add_value_labels(ax, spacing=5):
    for rect in ax.patches:
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        space = spacing
        align = 'bottom'

        if y_value < 0:
            space *= -1
            align = 'top'

        label = "{:.0f}".format(y_value)

        ax.annotate(
            label,                      
            (x_value, y_value),         
            xytext=(0, space),          
            textcoords="offset points", 
            ha='center',                
            va=align)                      

def calc_porcentage(df, cols, ref_col):
    results = {}

    for col in cols:
        group0 = df[df[ref_col] == 0]
        group1 = df[df[ref_col] == 1]

        spec00 = group0[group0[col] == 0]
        spec01 = group0[group0[col] == 1]

        spec10 = group1[group1[col] == 0]
        spec11 = group1[group1[col] == 1]

        perc00 = spec00.shape[0] / group0.shape[0] * 100
        perc01 = spec01.shape[0] / group0.shape[0] * 100

        perc10 = spec10.shape[0] / group1.shape[0] * 100
        perc11 = spec11.shape[0] / group1.shape[0] * 100

        col_perc = pd.Series([perc00, perc01, perc10, perc11], index=[f"{col}_00", f"{col}_01", f"{col}_10", f"{col}_11"])
        results[col] = col_perc
    
    return pd.DataFrame(results)                                       

def plot_porcentage(results):
    fig, ax = plt.subplots(figsize=(20, 8))

    x = [1, 1.5, 2, 2.5]
    initial_take_size = 0
    take_size = 4

    for column in results.columns:
      y = results[column][initial_take_size:take_size]

      ax.bar(x[0], y[0], label='Value = 0 to Predict = 0' if column == results.columns[0] else '', edgecolor='gray', linewidth=1, color='#EEC584')
      ax.bar(x[1], y[1], label='Value = 1 to Predict = 0' if column == results.columns[0] else '', edgecolor='gray', linewidth=1, color='#C8AB83')
      ax.bar(x[2], y[2], label='Value = 0 to Predict = 1' if column == results.columns[0] else '', edgecolor='gray', linewidth=1, color='#CACAAA')
      ax.bar(x[3], y[3], label='Value = 1 to Predict = 1' if column == results.columns[0] else '', edgecolor='gray', linewidth=1, color='#999973')

      x = [e + 3 for e in x]
      initial_take_size += 4
      take_size += 4
    
    ax.set_xticks([1.5, 4.5, 7.5, 10.5, 13.5])
    ax.set_xticklabels(results.columns, fontdict={'fontsize':12})
    ax.set_ylabel('Percentage')
    ax.legend(fontsize=12, frameon=True, edgecolor='black')
    

    add_value_labels(ax)

    plt.show()
    return fig

def time_customer_and_recency_plot(dataframe):
    
    plt.style.use("seaborn-v0_8-pastel")

    fig, axs = plt.subplots(1, 2, figsize=(14, 6))

    tick_labels = [0, 0.2, 0.4, 0.6, 0.8, 1]

    sns.lineplot(x='prediction_label', y='Time_Customer', data=dataframe, ax=axs[0])
    axs[0].set_title('Plot of Time Customer by Label', pad=15, fontdict={'fontsize':16})
    axs[0].set_xlabel('Time_Customer')
    axs[0].set_ylabel('Label')
    axs[0].set_yticklabels(tick_labels)
    axs[0].set_xticklabels(tick_labels)

    sns.boxplot(x='prediction_label', y='Recency', data=dataframe, ax=axs[1])
    axs[1].set_title('Boxplot of Recency by Label', pad=15, fontdict={'fontsize':16})
    axs[1].set_xlabel('Label')
    axs[1].set_ylabel('Recency')

    plt.grid(True)
    plt.show()
    fig.subplots_adjust(wspace=0.5, hspace=0.2)

    st.pyplot(plt, transparent=True) 

def education_marital_plots(plot_type, dataframe):
    
    plt.style.use("bmh")

    fig, axs = plt.subplots(1, 2, figsize=(20, 8))

    if plot_type == 'Absolute values':
        plot_dataframe_0 = dataframe.groupby(['Education', 'prediction_label'])['prediction_label'].count().unstack()
        plot_dataframe_0.plot(kind='bar', ax=axs[0])
        axs[0].set_title('N° of Predictions by Education Level',pad=15, fontdict={'fontsize':20})
        axs[0].set_xticklabels(plot_dataframe_0.index, rotation=45)

        add_value_labels(axs[0])
        
        plot_dataframe_1 = dataframe.groupby(['Marital_Status', 'prediction_label'])['prediction_label'].count().unstack()
        plot_dataframe_1.plot(kind='bar', ax=axs[1])
        axs[1].set_title('N° of Predictions by Marital Status',pad=15, fontdict={'fontsize':20})
        axs[1].set_xticklabels(plot_dataframe_1.index, rotation=45)

        add_value_labels(axs[1])


    else:
        prop_ed = dataframe.groupby(['Education'])['prediction_label'].value_counts(normalize=True).unstack()
        prop_ed *= 100
        prop_ed.plot(kind='bar', ax=axs[0])
        axs[0].set_title('Proportion of Predictions by Education Level',pad=15, fontdict={'fontsize':20})
        axs[0].set_xticklabels(prop_ed.index, rotation=45, fontdict={'fontsize':12})

        add_value_labels(axs[0])

        prop_ma = dataframe.groupby(['Marital_Status'])['prediction_label'].value_counts(normalize=True).unstack()
        prop_ma *= 100
        prop_ma.plot(kind='bar', ax=axs[1])
        axs[1].set_title('Proportion of Predictions by Marital Status',pad=15, fontdict={'fontsize':20})
        
        axs[1].set_xticklabels(prop_ma.index, rotation=45, fontdict={'fontsize':12})

        add_value_labels(axs[1])

        axs[0].set_ylabel('Percentage %')
        axs[1].set_ylabel('Percentage %')
        
    axs[0].set_xlabel('')
    axs[1].set_xlabel('')
    
    fig.subplots_adjust(wspace=0.5, hspace=0.2)
    fig.suptitle('')
    axs[0].legend(fontsize=12)
    axs[1].legend(fontsize=12)
    plt.show()
    st.pyplot(fig, transparent=True)

def purchase_campaign_plots(plot_type, ypred_dataframe):
    
    plt.style.use("seaborn-v0_8-colorblind")

    cols = ['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5']
    df_cols = ypred_dataframe[cols]

    purchases_cols = ["NumDealsPurchases", "NumWebPurchases", "NumCatalogPurchases", "NumStorePurchases", "NumWebVisitsMonth"]
    df_purchases_cols = ypred_dataframe[purchases_cols]

    df_grouped = df_cols.groupby(ypred_dataframe['prediction_label']).sum()

    if plot_type == 'Absolute values':
        fig, axs = plt.subplots(1, 2, figsize=(20, 8))

        labels = cols
        x = np.arange(len(labels))
        width = 0.35

        axs[0].bar(x - width/2, df_grouped.loc[0], width, label='Prediction = 0')
        axs[0].bar(x + width/2, df_grouped.loc[1], width, label='Prediction = 1')

        for i, v in enumerate(df_grouped.shape):
            axs[0].bar_label(axs[0].containers[i], label=str(v))

        axs[0].set_title('N° of Accepted Campaigns by Prediction Label',pad=20,fontdict={'fontsize':20})
        axs[0].set_xticks(x)
        axs[0].set_xticklabels(labels, rotation=45)
        axs[0].legend(fontsize=12)

        df_grouped = df_purchases_cols.groupby(ypred_dataframe['prediction_label']).sum()
        labels = purchases_cols
        x = np.arange(len(labels))
        width = 0.35

        axs[1].bar(x - width/2, df_grouped.loc[0], width, label='Prediction = 0')
        axs[1].bar(x + width/2, df_grouped.loc[1], width, label='Prediction = 1')

        for i, v in enumerate(df_grouped.shape):
            axs[1].bar_label(axs[1].containers[i], label=str(v))

        axs[1].set_title('Purchases Data by Prediction Label',pad=15,fontdict={'fontsize':20})
        axs[1].set_xticks(x)
        axs[1].set_xticklabels(labels, rotation=45)
        axs[1].legend(fontsize=12)

        
    else:
        fig, axs = plt.subplots(1, 2, figsize=(15, 8))
        test = calc_porcentage(ypred_dataframe, cols, 'prediction_label')
        fig = plot_porcentage(test)
    
    fig.subplots_adjust(wspace=0.5, hspace=0.2)
    fig.suptitle('')
    plt.show()
    st.pyplot(fig, transparent=True)
