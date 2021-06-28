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
    
    delete_table_status = db.delete_table(TableName='dev_jobs')
    if(delete_table_status == True):
        logging.info("Table deleted successfully")
    else:
        logging.warning("Table delete operation failed")

    table_names = db.read_all_table_names()
    logging.info("Table names: {}".format(table_names))
    
"""Output

INFO:root: Table deleted successfully
INFO:root:Table names: ['user']
"""