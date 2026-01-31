
# Gold layer – KPIs

spark.sql("USE CATALOG workspace")
spark.sql("USE SCHEMA slooze_db")

from pyspark.sql.functions import avg, count

df = spark.table("indiamart_silver_products")

# KPI 1 – product count per category
df_products_per_category = (
    df.groupBy("category")
      .agg(count("*").alias("product_count"))
)

spark.sql("DROP TABLE IF EXISTS indiamart_gold_products_per_category")

df_products_per_category.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("indiamart_gold_products_per_category")

# KPI 2 – average price per category
df_avg_price = (
    df.groupBy("category")
      .agg(avg("price").alias("avg_price"))
)

spark.sql("DROP TABLE IF EXISTS indiamart_gold_avg_price_per_category")

df_avg_price.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("indiamart_gold_avg_price_per_category")

print("Gold tables created")

df_products_per_category.display()
df_avg_price.display()
