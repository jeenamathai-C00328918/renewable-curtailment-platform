from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("RenewableEnergyStream") \
    .master("local[*]") \
    .config(
        "spark.jars.packages",
        "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3"
    ) \
    .getOrCreate()

print("Spark started!")

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "renewable-energy") \
    .load()

print("Kafka connected!")

query = df.selectExpr(
    "CAST(value AS STRING)"
).writeStream \
 .outputMode("append") \
 .format("console") \
 .start()

query.awaitTermination()