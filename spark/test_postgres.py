from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp

spark = SparkSession.builder \
    .appName("PostgresTest") \
    .master("local[*]") \
    .config(
        "spark.jars",
        "jars/postgresql-42.7.13.jar"
    ) \
    .getOrCreate()

# Test data
data = [
    ("2026-11-17 21:00:00", 2500, 5000)
]

# Create DataFrame
df = spark.createDataFrame(
    data,
    ["timestamp", "wind_generation", "electricity_demand"]
)

# Convert string to timestamp
df = df.withColumn(
    "timestamp",
    to_timestamp(col("timestamp"))
)

# Verify schema
df.printSchema()

# Write to PostgreSQL
df.write \
    .format("jdbc") \
    .option(
        "url",
        "jdbc:postgresql://127.0.0.1:5432/energydb"
    ) \
    .option(
        "dbtable",
        "renewable_energy"
    ) \
    .option(
        "user",
        "admin"
    ) \
    .option(
        "password",
        "admin123"
    ) \
    .option(
        "driver",
        "org.postgresql.Driver"
    ) \
    .mode("append") \
    .save()

print("✅ Success! Data inserted into PostgreSQL.")

spark.stop()