from datetime import date
from dateutil.relativedelta import relativedelta
from datetime import datetime
from nsepy import get_history
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import requests
from bs4 import BeautifulSoup



today_date = datetime.today()

symbol_list = pd.read_csv('EQUITY_L.csv')
d = dict(zip (symbol_list['SYMBOL'], symbol_list['NAME OF COMPANY']))

st.title("NSE STOCK CHARTS")
name="SBIN"
#name= (st.text_input('Enter Stock Symbol')).upper()
name = st.selectbox(
     'Symbol',
     d.keys())
col1,col2, col3,col4,col5,col6 = st.columns(6) 

url = 'https://www.google.com/finance/quote/'+name+':NSE'

page = requests.get(url).text
soup = BeautifulSoup(page)
soup.prettify()
t= str(soup.find_all(class_="bLLb2d"))
k=t
if ('bLLb2d' in k):
	i = t.index('>') + 1
	t = t[i:]
	i = t.index('<')
	t=t[:i]


dur ='Last Month'
dur = st.selectbox(
     'Duration',
     ('Last Month', 'Last Year', 'Last 6 Months', 'Last week'))

if (dur == 'Last Month') :
	prev_date = today_date - relativedelta(months=1)
if (dur == 'Last Year') :
	prev_date = today_date - relativedelta(years=1)
if (dur == 'Last 6 Months') :
	prev_date = today_date - relativedelta(months=6)
if (dur == 'Last week'):
	prev_date = today_date - relativedelta(days=7)


today_date = datetime.today().date()
prev_date = prev_date.date()
if (col1.button("VWAP")):
	st.title(d[name])
	stock = get_history(symbol=name,
	                   start=prev_date,
	                   end=today_date)
	
	st.write("""
	# VOLUME WEIGHTED AVERAGE PRICE
	""")

	st.line_chart(stock['VWAP'])

if (col2.button("VOLUME")):
	st.title(name)
	stock = get_history(symbol=name,
		                   start=prev_date,
		                   end=today_date)
	st.write("""
	# VOLUME
	""")
	st.line_chart(stock['Volume'])

if (col3.button("OPEN")):
	st.title(name)
	stock = get_history(symbol=name,
		                   start=prev_date,
		                   end=today_date)
	st.write("""
	# OPEN
	""")
	st.line_chart(stock['Open'])

if (col4.button("CLOSE")):
	st.title(name)
	stock = get_history(symbol=name,
		                   start=prev_date,
		                   end=today_date)
	st.write("""
	# CLOSE
	""")
	st.line_chart(stock['Close'])

if (col5.button("HIGH")):
	st.title(name)
	stock = get_history(symbol=name,
		                   start=prev_date,
		                   end=today_date)
	st.write("""
	# HIGH
	""")
	st.line_chart(stock['High'])

if (col6.button("LOW")):
	st.title(name)
	stock = get_history(symbol=name,
		                   start=prev_date,
		                   end=today_date)
	st.write("""
	# LOW
	""")
	st.line_chart(stock['Low'])

if ('bLLb2d' in k):
	st.write("""
	# ABOUT
	""")
	st.write(t)




