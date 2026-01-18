Outputs:
- summary.json: mean / P05 / P95 / probability below threshold
- simulations.csv: sim_orders, sim_aov, sim_revenue
- fig_1_revenue_distribution.png
- fig_2_cdf.png
- fig_3_orders_distribution.png
- fig_4_aov_distribution.png
Assumptions:
- Orders ~ Normal(mu, sigma), clipped at 0
- AOV ~ Gamma(shape, scale)
Revenue = Orders * AOV
