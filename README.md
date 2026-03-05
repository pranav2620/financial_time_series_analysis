# financial_time_series_analysis
# High-Frequency Market Microstructure Analysis

This project builds an end-to-end pipeline for analyzing high-frequency cryptocurrency market data and modeling short-term volatility using market microstructure features.

## Overview
High-frequency trading data contains detailed information about market microstructure such as bid-ask spreads, order flow, and price dynamics.  
This project processes raw market data, constructs microstructure features, and analyzes volatility patterns.

## Features Implemented

- Data ingestion and preprocessing pipeline
- Timestamp validation and data quality checks
- Feature engineering:
  - Log returns
  - Bid-ask spread
  - Rolling volatility
- Exploratory time-series analysis
- Volatility prediction using regression models

## Tech Stack

- Python
- Pandas
- NumPy
- SciPy
- Matplotlib
- Scikit-learn

## Project Structure

```
financial_time_series_analysis/
│
├── notebooks/        # Exploratory analysis and modeling
├── src/              # Core data processing scripts
├── data/             # Raw and processed datasets
├── reports/          # Plots and analysis outputs
├── requirements.txt
└── README.md
```

## Example Analysis

The project investigates relationships between:

- Bid-ask spread
- Rolling volatility
- Future volatility

These features are commonly studied in **market microstructure and quantitative finance research**.

## Spread vs Rolling Volatility

## Spread vs Rolling Volatility

Relationship between rolling volatility and bid–ask spread in high-frequency BTC market data.

Higher volatility periods tend to coincide with wider spreads, reflecting reduced liquidity and increased market uncertainty.

![Spread vs Volatility](reports/figures/spread_vs_volatility.png)

## Author
Pranav Jindal
