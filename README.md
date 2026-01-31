 Slooze – Databricks Data Engineering Take-Home

 Overview

This project implements an end-to-end data engineering pipeline using Databricks and Delta Lake.
The solution follows a Lakehouse architecture with Bronze, Silver and Gold layers.

All tables are created inside:

workspace.slooze_db

 Architecture

Marketplace feed (simulated)
→ Bronze Delta table
→ Silver Delta table
→ Gold KPI tables
→ EDA and insights

 Technology Stack

- Databricks
- PySpark
- Delta Lake

 Table Layout

Bronze
- indiamart_bronze_products

Silver
- indiamart_silver_products

Gold
- indiamart_gold_products_per_category
- indiamart_gold_avg_price_per_category

 How to run

1. Open all notebooks in Databricks
2. Run in this order

- ingestion_bronze.py
- etl_cleaning.py
- gold_aggregations.py
- eda_analysis.py

All tables will be created automatically inside workspace.slooze_db.

 Why ingestion is simulated

Live scraping of B2B marketplaces is unreliable because of:

- dynamic rendering
- frequent HTML changes
- anti-bot protection

In real production systems, marketplace data is commonly ingested through APIs or scheduled data feeds.
This project models that real-world ingestion pattern and focuses on ETL quality, schema control and analytics.

 Key insights

- Industrial machinery has significantly higher price range compared to electronic goods
- Electronic goods dominate listing volume
- Supplier locations are concentrated in major industrial regions

 Limitations

- Data source is simulated
- No real-time ingestion
- Small sample size

 Future improvements

- API based ingestion
- incremental merge instead of full overwrite
- automated data quality checks
- BI dashboards using Power BI or Tableau
