import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

st.title("Hello world")
with st.sidebar:
    st.header("Informazioni")
    st.write("questa è la mia prima app")
st.header("This is a header with a divider", divider="orange")
st.markdown("Questo testo è creato con markdown")
st.subheader("st.column")
col1, col2 = st.columns(2)
with col1:
    eta = st.slider("quanti anni hai?",0,100)

with col2:
    st.write(":red[Hai detto di avere] ",eta," anni")

st.subheader("st.area_chart")
df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

st.area_chart(df)
    
