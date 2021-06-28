from LucidDynamodb.Operations import DynamoDb
import os
import logging
import uuid
from boto3.dynamodb.conditions import Key
logging.basicConfig(level=logging.INFO)

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

if __name__ == "__main__":
    db = DynamoDb(region_name="us-east-1", 
                aws_access_key_id=AWS_ACCESS_KEY_ID, 
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    table_names = db.read_all_table_names()
    logging.info("Table names: {}".format(table_names))

"""Output

INFO:root:Table names: ['dev_jobs', 'user']
"""