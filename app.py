import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


def main():
    st.title("Nel mezzo del cammin di nostra vita mi ritrovai per una selva oscura...")
    st.write('Ciao a tutti io sono leonardo, questa è la mia prima webapp,\n sii paziente.')
    df = pd.DataFrame(np.random.randint(0,100,size=(100,4)), columns=list('ABCD'))
    st.dataframe(df)
    myimg = Image.open('fotocv.jpeg')
    #myimg = myimg.resize((120,120))
    width = st.sidebar.slider("Photo size", 120,1200,100)
    st.image(myimg, width=width)#, use_column_width=True)
    st.table(df.head())
    lista = ['Email', 'Telefono', 'Cellulare']
    select_box = st.sidebar.selectbox('Come desideri essere contattato:', lista)
    slider = st.sidebar.slider('Petal_lenght',0.0,10.0,0.1)  #.sidebar

def main2():
    st.button("re-run")
    st.markdown("markdown")
def main3():

    left_column, right_column = st.beta_columns(2)
    # You can use a column just like st.sidebar:
    left_column.button('Press me!')

    # Or even better, call Streamlit functions inside a "with" block:
    with right_column:
        chosen = st.radio(
            'Sorting hat',
            ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
        st.write(f"You are in {chosen} house!")



if __name__=='__main__':
    main3()