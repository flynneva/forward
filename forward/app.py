import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf


def get_ticker(symbol):
    return yf.Ticker(str(symbol))


def setup_app():
    st.title('forward')


def main():
    setup_app()

    input_ticker = st.text_input("Ticker", 'MSFT')
    time_period = st.selectbox(
        'Time Period',
        ('1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'))
    ticker = get_ticker(input_ticker)
    history = ticker.history(period=time_period)
    st.line_chart(history[['Open', 'Close']])
    
    ticker = get_ticker('MSFT')


if __name__ == "__main__":
    main()
