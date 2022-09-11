from pyspark.sql import SparkSession, DataFrame
import jaydebeapi
from dotenv import load_dotenv

if __name__ == '__main__':

    spark = SparkSession.builder \
        .config("spark.driver.host", "localhost") \
        .getOrCreate()

    print(spark.sparkContext.getConf().getAll())
