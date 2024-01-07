import streamlit as st
import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 

st.title("Project Data Scientis")
st.header("Tentang Satu Relawan")

st.text("data frame:")
data = pd.read_excel("KumpulanData-ProjectDataScience.xlsx")
df = pd.DataFrame(data)
st.write(df)

st.text("melakukan pengecekan missing Value : ")
st.write(df.isnull().sum())

st.text("melakukan pengecekan duplikasi data : ")
if df.duplicated().sum() == 0 :
    st.info("tidak ada data duplikasi!")
else :
    st.write(df.isnull().sum())

st.text("mengecek info type data : ")
st.write(df.dtypes)

st.text("menampilkan banyak baris dan kolom")
st.write(df.shape)

st.text("menampilkan Deskripsi data : ")
st.warning(df.describe())

def show_distribution_plots(data):
    numerical_features = data.select_dtypes(include=[np.number])
    for column in numerical_features.columns:
        plt.figure(figsize=(6, 4))
        sns.histplot(data[column], kde=True, bins=20, color='skyblue')
        plt.title(f'Distribusi {column}')
        plt.xlabel(column)
        plt.ylabel('Frekuensi')
        fig = plt.gcf()
        st.pyplot(fig)  

file_path = 'KumpulanData-ProjectDataScience.xlsx' 
data = pd.read_excel(file_path)

# Tampilkan plot menggunakan Streamlit
st.subheader('Diagram Distribusi Data Numerik : ')
show_distribution_plots(data)

def show_scatter_plot(data):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x='Umur', y='Keahlian')
    plt.title('Perbandingan Umur dan Keahlian')
    plt.xlabel('Umur')
    plt.ylabel('Keahlian')
    st.pyplot(plt)

st.subheader('Visualisasi Perbandingan Umur dan Keahlian ')
show_scatter_plot(data)

teks_panjang = """
ini merupakan visualisasi perbandingan antara umur dan keahlian,disini
terlihat bahwa rentang umur 22 - 34 keahlian yang banyak diminati adalah menejemen acara dan 
pengembangan sumber daya
"""

st.markdown(teks_panjang)

def show_scatter_plot(data):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=data, x='Umur', y='Jenis Organisasi')
    plt.title('Perbandingan Umur dan Keahlian')
    plt.xlabel('Umur')
    plt.ylabel('Jenis Organisasi')
    st.pyplot(plt)

st.subheader('Visualisasi Perbandingan Umur dan Jenis Organisasi ')
show_scatter_plot(data)

teks_panjang = """
ini merupakan visualisasi perbandingan antara umur dan jenis organisasi,disini
terlihat bahwa rentang umur 22-34 jenis organisasi yang diminati adalah lembaga amal dan
organisasi pengembang masyarakat
"""

st.markdown(teks_panjang)


