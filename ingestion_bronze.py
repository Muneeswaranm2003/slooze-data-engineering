
# Ingestion – Bronze layer

spark.sql("USE CATALOG workspace")
spark.sql("USE SCHEMA slooze_db")

from pyspark.sql import Row

# Simulated B2B marketplace feed
data = [
    {
        "product_name": "Industrial Air Compressor",
        "category": "industrial_machinery",
        "price": 25000,
        "supplier_name": "ABC Engineering",
        "supplier_location": "Chennai, Tamil Nadu"
    },
    {
        "product_name": "Hydraulic Press Machine",
        "category": "industrial_machinery",
        "price": 120000,
        "supplier_name": "XYZ Machines",
        "supplier_location": "Pune, Maharashtra"
    },
    {
        "product_name": "Electronic Control Panel",
        "category": "electronic_goods",
        "price": 18000,
        "supplier_name": "Delta Controls",
        "supplier_location": "Bengaluru, Karnataka"
    },
    {
        "product_name": "Industrial Sensor",
        "category": "electronic_goods",
        "price": 8000,
        "supplier_name": "Omega Systems",
        "supplier_location": "Hyderabad, Telangana"
    }
]

df_bronze = spark.createDataFrame([Row(**r) for r in data])

# Recreate clean table
spark.sql("DROP TABLE IF EXISTS indiamart_bronze_products")

df_bronze.write \
    .format("delta") \
    .mode("overwrite") \
    .option("mergeSchema", "true") \
    .saveAsTable("indiamart_bronze_products")

print("Bronze table created")
df_bronze.display()
