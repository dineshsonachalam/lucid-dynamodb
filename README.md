<h1 align="center">
  <a href="https://pypi.org/project/LucidDynamodb" target="_blank">
    <img src="https://i.imgur.com/r9hHHUo.png" alt="LucidDynamodb">
  </a>
</h1>
<p align="center">
    <em>A minimalistic wrapper to AWS DynamoDB</em>
</p>

<p align="center">
    <a href="https://github.com/dineshsonachalam/Lucid-Dynamodb/actions" target="_blank">
        <img src="https://github.com/dineshsonachalam/Lucid-Dynamodb/actions/workflows/pypi-deploy.yml/badge.svg" alt="Deployment">
    </a>
    <a href="https://github.com/dineshsonachalam/Lucid-Dynamodb/actions" target="_blank">
        <img src="https://github.com/dineshsonachalam/Lucid-Dynamodb/workflows/markdown-autodocs/badge.svg" alt="Deployment">
    </a>
    <a href="https://pypi.org/project/LucidDynamodb" target="_blank">
        <img src="https://img.shields.io/pypi/v/LucidDynamodb?color=%2334D058&label=pypi%20package" alt="Package version">
    </a>
    <a href="https://github.com/dineshsonachalam/Lucid-Dynamodb/blob/master/LICENSE" target="_blank">
        <img src="https://badgen.net/github/license/dineshsonachalam/Lucid-Dynamodb" alt="MIT License" height="20">
    </a>
</p>

## Table of contents
- [Installation](#installation)
- [Example](#example)
    - [Connect to DynamodDB](#connect-to-dynamodb)
    - [Create a new table](#create-a-new-table)
    - [Get all table names](#get-all-table-names)
    - [Create a New Item](#create-a-new-item)
    - [Read an Item](#read-an-item)
    - [Increase an existing attribute value](#increase-an-existing-attribute-value)
    - [Update existing attribute in an item](#update-existing-attribute-in-an-item)
    - [Add a new attribute in an item](#add-a-new-attribute-in-an-item)
    - [Add an attribute to the list](#add-an-attribute-to-the-list)
    - [Add an attribute to the string set](#add-an-attribute-to-the-string-set)
    - [Delete an attribute from the string set](#delete-an-attribute-from-the-string-set)
    - [Delete an attribute from an item](#delete-an-attribute-from-an-item)
    - [Read items by filter](#read-items-by-filter)
    - [Delete a table](#delete-a-table)
- [Running tests](#running-tests)
- [Github Workflow Artifacts](#github-workflow-artifacts)
- [License](#license)


## Installation

<div class="termy">

```console
pip install LucidDynamodb
```
  
</div>

**Note:**  <a href="https://gist.github.com/dineshsonachalam/88f55b28c1f0c1ce93421f5a8f33e84a"> Prerequisite for Python3 development </a>


## Example

### Connect to DynamoDB
You can connect to DynamoDB by following any of these two ways.

1. Using AWS config
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/using-aws-config-to-connect-to-dynamodb.py) -->
<!-- The below code snippet is automatically added from ./examples/using-aws-config-to-connect-to-dynamodb.py -->
```py
from LucidDynamodb import DynamoDb
db = DynamoDb()

# $> pip install awscli  #can add user flag 
# $> aws configure
# AWS Access Key ID [****************ABCD]:[enter your key here]
# AWS Secret Access Key [****************xyz]:[enter your secret key here]
# Default region name [us-west-2]:[enter your region here]
# Default output format [None]:
```
<!-- MARKDOWN-AUTO-DOCS:END -->

2. Using AWS secret key
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/using-aws-secret-to-connect-to-dynamodb.py) -->
<!-- The below code snippet is automatically added from ./examples/using-aws-secret-to-connect-to-dynamodb.py -->
```py
from LucidDynamodb import DynamoDb
import os
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
db = DynamoDb(region_name="us-east-1", 
              aws_access_key_id=AWS_ACCESS_KEY_ID, 
              aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
```
<!-- MARKDOWN-AUTO-DOCS:END -->

### Create a new table
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/1-create-a-new-table.py) -->
<!-- The below code snippet is automatically added from ./examples/1-create-a-new-table.py -->
```py
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
        
"""
dineshsonachalam@macbook examples % python 1-create-a-new-table.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:dev_jobs table created successfully
"""
```
<!-- MARKDOWN-AUTO-DOCS:END -->

### Get all table names
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/2-get-all-table-names.py) -->
<!-- The below code snippet is automatically added from ./examples/2-get-all-table-names.py -->
```py
from LucidDynamodb import DynamoDb
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
```
<!-- MARKDOWN-AUTO-DOCS:END -->

### Create a New Item
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/3-create-a-new-item.py) -->
<!-- The below code snippet is automatically added from ./examples/3-create-a-new-item.py -->
```py
from LucidDynamodb import DynamoDb
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    db = DynamoDb()
    item_creation_status = db.create_item(
        TableName="dev_jobs", 
        Item={
            "company_name": "Google",
            "role_id": "111",
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
        
"""
dineshsonachalam@macbook examples % python 3-create-a-new-item.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:Item created successfully
"""
```
<!-- MARKDOWN-AUTO-DOCS:END -->

### Read an Item
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/4-read-an-item.py) -->
<!-- The below code snippet is automatically added from ./examples/4-read-an-item.py -->
```py
from LucidDynamodb import DynamoDb
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    db = DynamoDb()
    item = db.read_item(
        TableName="dev_jobs", 
        Key={
            "company_name": "Google",
            "role_id": "111"
        })
    if(item != None):
        logging.info("Item: {}".format(item))
    else:
        logging.warning("Item doesn't exist")
        
"""
dineshsonachalam@macbook examples % python 4-read-an-item.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:Item: {
	'locations': ['Mountain View, California', 'Austin, Texas', 'Chicago, IL'],
	'role_id': '111',
	'overall_review': {
		'compensation_and_benefits': '3.9/5',
		'overall_rating': '4/5'
	},
	'company_name': 'Google',
	'role': 'Software Engineer 1',
	'yearly_hike_percent': Decimal('8'),
	'salary': '$1,50,531',
	'benefits': {
		'Travel reimbursements',
		'Internet, Medical, Edu reimbursements',
		'Health insurance'
	}
}
"""
```
<!-- MARKDOWN-AUTO-DOCS:END -->

### Increase an existing attribute value
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/5-increase-an-existing-attribute-value.py) -->
<!-- The below code snippet is automatically added from ./examples/5-increase-an-existing-attribute-value.py -->
```py
from LucidDynamodb import DynamoDb
import os
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    db = DynamoDb()
    
    increase_attribute_status = db.increase_attribute_value(
        TableName='dev_jobs',
        Key={
            "company_name": "Google",
            "role_id": "111"
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
            "role_id": "111"
        })
    if(item != None):
        logging.info("Item: {}".format(item))
    else:
        logging.warning("Item doesn't exist") 

"""
dineshsonachalam@macbook examples % python 5-increase-an-existing-attribute-value.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:Attribute value increment completed
INFO:root:Item: {
	'locations': ['Mountain View, California', 'Austin, Texas', 'Chicago, IL'],
	'role_id': '111',
	'overall_review': {
		'compensation_and_benefits': '3.9/5',
		'overall_rating': '4/5'
	},
	'company_name': 'Google',
	'role': 'Software Engineer 1',
	'yearly_hike_percent': Decimal('13'),
	'salary': '$1,50,531',
	'benefits': {
		'Internet, Medical, Edu reimbursements',
		'Health insurance',
		'Travel reimbursements'
	}
}
"""
```
<!-- MARKDOWN-AUTO-DOCS:END -->

### Update existing attribute in an item
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/6-update-existing-attribute-in-an-item.py) -->
<!-- The below code snippet is automatically added from ./examples/6-update-existing-attribute-in-an-item.py -->
```py
from LucidDynamodb import DynamoDb
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    db = DynamoDb() 
    item_update_status = db.update_item(
        TableName="dev_jobs", 
        Key={
            "company_name": "Google",
            "role_id": "111"
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
            "role_id": "111"
        })
    if(item != None):
        logging.info("Item: {}".format(item))
    else:
        logging.warning("Item doesn't exist")

"""
dineshsonachalam@macbook examples % python 6-update-existing-attribute-in-an-item.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:Update is successful
INFO:root:Item: {
	'locations': ['Mountain View, California', 'Austin, Texas', 'Chicago, IL'],
	'role_id': '111',
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
"""
```
<!-- MARKDOWN-AUTO-DOCS:END -->

### Add a new attribute in an item
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/7-add-a-new-attribute-in-an-item.py) -->
<!-- The below code snippet is automatically added from ./examples/7-add-a-new-attribute-in-an-item.py -->
```py
from LucidDynamodb import DynamoDb
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    db = DynamoDb()
    item_update_status = db.update_item(
        TableName="dev_jobs", 
        Key={
            "company_name": "Google",
            "role_id": "111"
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
            "role_id": "111"
        })
    if(item != None):
        logging.info("Item: {}".format(item))
    else:
        logging.warning("Item doesn't exist")
        
"""
dineshsonachalam@macbook examples % python 7-add-a-new-attribute-in-an-item.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:Update is successful
INFO:root:Item: {
	'locations': ['Mountain View, California', 'Austin, Texas', 'Chicago, IL'],
	'role_id': '111',
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
"""
```
<!-- MARKDOWN-AUTO-DOCS:END -->

### Add an attribute to the list
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/8-add-an-attribute-to-the-list.py) -->
<!-- The below code snippet is automatically added from ./examples/8-add-an-attribute-to-the-list.py -->
```py
from LucidDynamodb import DynamoDb
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    db = DynamoDb()
    
    item_update_status = db.update_item(
        TableName="dev_jobs", 
        Key={
            "company_name": "Google",
            "role_id": "111"
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
            "role_id": "111"
        })
    if(item != None):
        logging.info("Item: {}".format(item))
    else:
        logging.warning("Item doesn't exist")

"""
dineshsonachalam@macbook examples % python 8-add-an-attribute-to-the-list.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:Update is successful
INFO:root:Item: {
	'locations': ['Mountain View, California', 'Austin, Texas', 'Chicago, IL', 'Detroit, Michigan'],
	'role_id': '111',
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
		'Travel reimbursements',
		'Internet, Medical, Edu reimbursements',
		'Health insurance'
	}
}
"""
```
<!-- MARKDOWN-AUTO-DOCS:END -->

### Add an attribute to the string set
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/9-add-an-attribute-to-the-string-set.py) -->
<!-- The below code snippet is automatically added from ./examples/9-add-an-attribute-to-the-string-set.py -->
```py
from LucidDynamodb import DynamoDb
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    db = DynamoDb()
    
    item_update_status = db.update_item(
        TableName="dev_jobs", 
        Key={
            "company_name": "Google",
            "role_id": "111"
        },
        AttributesToUpdate={
            'benefits': "Free Food"
        },
        Operation="ADD_ATTRIBUTE_TO_STRING_SET"
    )
    if(item_update_status == True):
        logging.info("Update is successful")
    else:
        logging.warning("Update failed")

    item = db.read_item(
        TableName="dev_jobs", 
        Key={
            "company_name": "Google",
            "role_id": "111"
        })
    if(item != None):
        logging.info("Item: {}".format(item))
    else:
        logging.warning("Item doesn't exist")
        
"""
dineshsonachalam@macbook examples % python 9-add-an-attribute-to-the-string-set.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:Update is successful
INFO:root:Item: {
	'locations': ['Mountain View, California', 'Austin, Texas', 'Chicago, IL', 'Detroit, Michigan'],
	'role_id': '111',
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
		'Travel reimbursements',
		'Internet, Medical, Edu reimbursements',
		'Health insurance',
		'Free Food'
	}
}
"""
```
<!-- MARKDOWN-AUTO-DOCS:END -->

### Delete an attribute from the string set
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/10-delete-an-attribute-from-the-string-set.py) -->
<!-- The below code snippet is automatically added from ./examples/10-delete-an-attribute-from-the-string-set.py -->
```py
from LucidDynamodb import DynamoDb
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    db = DynamoDb()
    
    item_update_status = db.update_item(
        TableName="dev_jobs", 
        Key={
            "company_name": "Google",
            "role_id": "111"
        },
        AttributesToUpdate={
            'benefits': "Free Food"
        },
        Operation="DELETE_ATTRIBUTE_FROM_STRING_SET"
    )
    if(item_update_status == True):
        logging.info("Update is successful")
    else:
        logging.warning("Update failed")

    item = db.read_item(
        TableName="dev_jobs", 
        Key={
            "company_name": "Google",
            "role_id": "111"
        })
    if(item != None):
        logging.info("Item: {}".format(item))
    else:
        logging.warning("Item doesn't exist")

"""
dineshsonachalam@macbook examples % python 10-delete-an-attribute-from-the-string-set.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:Update is successful
INFO:root:Item: {
	'locations': ['Mountain View, California', 'Austin, Texas', 'Chicago, IL', 'Detroit, Michigan'],
	'role_id': '111',
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
"""
```
<!-- MARKDOWN-AUTO-DOCS:END -->

### Delete an attribute from an item
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/11-delete-an-attribute-from-an-item.py) -->
<!-- The below code snippet is automatically added from ./examples/11-delete-an-attribute-from-an-item.py -->
```py
from LucidDynamodb import DynamoDb
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    db = DynamoDb()
    
    attribute_delete_status = db.delete_attribute(
        TableName="dev_jobs", 
        Key={
              "company_name": "Google",
              "role_id": "111"
        }, 
        AttributeName="yearly_hike_percent")

    if(attribute_delete_status == True):
        logging.info("The attribute is deleted successfully")
    else:
        logging.warning("The attribute delete operation failed")

    item = db.read_item(
        TableName="dev_jobs", 
        Key={
            "company_name": "Google",
            "role_id": "111"
        })
    if(item != None):
        logging.info("Item: {}".format(item))
    else:
        logging.warning("Item doesn't exist")

"""
dineshsonachalam@macbook examples % python 11-delete-an-attribute-from-an-item.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:The attribute is deleted successfully
INFO:root:Item: {
	'locations': ['Mountain View, California', 'Austin, Texas', 'Chicago, IL', 'Detroit, Michigan'],
	'role_id': '111',
	'overall_review': {
		'compensation_and_benefits': '3.9/5',
		'overall_rating': '4/5',
		'yearly_bonus_percent': Decimal('12')
	},
	'company_name': 'Google',
	'role': 'Staff Software Engineer 2',
	'salary': '$1,50,531',
	'benefits': {
		'Internet, Medical, Edu reimbursements',
		'Travel reimbursements',
		'Health insurance'
	}
}
"""
```
<!-- MARKDOWN-AUTO-DOCS:END -->

### Read items by filter
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/12-read-items-by-filter.py) -->
<!-- The below code snippet is automatically added from ./examples/12-read-items-by-filter.py -->
```py
from LucidDynamodb import DynamoDb
import logging
from boto3.dynamodb.conditions import Key
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    db = DynamoDb()
    
    item_creation_status = db.create_item(
        TableName="dev_jobs", 
        Item={
            "company_name": "Google",
            "role_id": "112",
            "role": "Software Architect",
            "salary": "$4,80,000",
            "locations": ["Mountain View, California"],
            "yearly_hike_percent": 13,
            "benefits": set(["Internet reimbursements"]),
            "overall_review":{
                "overall_rating" : "3/5",
                "compensation_and_benefits": "4.2/5"
            }
        }
    )
    if(item_creation_status == True):
        logging.info("Item created successfully")
    else:
        logging.warning("Item creation failed")
    
    items = db.read_items_by_filter(
                    TableName='dev_jobs', 
                    KeyConditionExpression=Key("company_name").eq("Google") 
    )
    
    if(len(items)>0):
        logging.info("Items: {}".format(items))
    else:
        logging.warning("Items doesn't exist")
        
"""
dineshsonachalam@macbook examples % python 12-read-items-by-filter.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:Item created successfully
INFO:root:Items: [{
	'locations': ['Mountain View, California', 'Austin, Texas', 'Chicago, IL', 'Detroit, Michigan'],
	'role_id': '111',
	'overall_review': {
		'compensation_and_benefits': '3.9/5',
		'overall_rating': '4/5',
		'yearly_bonus_percent': Decimal('12')
	},
	'company_name': 'Google',
	'role': 'Staff Software Engineer 2',
	'salary': '$1,50,531',
	'benefits': {
		'Internet, Medical, Edu reimbursements',
		'Travel reimbursements',
		'Health insurance'
	}
}, {
	'locations': ['Mountain View, California'],
	'role_id': '112',
	'overall_review': {
		'compensation_and_benefits': '4.2/5',
		'overall_rating': '3/5'
	},
	'company_name': 'Google',
	'role': 'Software Architect',
	'yearly_hike_percent': Decimal('13'),
	'salary': '$4,80,000',
	'benefits': {
		'Internet reimbursements'
	}
}]
"""
```
<!-- MARKDOWN-AUTO-DOCS:END -->

### Delete a table
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/13-delete-a-table.py) -->
<!-- The below code snippet is automatically added from ./examples/13-delete-a-table.py -->
```py
from LucidDynamodb import DynamoDb
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
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## Running Tests

To run tests, run the following command

```bash
pytest -s
```

## Github Workflow Artifacts

<!-- MARKDOWN-AUTO-DOCS:START (WORKFLOW_ARTIFACT_TABLE) -->
<table class="ARTIFACTS-TABLE"><thead><tr><th class="artifact-th">Artifact</th><th class="workflow-th">Workflow</th></tr></thead><tbody ><tr ><td class="artifact-td td_text"><a href=https://github.com/dineshsonachalam/lucid-dynamodb/suites/3209758451/artifacts/74241012>dependency-graph</a></td><td class="workflow-td td_text"><a href=https://github.com/dineshsonachalam/lucid-dynamodb/actions/runs/1020252377>integration-tests</a></td></tr>
<tr ><td class="artifact-td td_text"><a href=https://github.com/dineshsonachalam/lucid-dynamodb/suites/3209758451/artifacts/74241013>module-dependencies-license-report</a></td><td class="workflow-td td_text"><a href=https://github.com/dineshsonachalam/lucid-dynamodb/actions/runs/1020252377>integration-tests</a></td></tr>
<tr ><td class="artifact-td td_text"><a href=https://github.com/dineshsonachalam/lucid-dynamodb/suites/3209758451/artifacts/74241014>Pytest-report</a></td><td class="workflow-td td_text"><a href=https://github.com/dineshsonachalam/lucid-dynamodb/actions/runs/1020252377>integration-tests</a></td></tr></tbody></table>
<!-- MARKDOWN-AUTO-DOCS:END -->

## License

[MIT](https://choosealicense.com/licenses/mit/) © [dineshsonachalam](https://www.github.com/dineshsonachalam)
