from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from test1.config.ConfigStore import *
from test1.udfs.UDFs import *

def FlattenSchema_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select()
