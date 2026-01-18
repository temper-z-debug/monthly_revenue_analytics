Outputs:
- metrics.csv: R2/RMSE/MAE comparison
- predictions_test.csv: actual vs predicted on test split
- fig_A_actual_vs_pred.png
- fig_B_residuals.png
- fig_C_rf_feature_importance.png
Split: train/test = 75/25, shuffle=False
Features: num_orders, revenue_lag1, month_sin, month_cos
