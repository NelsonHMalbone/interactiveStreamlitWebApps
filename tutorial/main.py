# making a live converter for currency
import requests
import config
import streamlit as st

url = f'https://v6.exchangerate-api.com/v6/{config.api_key}/latest/USD'
def convert(currency, currency_value):
# currency_value: dollar amount
# currency: eur,usd, etc

    response = requests.get(url)
    data = response.json()
    conversion_rate = data['conversion_rates']['EUR']
    result = currency_value * conversion_rate
    return result

st.title('Live Currency Converter')
conversion = st.radio("Choose the conversion: ", ('USD to EUR', 'EUR to USD'))

# instead of having two separate inputs we will have one
user_input_value = st.number_input("Enter the amount:")

btn_value = st.button('Convert')

if conversion == 'USD to EUR':
    # intending to get euros from usd
    # calculating the conversion
    # result of conversion
    if btn_value:
        # extracting the USD and that will be sent to the convery funct
        # the pass the value
        euros = convert(conversion[:3], user_input_value)
        st.success(f"The Results is {euros:.2f}")
else:
    # intending to get usd from euros
    if btn_value:
        dollars = convert(conversion[:3], user_input_value)
        st.success(f'The Results is {dollars:.2f}')