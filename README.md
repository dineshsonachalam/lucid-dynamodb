<p align="center">
  <img src="https://i.imgur.com/r9hHHUo.png" alt="LucidDynamodb">
</p>
<p align="center">
    <em>A minimalistic wrapper to AWS DynamoDB</em>
</p>
<p align="center">
  
<a href="https://github.com/dineshsonachalam/Lucid-Dynamodb/actions" target="_blank">
    <img src="https://github.com/dineshsonachalam/Lucid-Dynamodb/actions/workflows/pypi-deploy.yml/badge.svg" alt="Deployment">
</a>
  
<a href="https://pypi.org/project/LucidDynamodb" target="_blank">
    <img src="https://img.shields.io/pypi/v/LucidDynamodb?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
</p>

## Installation

<div class="termy">

```console
$ pip install LucidDynamodb
```
  
</div>

**Note:**  <a href="https://gist.github.com/dineshsonachalam/88f55b28c1f0c1ce93421f5a8f33e84a"> Prerequisite for Python3 development </a>

## Example

### 1. Create a new table

```Python
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
```
**Output:**
```
INFO:root:dev_jobs table created successfully
```

### 2. Get all table names

```Python
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
```
**Output:**
```
INFO:root:Table names: ['dev_jobs', 'user']
```





