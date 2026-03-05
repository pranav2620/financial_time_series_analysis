"""
load_data.py

Purpose:
--------
Load raw high-frequency financial time-series data, perform basic validation,
standardize timestamps, and store a clean version for downstream analysis.

This script is intentionally simple and robust.
"""

from pathlib import Path
import pandas as pd


# -----------------------------
# Project Paths
# -----------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"


# -----------------------------
# Configuration
# -----------------------------
RAW_FILE_NAME = "BTC_1min.csv"
      # <-- change later if needed
PROCESSED_FILE_NAME = "clean_data.csv"
TIMESTAMP_COLUMN = "system_time"      # <-- adjust to dataset
EXPECTED_COLUMNS = None             # set list later if schema is known

DROP_COLUMNS = ["Unnamed: 0"]


# -----------------------------
# Functions
# -----------------------------
def load_raw_data(filepath: Path) -> pd.DataFrame:
    """
    Load raw CSV data into a pandas DataFrame.
    """
    if not filepath.exists():
        raise FileNotFoundError(f"Raw data file not found: {filepath}")

    df = pd.read_csv(filepath)
    return df


def basic_validation(df: pd.DataFrame) -> None:
    """
    Perform minimal sanity checks on the dataset.
    """
    if df.empty:
        raise ValueError("Loaded DataFrame is empty.")

    if TIMESTAMP_COLUMN not in df.columns:
        raise ValueError(f"Timestamp column '{TIMESTAMP_COLUMN}' not found.")

    if EXPECTED_COLUMNS is not None:
        missing = set(EXPECTED_COLUMNS) - set(df.columns)
        if missing:
            raise ValueError(f"Missing expected columns: {missing}")


def preprocess_timestamps(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert timestamp column to pandas datetime and sort.
    """
    df[TIMESTAMP_COLUMN] = pd.to_datetime(
        df[TIMESTAMP_COLUMN], errors="coerce"
    )

    df = df.dropna(subset=[TIMESTAMP_COLUMN])
    df = df.sort_values(by=TIMESTAMP_COLUMN)
    df = df.reset_index(drop=True)

    return df


def save_processed_data(df: pd.DataFrame, output_path: Path) -> None:
    """
    Save processed DataFrame to disk.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


# -----------------------------
# Main Execution
# -----------------------------
def main():
    raw_path = RAW_DATA_DIR / RAW_FILE_NAME
    processed_path = PROCESSED_DATA_DIR / PROCESSED_FILE_NAME

    print("Loading raw data...")
    df = load_raw_data(raw_path)

    print("Running basic validation...")
    basic_validation(df)

    print("Processing timestamps...")
    df = preprocess_timestamps(df)

    print(f"Saving processed data to: {processed_path}")
    save_processed_data(df, processed_path)

    print("Data ingestion completed successfully.")


if __name__ == "__main__":
    main()
