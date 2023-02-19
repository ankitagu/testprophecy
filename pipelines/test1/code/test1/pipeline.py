from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from test1.config.ConfigStore import *
from test1.udfs.UDFs import *
from prophecy.utils import *
from test1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_gcp = gcp(spark)
    df_FlattenSchema_1 = FlattenSchema_1(spark, df_gcp)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/test1")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/test1")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
