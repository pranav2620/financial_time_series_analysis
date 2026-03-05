"""
validate_data.py

Purpose:
--------
Run explicit validation checks on processed financial time-series data.
This script does NOT aggressively clean data.
It detects, quantifies, and reports potential issues.

This separation keeps ingestion, validation, and analysis clean and defensible.
"""

from pathlib import Path
import pandas as pd
import numpy as np


# -----------------------------
# Paths
# -----------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed" / "clean_data.csv"


# -----------------------------
# Configuration
# -----------------------------
TIMESTAMP_COLUMN = "system_time"
PRICE_COLUMN = "midpoint"
SPREAD_COLUMN = "spread"


# -----------------------------
# Validation Functions
# -----------------------------
def validate_structure(df: pd.DataFrame):
    print("\n[STRUCTURE CHECKS]")
    required_cols = [TIMESTAMP_COLUMN, PRICE_COLUMN, SPREAD_COLUMN]
    missing = set(required_cols) - set(df.columns)

    if missing:
        print(f"❌ Missing required columns: {missing}")
    else:
        print("✅ Required columns present")


def validate_timestamps(df: pd.DataFrame):
    print("\n[TIMESTAMP CHECKS]")

    missing_ts = df[TIMESTAMP_COLUMN].isna().sum()
    print(f"Missing timestamps: {missing_ts}")

    is_sorted = df[TIMESTAMP_COLUMN].is_monotonic_increasing
    print(f"Chronologically sorted: {is_sorted}")

    duplicates = df[TIMESTAMP_COLUMN].duplicated().sum()
    print(f"Duplicate timestamps: {duplicates}")


def validate_numerical_values(df: pd.DataFrame):
    print("\n[NUMERICAL SANITY CHECKS]")

    negative_prices = (df[PRICE_COLUMN] <= 0).sum()
    print(f"Non-positive prices: {negative_prices}")

    negative_spreads = (df[SPREAD_COLUMN] < 0).sum()
    print(f"Negative spreads: {negative_spreads}")

    missing_prices = df[PRICE_COLUMN].isna().sum()
    print(f"Missing prices: {missing_prices}")


def validate_returns(df: pd.DataFrame):
    print("\n[RETURN DISTRIBUTION CHECKS]")

    log_returns = np.log(df[PRICE_COLUMN]).diff()

    extreme_moves = log_returns.abs() > log_returns.abs().quantile(0.999)
    print(f"Extreme return observations (>99.9%): {extreme_moves.sum()}")

    print("Return summary:")
    print(log_returns.describe())


# -----------------------------
# Main Execution
# -----------------------------
def main():
    print("Loading processed data...")
    df = pd.read_csv(PROCESSED_DATA_PATH, parse_dates=[TIMESTAMP_COLUMN])

    validate_structure(df)
    validate_timestamps(df)
    validate_numerical_values(df)
    validate_returns(df)

    print("\nValidation completed.")


if __name__ == "__main__":
    main()
