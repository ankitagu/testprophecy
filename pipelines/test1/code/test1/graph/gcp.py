from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from test1.config.ConfigStore import *
from test1.udfs.UDFs import *

def gcp(spark: SparkSession) -> DataFrame:
    return spark.read\
        .option("header", True)\
        .option("sep", ",")\
        .csv("s3://seceng-datalake-adobe-mavlink-gcp-refined-stage/")
