
# ETL – Silver layer

spark.sql("USE CATALOG workspace")
spark.sql("USE SCHEMA slooze_db")

from pyspark.sql.functions import col

df_raw = spark.table("indiamart_bronze_products")

df_silver = (
    df_raw
        .dropDuplicates(["product_name", "supplier_name"])
        .withColumn("price", col("price").cast("int"))
        .filter(col("product_name").isNotNull())
        .filter(col("supplier_name").isNotNull())
)

spark.sql("DROP TABLE IF EXISTS indiamart_silver_products")

df_silver.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("indiamart_silver_products")

print("Silver table created")
df_silver.display()
