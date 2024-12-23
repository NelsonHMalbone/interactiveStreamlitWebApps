# making a live converter for currency

# from tutorial import config
import streamlit as st


st.title('Live Currency Converter')
conversion = st.radio("Choose the conversion: ", ('USD to EUR', 'EUR to USD'))
if conversion == 'USD to EUR':
    pass
elif conversion == 'EUR to USD':
    pass