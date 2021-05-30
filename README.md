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
pip install LucidDynamodb
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
### 3. Create a New Item

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

    item_creation_status = db.create_item(
        TableName="dev_jobs", 
        Item={
            "company_name": "Google",
            "role_id": str(uuid.uuid4()),
            "role": "Software Engineer 1",
            "salary": "$1,50,531",
            "locations": ["Mountain View, California", "Austin, Texas", "Chicago, IL"],
            "yearly_hike_percent": 8,
            "benefits": set(["Internet, Medical, Edu reimbursements", 
                             "Health insurance",
                             "Travel reimbursements"
                             ]),
            "overall_review":{
                "overall_rating" : "4/5",
                "compensation_and_benefits": "3.9/5"
            }
        }
    )
    if(item_creation_status == True):
        logging.info("Item created successfully")
    else:
        logging.warning("Item creation failed")
```
**Output:**
```
INFO:root:Item created successfully
```

### 4. Read an Item

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
    item = db.read_item(
        TableName="dev_jobs", 
        Key={
            "company_name": "Google",
            "role_id": "e85f79a7-0857-4086-afbd-da13ec76b442"
        })
    if(item != None):
        logging.info("Item: {}".format(item))
    else:
        logging.warning("Item doesn't exist")
```
**Output:**
```
INFO:root:Item: 
{
	'locations': ['Mountain View, California', 'Austin, Texas', 'Chicago, IL'],
	'role_id': 'e85f79a7-0857-4086-afbd-da13ec76b442',
	'overall_review': {
		'compensation_and_benefits': '3.9/5',
		'overall_rating': '4/5'
	},
	'company_name': 'Google',
	'role': 'Software Engineer 1',
	'yearly_hike_percent': Decimal('8'),
	'salary': '$1,50,531',
	'benefits': {
		'Health insurance',
		'Travel reimbursements',
		'Internet, Medical, Edu reimbursements'
	}
}
```
### 5. Increase an existing attribute value

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
    
    increase_attribute_status = db.increase_attribute_value(
        TableName='dev_jobs',
        Key={
            "company_name": "Google",
            "role_id": "e85f79a7-0857-4086-afbd-da13ec76b442"
        },
        AttributeName="yearly_hike_percent",
        IncrementValue=5
    )
    
    if(increase_attribute_status==True):
        logging.info("Attribute value increment completed")
    else:
        logging.warning("Attribute value increment failed")
    
    item = db.read_item(
        TableName='dev_jobs', 
        Key={
            "company_name": "Google",
            "role_id": "e85f79a7-0857-4086-afbd-da13ec76b442"
        })
    if(item != None):
        logging.info("Item: {}".format(item))
    else:
        logging.warning("Item doesn't exist") 
```
**Output:**
```
INFO:root: Attribute value increment completed
INFO:root: Item: 
{
	'locations': ['Mountain View, California', 'Austin, Texas', 'Chicago, IL'],
	'role_id': 'e85f79a7-0857-4086-afbd-da13ec76b442',
	'overall_review': {
		'compensation_and_benefits': '3.9/5',
		'overall_rating': '4/5'
	},
	'company_name': 'Google',
	'role': 'Software Engineer 1',
	'yearly_hike_percent': Decimal('13'),
	'salary': '$1,50,531',
	'benefits': {
		'Health insurance',
		'Travel reimbursements',
		'Internet, Medical, Edu reimbursements'
	}
}
```
### 6. Update existing attribute in an item

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
    
    item_update_status = db.update_item(
        TableName="dev_jobs", 
        Key={
            "company_name": "Google",
            "role_id": "e85f79a7-0857-4086-afbd-da13ec76b442"
        },
        AttributesToUpdate={
            'role': 'Staff Software Engineer 2'
        }
    )
    if(item_update_status == True):
        logging.info("Update is successful")
    else:
        logging.warning("Update failed")

    item = db.read_item(
        TableName="dev_jobs", 
        Key={
            "company_name": "Google",
            "role_id": "e85f79a7-0857-4086-afbd-da13ec76b442"
        })
    if(item != None):
        logging.info("Item: {}".format(item))
    else:
        logging.warning("Item doesn't exist")
```
**Output:**
```
INFO:root:Update is successful
INFO:root:Item: 
{
	'locations': ['Mountain View, California', 'Austin, Texas', 'Chicago, IL'],
	'role_id': 'e85f79a7-0857-4086-afbd-da13ec76b442',
	'overall_review': {
		'compensation_and_benefits': '3.9/5',
		'overall_rating': '4/5'
	},
	'company_name': 'Google',
	'role': 'Staff Software Engineer 2',
	'yearly_hike_percent': Decimal('13'),
	'salary': '$1,50,531',
	'benefits': {
		'Internet, Medical, Edu reimbursements',
		'Travel reimbursements',
		'Health insurance'
	}
}
```

### 7. Add a new attribute in an item

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
    
    item_update_status = db.update_item(
        TableName="dev_jobs", 
        Key={
            "company_name": "Google",
            "role_id": "e85f79a7-0857-4086-afbd-da13ec76b442"
        },
        AttributesToUpdate={
            'overall_review.yearly_bonus_percent': 12
        }
    )
    if(item_update_status == True):
        logging.info("Update is successful")
    else:
        logging.warning("Update failed")

    item = db.read_item(
        TableName="dev_jobs", 
        Key={
            "company_name": "Google",
            "role_id": "e85f79a7-0857-4086-afbd-da13ec76b442"
        })
    if(item != None):
        logging.info("Item: {}".format(item))
    else:
        logging.warning("Item doesn't exist")
```
**Output:**
```
INFO:root:Update is successful
INFO:root:Item: 
{
	'locations': ['Mountain View, California', 'Austin, Texas', 'Chicago, IL'],
	'role_id': 'e85f79a7-0857-4086-afbd-da13ec76b442',
	'overall_review': {
		'compensation_and_benefits': '3.9/5',
		'overall_rating': '4/5',
		'yearly_bonus_percent': Decimal('12')
	},
	'company_name': 'Google',
	'role': 'Staff Software Engineer 2',
	'yearly_hike_percent': Decimal('13'),
	'salary': '$1,50,531',
	'benefits': {
		'Internet, Medical, Edu reimbursements',
		'Travel reimbursements',
		'Health insurance'
	}
}
```
### 8. Add an attribute to the list

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
    
    item_update_status = db.update_item(
        TableName="dev_jobs", 
        Key={
            "company_name": "Google",
            "role_id": "e85f79a7-0857-4086-afbd-da13ec76b442"
        },
        AttributesToUpdate={
            'locations': "Detroit, Michigan"
        },
        Operation="ADD_ATTRIBUTE_TO_LIST"
    )
    if(item_update_status == True):
        logging.info("Update is successful")
    else:
        logging.warning("Update failed")

    item = db.read_item(
        TableName="dev_jobs", 
        Key={
            "company_name": "Google",
            "role_id": "e85f79a7-0857-4086-afbd-da13ec76b442"
        })
    if(item != None):
        logging.info("Item: {}".format(item))
    else:
        logging.warning("Item doesn't exist")
```
**Output:**
```
INFO:root:Update is successful
INFO:root:Item: 
{
	'locations': ['Mountain View, California', 'Austin, Texas', 'Chicago, IL', 'Detroit, Michigan'],
	'role_id': 'e85f79a7-0857-4086-afbd-da13ec76b442',
	'overall_review': {
		'compensation_and_benefits': '3.9/5',
		'overall_rating': '4/5',
		'yearly_bonus_percent': Decimal('12')
	},
	'company_name': 'Google',
	'role': 'Staff Software Engineer 2',
	'yearly_hike_percent': Decimal('13'),
	'salary': '$1,50,531',
	'benefits': {
		'Health insurance',
		'Internet, Medical, Edu reimbursements',
		'Travel reimbursements'
	}
}
```



