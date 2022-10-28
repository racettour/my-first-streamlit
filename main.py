import streamlit as st
import pandas as pd
import seaborn as sns

st.title('analyse de correlation et de distribution')

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"

df_weather = pd.read_csv(link)

col1, col2, col3 = st.columns(3)

continent_list = []
with col1:
    bt_us = st.checkbox('US.', value= True)
with col2:
    bt_jap = st.checkbox('Jap.', value=True)
with col3:
    bt_eur = st.checkbox('Eur.', value=True)

if bt_us:
    continent_list.append(' US.')

if bt_eur:
    continent_list.append(' Europe.')


if bt_jap:
    continent_list.append(' Japan.')

tab1, tab2, tab3 = st.tabs(["Data Frame", "Correlation", "Distribution"])

with tab1:
    df_corr = df_weather.loc[df_weather['continent'].isin(continent_list)]

    st.write(df_corr)

with tab2:
    viz_correlation = sns.heatmap(df_corr.corr(), center=0,
                                  cmap=sns.color_palette("vlag", as_cmap=True),
                                  vmin=-1,
                                  vmax=1
                                  )

    st.pyplot(viz_correlation.figure)

with tab3:
    col1, col2 = st.columns([1,3])
    with col1:
        genre = st.radio(
            "category",
            df_weather.columns.values)

    with col2:
        viz_distri= sns.displot(df_corr, x=genre, hue="continent", element="step")
        st.pyplot(viz_distri.figure)