
import psycopg2
from src.config_parser import Config



config = Config().config


con=psycopg2.connect(dbname=config.redshift_fashion.dbname,
                     host=config.redshift_fashion.host,
                     port=config.redshift_fashion.port,
                     user=config.redshift_fashion.user,
                     password=config.redshift_fashion.password)

cur = con.cursor()
cur.execute("SELECT * FROM pg_namespace")
cur.fetchall()


