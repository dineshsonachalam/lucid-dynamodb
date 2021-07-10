from LucidDynamodb.Operations import DynamoDb
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    db = DynamoDb()
    
    delete_table_status = db.delete_table(TableName='dev_jobs')
    if(delete_table_status == True):
        logging.info("Table deleted successfully")
    else:
        logging.warning("Table delete operation failed")

    table_names = db.read_all_table_names()
    logging.info("Table names: {}".format(table_names))
    
"""
dineshsonachalam@macbook examples % python 13-delete-a-table.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:Table deleted successfully
INFO:root:Table names: ['dev_test']
"""