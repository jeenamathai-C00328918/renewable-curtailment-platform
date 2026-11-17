from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    from_json,
    to_timestamp
)
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType
)

# Create Spark Session
spark = SparkSession.builder \
    .appName("RenewableEnergyStream") \
    .master("local[*]") \
    .config(
        "spark.jars",
        "jars/postgresql-42.7.13.jar"
    ) \
    .config(
        "spark.jars.packages",
        "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3"
    ) \
    .getOrCreate()

print("✅ Spark started!")

# Read from Kafka
df = spark.readStream \
    .format("kafka") \
    .option(
        "kafka.bootstrap.servers",
        "localhost:9092"
    ) \
    .option(
        "subscribe",
        "renewable-energy"
    ) \
    .load()

print("✅ Kafka connected!")

# JSON schema
schema = StructType([
    StructField(
        "timestamp",
        StringType(),
        True
    ),
    StructField(
        "wind_generation",
        IntegerType(),
        True
    ),
    StructField(
        "electricity_demand",
        IntegerType(),
        True
    )
])

# Parse Kafka JSON
json_df = df.select(
    from_json(
        col("value").cast("string"),
        schema
    ).alias("data")
)

parsed_df = json_df.select("data.*")

# Convert timestamp string to timestamp type
parsed_df = parsed_df.withColumn(
    "timestamp",
    to_timestamp(col("timestamp"))
)

# Function to write each batch to PostgreSQL
def write_to_postgres(batch_df, batch_id):

    print(f"\n✅ Writing batch {batch_id}")

    batch_df.show(truncate=False)

    batch_df.write \
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

    print(f"✅ Batch {batch_id} written successfully")


# Start Streaming
query = parsed_df.writeStream \
    .foreachBatch(write_to_postgres) \
    .start()

query.awaitTermination()