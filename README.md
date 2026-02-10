# 📊 Finance Data Pipeline → Power BI Analytics Dashboard

## Overview

This project builds an automated financial data pipeline that:

- Ingests daily market data using Yahoo Finance (yfinance)
- Cleans and normalizes time-series data into tidy (long) format
- Engineers financial risk and performance features
- Aggregates per-asset summary statistics
- Outputs structured datasets for Power BI dashboards

This is not a trading bot.  
It is a structured data engineering + analytics pipeline designed to demonstrate:

- Data ingestion workflows  
- Time-series feature engineering  
- Rolling window analytics  
- Financial risk metrics  
- Clean dataset architecture  
- BI integration  

---

## 🏗 Architecture

Yahoo Finance (yfinance)  
↓  
Python Pipeline  
- fetch_prices()  
- add_features()  
- make_summary()  
- write_sqlite()  
↓  
SQLite + CSV Outputs  
↓  
Power BI Dashboard  

---

## 📂 Project Structure

finance-pipeline-powerbi-project/
│
├── data/
│   ├── finance.db
│   └── processed/
│       ├── prices_clean.csv
│       ├── features_daily.csv
│       └── summary_by_ticker.csv
│
├── src/
│   ├── config.py
│   └── pipeline.py
│
├── requirements.txt
└── README.md

---

## ⚙️ Setup & Installation (Mac)

### 1. Create Virtual Environment

python3 -m venv .venv  
source .venv/bin/activate  

### 2. Install Dependencies

pip install -r requirements.txt  

### 3. Run the Pipeline

python src/pipeline.py  

After running, the following files are generated:

- data/processed/prices_clean.csv  
- data/processed/features_daily.csv  
- data/processed/summary_by_ticker.csv  
- data/finance.db  

---

## 🔍 Core Pipeline Functions

### fetch_prices()

Downloads daily OHLCV data from Yahoo Finance and normalizes it into tidy format.

Each row represents:
(date, ticker)

This structure simplifies group-based calculations and BI modeling.

---

### add_features()

Creates:

- Daily return (ret)
- Log return (log_ret)
- Rolling volatility (vol)
- Simple moving averages (sma_21, sma_63, sma_126, sma_252)
- Cumulative return
- Drawdown
- Maximum drawdown

Rolling windows are calculated per ticker using groupby transformations.

---

### make_summary()

Aggregates per-ticker metrics:

- Annualized return
- Annualized volatility
- Sharpe-like ratio
- Worst drawdown

Annualization logic assumes 252 trading days per year.

---

### write_sqlite()

Writes structured tables:

- prices_clean
- features_daily
- summary_by_ticker

Tables are overwritten each run to ensure deterministic refresh behavior.

---

## 📈 Power BI Integration

Load into Power BI:

- prices_clean.csv
- features_daily.csv
- summary_by_ticker.csv

Create relationships on:
- ticker
- date

Suggested dashboard pages:
- Overview (KPIs)
- Performance (price + SMA overlays)
- Risk (volatility + drawdown)
- Asset comparison (risk vs return scatter)

---

## 🎯 Purpose

This project demonstrates:

- Financial time-series data engineering
- Rolling-window feature computation
- Risk-adjusted performance analytics
- Structured dataset design
- BI integration workflow
