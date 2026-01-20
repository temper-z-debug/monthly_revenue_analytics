import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from utils.load_data import load_monthly_revenue
from utils.artifact_utils import ARTIFACT_DIR, maybe_savefig, maybe_to_csv


def evaluate(model_name, y_true, y_pred):
    return {
        "Model": model_name,
        "R2": float(r2_score(y_true, y_pred)),
        "RMSE": float(mean_squared_error(y_true, y_pred) ** 0.5),
        "MAE": float(mean_absolute_error(y_true, y_pred)),
    }

def ensure_month_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "total_revenue" not in df.columns:
        if "revenue" in df.columns:
            df["total_revenue"] = df["revenue"]
        else:
            raise ValueError("Missing required column: total_revenue (or revenue).")

    if "num_orders" not in df.columns:
        if "orders" in df.columns:
            df["num_orders"] = df["orders"]
        else:
            raise ValueError("Missing required column: num_orders (or orders).")

    if "year_month" not in df.columns:
        df["year_month"] = np.arange(len(df)).astype(str)

    if "month" not in df.columns:
        ym = df["year_month"].astype(str)
        if ym.str.contains("-").any():
            df["month"] = ym.str.split("-").str[-1].astype(int)
        else:
            df["month"] = ym.str[-2:].astype(int)

    return df


def main():
    df = load_monthly_revenue()
    df = ensure_month_features(df)

    df["revenue_lag1"] = df["total_revenue"].shift(1)
    df = df.dropna().reset_index(drop=True)

    df["month_sin"] = np.sin(2 * np.pi * df["month"] / 12)
    df["month_cos"] = np.cos(2 * np.pi * df["month"] / 12)

    X = df[["num_orders", "revenue_lag1", "month_sin", "month_cos"]]
    y = df["total_revenue"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, shuffle=False
    )

    lr = LinearRegression()
    lr.fit(X_train, y_train)
    lr_pred = lr.predict(X_test)

    rf = RandomForestRegressor(n_estimators=300, random_state=42)
    rf.fit(X_train, y_train)
    rf_pred = rf.predict(X_test)

    results = [
        evaluate("Linear Regression", y_test, lr_pred),
        evaluate("Random Forest", y_test, rf_pred),
    ]
    metrics_df = pd.DataFrame(results).sort_values("RMSE").reset_index(drop=True)

    print("\n=== Model Comparison Results ===\n")
    print(metrics_df)

    pred_df = pd.DataFrame({
        "year_month": df.loc[X_test.index, "year_month"].astype(str).values,
        "actual_revenue": y_test.values,
        "pred_lr": lr_pred,
        "pred_rf": rf_pred,
    })

    x_axis = pred_df["year_month"].values

    fig, axes = plt.subplots(1, 3, figsize=(16, 4))

    axes[0].plot(x_axis, pred_df["actual_revenue"].values, label="Actual")
    axes[0].plot(x_axis, pred_df["pred_lr"].values, label="LR")
    axes[0].plot(x_axis, pred_df["pred_rf"].values, label="RF")
    axes[0].set_title("Actual vs Predicted")
    axes[0].set_xlabel("year_month")
    axes[0].set_ylabel("Revenue")
    axes[0].tick_params(axis="x", rotation=45)
    axes[0].legend()

    lr_resid = pred_df["actual_revenue"].values - pred_df["pred_lr"].values
    rf_resid = pred_df["actual_revenue"].values - pred_df["pred_rf"].values
    axes[1].plot(x_axis, lr_resid, label="LR Residual")
    axes[1].plot(x_axis, rf_resid, label="RF Residual")
    axes[1].axhline(0, linewidth=1)
    axes[1].set_title("Residuals (Actual - Pred)")
    axes[1].set_xlabel("year_month")
    axes[1].set_ylabel("Residual")
    axes[1].tick_params(axis="x", rotation=45)
    axes[1].legend()

    axes[2].bar(X.columns, rf.feature_importances_)
    axes[2].set_title("RF Feature Importance")
    axes[2].set_xlabel("Feature")
    axes[2].set_ylabel("Importance")
    axes[2].tick_params(axis="x", rotation=20)

    fig.suptitle("Model Comparison: Linear Regression vs Random Forest (Test Set)", y=1.05, fontsize=14)
    fig.tight_layout()

    plt.show()

    maybe_savefig(fig, ARTIFACT_DIR / "10_model_compare_composite.png")
    maybe_to_csv(metrics_df, ARTIFACT_DIR / "10_metrics.csv", index=False)
    maybe_to_csv(pred_df, ARTIFACT_DIR / "10_predictions_test.csv", index=False)


if __name__ == "__main__":
    main()
