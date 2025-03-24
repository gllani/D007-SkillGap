from pyspark.sql import SparkSession

def initialize_spark():
    spark = SparkSession.builder.appName("SkillGapETL").getOrCreate()
    return spark

def etl_pipeline():
    spark = initialize_spark()
    # Load data, clean, process
    print("Running ETL pipeline...")
    spark.stop()