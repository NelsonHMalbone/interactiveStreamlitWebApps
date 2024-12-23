# making a live converter for currency

# from tutorial import config
import streamlit as st


st.title('Live Currency Converter')
conversion = st.radio("Choose the conversion: ", ('USD to EUR', 'EUR to USD'))

# instead of having two separate inputs we will have one
user_input_value = st.number_input("Enter the amount:")
if conversion == 'USD to EUR':
    # intending to get euros from usd
    # calculating the conversion
    # result of conversion
    euros = usd_to_euros()

else:
    # intending to get usd from euros
    dollars = eur_to_usd()