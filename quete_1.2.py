import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 



st.title ("Manipulation de données et création de graphiques pour chaque dataset")


choix = st.selectbox(
    "Quel dataset veux tu utiliser ? ", sns.get_dataset_names()) #sns.get regroupe tous les dataframes listé dans le lien github

df= sns.load_dataset(choix) #on definie le dataframe choisis à partir de la variable choix 


st.dataframe(df) #on affiche le dataframe

st.text("Choisissez la Colonne X ") #titre pour la selectbox des colonnes
X= st.selectbox("X", df.columns)#affichage de la selectbox 

st.text("Choisissez la Colonne Y ")
Y= st.selectbox("Y", df.columns)

liste_graph=["scatter_chart","bar_chart","line_char"]

choix_graph= st.selectbox("Quel graphique veux tu utiliser ?", liste_graph)

if choix_graph ==  "bar_chart" :
    st.bar_chart(data=df,x=X,y=Y) #affichage graphiques

elif choix_graph ==  "line_char" : 
    st.line_chart(data=df,x=X,y=Y) #affichage graphiques

elif choix_graph == "scatter_chart":
    st.scatter_chart(data=df,x=X,y=Y) #affichage graphiques



agree = st.checkbox("Afficher la matrice de corrélation")

if agree:
    correlation= df.select_dtypes("number").corr()
    sns.heatmap(correlation, annot= True, cmap="coolwarm")
    st.pyplot(plt)


st.page_link("https://github.com/mohamedachem-droid/quete1.2-streamlit", label="Code Source", icon=":material/code_blocks:")