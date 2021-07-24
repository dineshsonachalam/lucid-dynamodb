from LucidDynamodb import DynamoDb
from LucidDynamodb.exceptions import (
    TableAlreadyExists
)
import logging
logging.basicConfig(level=logging.INFO)

table_schema = {
	"TableName": "dev_jobs",
	"KeySchema": [
        {
            "AttributeName": "company_name",
            "KeyType": "HASH"
	    },
        {
            "AttributeName": "role_id",
            "KeyType": "RANGE"
	    }
    ],
	"AttributeDefinitions": [
        {
            "AttributeName": "company_name",
            "AttributeType": "S"
	    },
        {
            "AttributeName": "role_id",
            "AttributeType": "S"
	    }
     ],
	"GlobalSecondaryIndexes": [],
	"ProvisionedThroughput": {
		"ReadCapacityUnits": 1,
		"WriteCapacityUnits": 1
	}
}

if __name__ == "__main__":
    try:
        db = DynamoDb()
        db.create_table(
            table_name=table_schema.get("TableName"),
            key_schema=table_schema.get("KeySchema"),
            attribute_definitions=table_schema.get("AttributeDefinitions"),
            global_secondary_indexes=table_schema.get("GlobalSecondaryIndexes"),
            provisioned_throughput=table_schema.get("ProvisionedThroughput")
        )
        logging.info(f"{table_schema.get('TableName')} table created successfully")
    except TableAlreadyExists as e:
        logging.error(f"{table_schema.get('TableName')} table creation failed - {e}")

"""
dineshsonachalam@macbook examples % python 1-create-a-new-table.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:dev_jobs table created successfully
"""