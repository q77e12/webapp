import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


def main2():
    st.title("Nel mezzo del cammin..")
    df = pd.DataFrame(np.random.randint(0,100,size=(100,4)), columns=list('ABCD'))
    st.dataframe(df)
    myimg = Image.open('avvo.jpg')
    st.image(myimg, use_column_width=True)
    st.write('ciao a tutti i miei studenti')
    st.table(df.head())
    lista = ['Email', 'Telefono', 'Cellulare']
    select_box = st.sidebar.selectbox('Come desideri essere contattato:', lista)
    st.sidebar.write(select_box)
    slider = st.sidebar.slider('Petal_lenght',0.0,10.0,0.1)

def main():
    st.button("re-run")
    st.markdown("markdown")
    



if __name__=='__main__':
    main()