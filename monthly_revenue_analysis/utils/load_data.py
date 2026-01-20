from __future__ import annotations

from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"
DATA_RAW = PROJECT_ROOT / "data" / "raw"


def load_monthly_revenue() -> pd.DataFrame:
    fp = DATA_PROCESSED / "monthly_revenue.csv"
    df = pd.read_csv(fp)

    df.columns = ["year_month", "total_revenue", "num_orders"]
    df["year"] = df["year_month"] // 100
    df["month"] = df["year_month"] % 100
    df["date"] = pd.to_datetime(df["year"].astype(str) + "-" + df["month"].astype(str))
    df["aov"] = df["total_revenue"] / df["num_orders"]

    df = df.sort_values("date").reset_index(drop=True)
    return df


def load_online_retail() -> pd.DataFrame:
    fp = DATA_RAW / "online_retail_II.csv"
    return pd.read_csv(fp)
