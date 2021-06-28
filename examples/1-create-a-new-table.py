from LucidDynamodb.Operations import DynamoDb
import os
import logging
import uuid
from boto3.dynamodb.conditions import Key
logging.basicConfig(level=logging.INFO)

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

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
    db = DynamoDb(region_name="us-east-1", 
                aws_access_key_id=AWS_ACCESS_KEY_ID, 
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
                
    table_creation_status = db.create_table(
                                    TableName=table_schema.get("TableName"),
                                    KeySchema=table_schema.get("KeySchema"),
                                    AttributeDefinitions=table_schema.get("AttributeDefinitions"),
                                    GlobalSecondaryIndexes=table_schema.get("GlobalSecondaryIndexes"),
                                    ProvisionedThroughput=table_schema.get("ProvisionedThroughput")
    )
    if(table_creation_status == True):
        logging.info("{} table created successfully".format(table_schema.get("TableName")))
    else:
        logging.error("{} table creation failed".format(table_schema.get("TableName")))

"""Output

INFO:root:dev_jobs table created successfully
"""