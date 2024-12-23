# making a live converter for currency

# from tutorial import config
import streamlit as st


st.title('Live Currency Converter')
conversion = st.radio("Choose the conversion: ", ('USD to EUR', 'EUR to USD'))

if conversion == 'USD to EUR':
    # intending to get euros from usd
    user_input_usd = st.number_input("Enter the amount in USD:")
    # calculating the conversion
    # result of conversion
    euros = usd_to_euros()

else:
    # intending to get usd from euros
    user_input_eur = st.number_input("Enter the amount in EUR:")
    dollars = usd_to_euros()