from LucidDynamodb import DynamoDb
from LucidDynamodb.exceptions import (
    UnexpectedError
)
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    try:
        db = DynamoDb()
        table_names = db.read_all_table_names()
        logging.info(f"Table names: {table_names}")
    except UnexpectedError as e:
        logging.error(f"Read all table names failed - {e}")

"""
dineshsonachalam@macbook examples % python 2-get-all-table-names.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:Table names: ['CertMagic', 'dev_jobs', 'dev_test', 'kp-config-v1', 'test-1']
"""