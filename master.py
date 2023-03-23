
# This is the master script for loading in data and generating the PDF

# Importing necessary libraries

from statsmodels.distributions.empirical_distribution import ECDF
import pandas as pd 
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

# Input ticker and download data on weekly interval

stock = input("Ticker: ")
df = yf.download(stock, interval="1wk")

# Interval pct. change
returns = df["Returns"] = df["Adj Close"].pct_change()*100

# Plotting and saving hist

def plot_hist():
    plt.hist(df["Returns"], bins=100, color='black', density=True, alpha=1)
    plt.ylabel("Density")
    plt.xlabel(f"{stock} Weekly Returns pct.")
    plt.title(f"{stock} Returns Distribution")
    plt.savefig(f'{stock}-hist.png')

# Plotting and saving ECDF 

def plot_ECDF():
    plt.hist(df["Returns"], bins=100, color='black', density=True, alpha=1, cumulative=True)
    plt.ylabel("Density")
    plt.xlabel(f"{stock} Weekly Returns pct.")
    plt.title(f"{stock} Empirical CDF")
    plt.savefig(f'{stock}-ECDF.png')

def plot_change(): 
    plt.plot(df.index, df["Returns"], color="black")
    plt.ylabel("Weekly % Change")
    plt.savefig(f'{stock}-change.png')

# Calculating data for ECDF 

sample = df["Returns"]

# Fitting ECDF on data
ecdf = ECDF(sample)

ecdf_data = pd.DataFrame( 
    {"Weekly % Change" : ["P(R<0.01)", "P(R<0.02)", "P(R<0.03)", "P(R<0.04)", "P(R<0.05)", "P(R<0.06)", "P(R<0.07)", "P(R<0.08)", "P(R<0.09)", "P(R<0.10)"], 
     "Probability" : [ecdf(1), ecdf(2), ecdf(3), ecdf(4), ecdf(5), ecdf(6), ecdf(7), ecdf(8), ecdf(9), ecdf(10)]
    })

ecdf_data = ecdf_data.reset_index(drop=True)

# Getting options data

# stockdata = yf.Ticker(stock)
# opt = stockdata.option_chain("2023-03-31")
# calls = pd.DataFrame(opt.calls)



