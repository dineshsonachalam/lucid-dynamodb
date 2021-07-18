from LucidDynamodb import DynamoDb
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
    db = DynamoDb()
    table_creation_status = db.create_table(
                                    table_name=table_schema.get("TableName"),
                                    key_schema=table_schema.get("KeySchema"),
                                    attribute_definitions=table_schema.get("AttributeDefinitions"),
                                    global_secondary_indexes=table_schema.get("GlobalSecondaryIndexes"),
                                    provisioned_throughput=table_schema.get("ProvisionedThroughput")
    )
    try:
        logging.info("{} table created successfully".format(table_schema.get("TableName")))
    except Exception as e:
        logging.error("{} table creation failed - {}".format(table_schema.get("TableName"), e))
"""
dineshsonachalam@macbook examples % python 1-create-a-new-table.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:dev_jobs table created successfully
"""