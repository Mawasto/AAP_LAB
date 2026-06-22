import os
os.environ["JAVA_HOME"] = r"C:\Program Files\Eclipse Adoptium\jdk-17.0.19.10-hotspot"

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").getOrCreate()
print("Spark version:", spark.version)
spark.stop()