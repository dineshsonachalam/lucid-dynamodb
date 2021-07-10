from LucidDynamodb.Operations import DynamoDb
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    db = DynamoDb()
    table_names = db.read_all_table_names()
    logging.info("Table names: {}".format(table_names))
    
"""
dineshsonachalam@macbook examples % python 2-get-all-table-names.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:Table names: ['dev_jobs', 'dev_test']
"""