from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("RenewableEnergyStream") \
    .master("local[*]") \
    .getOrCreate()

print("✅ Spark started successfully!")

spark.stop()