import streamlit as st
from pymongo import MongoClient

client = MongoClient('mongodb://mongo:27017/')
db = client['trading_db']
trades = db['trades']

st.title("FNO Trading Dashboard")

all_trades = list(trades.find())
st.write("Total Trades:", len(all_trades))

for trade in all_trades[-10:]:
    st.json(trade)
