from flask import Flask, render_template, request
import pandas_datareader as pdr
import pandas as pd
from datetime import date, datetime, timedelta
import yfinance as yf
import requests
import plotly.graph_objects as go
import numpy as np


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    var = ""
    quarterly_chart_html = ""
    annual_chart_html = ""
    nonlinearmodel = ""
    linearmodel = ""
    price_text_11 = ""
    price_text_12 = ""
    price_text_13 = ""
    price_text_14 = ""
    price_text_15 = ""
    price_text_21 = ""
    price_text_22 = ""
    price_text_23 = ""
    price_text_24 = ""
    price_text_25 = ""
    price_text_26 = ""
    p = ""
    nonlinear_chart_html = ""
    linear_chart_html = ""
    processed_text = None  # Renamed for clarity
    if request.method == "POST":
        # Get the ticker symbol from the form
        text_input = request.form.get("ticker")

        # Process the text (for example, convert it to uppercase)
        ticker = text_input.upper()
        print("")  # Debugging: Print the processed text to the console
        print(ticker)

        API_KEY = "11"

        url = f"https://www.alphavantage.co/query?function=CASH_FLOW&symbol={ticker}&apikey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        p = data
    return render_template("index.html", processed_text=var, quarterly_chart_html=quarterly_chart_html, annual_chart_html=annual_chart_html, nonlinear_chart_html=nonlinearmodel, linear_chart_html=linearmodel, price_text_11=price_text_11, price_text_12=price_text_12, price_text_13=price_text_13, price_text_14=price_text_14, price_text_15=price_text_15, price_text_21=price_text_21, price_text_22=price_text_22, price_text_23=price_text_23, price_text_24=price_text_24, price_text_25=price_text_25, price_text_26=price_text_26, p=p)