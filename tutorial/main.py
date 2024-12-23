# making a live converter for currency

# from tutorial import config
import streamlit as st

def convert(currency, currency_value):
# currency_value: dollar amount
# currency: eur,usd, etc
    return 10

st.title('Live Currency Converter')
conversion = st.radio("Choose the conversion: ", ('USD to EUR', 'EUR to USD'))

# instead of having two separate inputs we will have one
user_input_value = st.number_input("Enter the amount:")

btn_value = st.button('Convert')

if conversion == 'USD to EUR':
    # intending to get euros from usd
    # calculating the conversion
    # result of conversion
    # extracting the USD and that will be sent to the convery funct
    # the pass the value
    euros = convert(conversion[:3], user_input_value)
    if btn_value

else:
    # intending to get usd from euros
    dollars = convert(conversion[:3])