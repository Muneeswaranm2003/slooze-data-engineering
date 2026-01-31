
# EDA

spark.sql("USE CATALOG workspace")
spark.sql("USE SCHEMA slooze_db")

spark.table("indiamart_silver_products").display()
spark.table("indiamart_gold_products_per_category").display()
spark.table("indiamart_gold_avg_price_per_category").display()
