## Slooze Data Engineering

### Tech Stack
- Databricks
- Python
- PySpark
- Delta Lake

### Pipeline
Bronze: Raw scraped JSON  
Silver: Cleaned Delta table  
EDA: Databricks notebooks  

### How to Run
1. Import notebooks into Databricks
2. Attach cluster
3. Run notebooks in order

### Insights
- Supplier concentration in manufacturing hubs
- Large price variability in machinery
- Missing price data common in B2B marketplaces

### Improvements
- Async scraping
- Gold layer aggregation
- Databricks Jobs scheduling
