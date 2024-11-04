
import psycopg2
import boto3
from src.config_parser import Config




def initialize():
    config = Config().config
    return config


def collect_data():
    pass


def process_data():
    pass


def make_db():
    pass


def main():
    pass




config = initialize()


### redshift
con=psycopg2.connect(dbname=config.redshift_fashion.dbname,
                     host=config.redshift_fashion.host,
                     port=config.redshift_fashion.port,
                     user=config.redshift_fashion.user,
                     password=config.redshift_fashion.password)

cur = con.cursor()
cur.execute("SELECT * FROM pg_namespace")
cur.fetchall()


### S3
s3 = boto3.resource(
    service_name=config.s3_fashion.service_name,
    region_name=config.s3_fashion.region_name,
    aws_access_key_id=config.s3_fashion.aws_access_key_id,
    aws_secret_access_key=config.s3_fashion.aws_access_key
)

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)




if __name__ == "__main__":
    main()







