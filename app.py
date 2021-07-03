import streamlit as st
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.cryptocurrencies import CryptoCurrencies

st.write('Alpha Vantage data')

apk = 'BA0BRPDZ1UOJKL47' 

st.write('Cryptocurrency prices at closing ')
cc = CryptoCurrencies(key='apk', output_format='pandas')
data, meta_data = cc.get_digital_currency_daily(symbol='BTC', market='CNY')
st.line_chart(data['4b. close (USD)'])


if st.checkbox('Show raw data for cryptocurrency'):
    st.subheader('Raw data')
    st.write(data)


symbol=st.text_input('Ticker?')
st.write('Confirm ticker', symbol)
st.write('[One can try with different ticker and reload the page]')


if len(symbol) !=0:
    ts2 = TimeSeries(key='apk',output_format='pandas', indexing_type='date')
    st.write('Intraday Times Series -5min- closing price for the stock ticker',symbol)
    data2, meta_data = ts2.get_intraday(symbol=symbol,interval='5min', outputsize='full')
    st.line_chart(data2['4. close'])

if st.checkbox('Show raw data for stock prices'):
    st.subheader('Raw data')
    st.write(data2)
   
