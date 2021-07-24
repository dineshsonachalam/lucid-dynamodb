from LucidDynamodb import DynamoDb
from LucidDynamodb.exceptions import (
    TableNotFound
)
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    try:
        db = DynamoDb()
        db.delete_table(table_name='dev_jobs')
        logging.info("Table deleted successfully")
        table_names = db.read_all_table_names()
        logging.info(f"Table names: {table_names}")
    except TableNotFound as e:
        logging.error(f"Table delete operation failed {e}")

"""
dineshsonachalam@macbook examples % python 14-delete-a-table.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:Table deleted successfully
INFO:root:Table names: ['CertMagic', 'dev_test', 'kp-config-v1', 'test-1']
"""