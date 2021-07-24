<h1 align="center">
  <a href="https://pypi.org/project/LucidDynamodb" target="_blank">
    <img src="https://i.imgur.com/r9hHHUo.png" alt="LucidDynamodb">
  </a>
</h1>
<p align="center">
    <em>A minimalistic wrapper to <a href="https://aws.amazon.com/dynamodb">AWS DynamoDB</a></em>
</p>
<p align="center">
    <a href="https://sonarcloud.io/dashboard?id=lucid-dynamodb">
        <img src="https://sonarcloud.io/api/project_badges/quality_gate?project=lucid-dynamodb"/>
    </a>
</p>

<p align="center">
    <a href="https://www.codacy.com/gh/dineshsonachalam/lucid-dynamodb/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dineshsonachalam/lucid-dynamodb&amp;utm_campaign=Badge_Grade">
        <img src="https://app.codacy.com/project/badge/Grade/3607dfd408bb4b7394cb0631b717a76e"/>
    </a>
    <a href="https://snyk.io/test/github/dineshsonachalam/lucid-dynamodb">
        <img src="https://snyk.io/test/github/dineshsonachalam/lucid-dynamodb/badge.svg"/>
    </a>
    <a href="https://github.com/dineshsonachalam/Lucid-Dynamodb/actions" target="_blank">
        <img src="https://github.com/dineshsonachalam/Lucid-Dynamodb/actions/workflows/pypi-deploy.yml/badge.svg" alt="Deployment">
    </a>
    <a href="https://pypi.org/project/LucidDynamodb" target="_blank">
        <img src="https://img.shields.io/pypi/v/LucidDynamodb?color=%2334D058&label=pypi%20package" alt="Package version">
    </a>
    <a href="https://github.com/dineshsonachalam/Lucid-Dynamodb/blob/master/LICENSE" target="_blank">
        <img src="https://badgen.net/github/license/dineshsonachalam/Lucid-Dynamodb" alt="MIT License" height="20">
    </a>
</p>

Useful links:
- See the full documentation at https://lucid-dynamodb.dineshsonachalam.com
- Ask questions in the <a href ="https://github.com/dineshsonachalam/lucid-dynamodb/issues">GitHub issues</a>

## Table of contents
- [Installation](#installation)
- [Example](#example)
    - [Connect to DynamodDB](#connect-to-dynamodb)
    - [Create a new table](#create-a-new-table)
    - [Get all table names](#get-all-table-names)
    - [Create a New Item](#create-a-new-item)
    - [Read an Item](#read-an-item)
    - [Read items by filter](#read-items-by-filter)
    - [Update existing attribute in an item](#update-existing-attribute-in-an-item)
    - [Add a new attribute in an item](#add-a-new-attribute-in-an-item)
    - [Add an attribute to the list](#add-an-attribute-to-the-list)
    - [Add an attribute to the string set](#add-an-attribute-to-the-string-set)
    - [Increase an existing attribute value](#increase-an-existing-attribute-value)
    - [Delete an attribute from an item](#delete-an-attribute-from-an-item)
    - [Delete an attribute from the string set](#delete-an-attribute-from-the-string-set)
    - [Delete an item](#delete-an-item)
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

#### Connect to DynamoDB
You can connect to DynamoDB by following any of these two ways.

1. Using AWS config
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/using-aws-config-to-connect-to-dynamodb.py) -->
<!-- The below code snippet is automatically added from ./examples/using-aws-config-to-connect-to-dynamodb.py -->
```py
from LucidDynamodb import DynamoDb
db = DynamoDb()

"""
$ pip install awscli  #can add user flag
$ aws configure
AWS Access Key ID [****************ABCD]:[enter your key here]
AWS Secret Access Key [****************xyz]:[enter your secret key here]
Default region name [us-west-2]:[enter your region here]
Default output format [None]:
"""
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

#### Create a new table
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/1-create-a-new-table.py) -->
<!-- The below code snippet is automatically added from ./examples/1-create-a-new-table.py -->
```py
from LucidDynamodb import DynamoDb
from LucidDynamodb.exceptions import (
    TableAlreadyExists
)
import logging
logging.basicConfig(level=logging.INFO)

table_schema = {
	"TableName": "dev_jobs",
	"KeySchema": [{
			"AttributeName": "company_name",
			"KeyType": "HASH"
		},
		{
			"AttributeName": "role_id",
			"KeyType": "RANGE"
		}
	],
	"AttributeDefinitions": [{
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
```
<!-- MARKDOWN-AUTO-DOCS:END -->

#### Get all table names
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/2-get-all-table-names.py) -->
<!-- The below code snippet is automatically added from ./examples/2-get-all-table-names.py -->
```py
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
```
<!-- MARKDOWN-AUTO-DOCS:END -->

#### Create a new item
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/3-create-a-new-item.py) -->
<!-- The below code snippet is automatically added from ./examples/3-create-a-new-item.py -->
```py
from LucidDynamodb import DynamoDb
from LucidDynamodb.exceptions import (
    UnexpectedError
)
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    try:
        db = DynamoDb()
        db.create_item(
            table_name="dev_jobs",
            item={
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
        logging.info("Item created successfully")
    except UnexpectedError as e:
        logging.error(f"Item creation failed - {e}")
        
"""
dineshsonachalam@macbook examples % python 3-create-a-new-item.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:Item created successfully
"""
```
<!-- MARKDOWN-AUTO-DOCS:END -->

#### Read an item
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/4-read-an-item.py) -->
<!-- The below code snippet is automatically added from ./examples/4-read-an-item.py -->
```py
from LucidDynamodb import DynamoDb
from LucidDynamodb.exceptions import (
    ItemNotFound
)
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    try:
        db = DynamoDb()
        item = db.read_item(
            table_name="dev_jobs",
            key={
                "company_name": "Google",
                "role_id": "111"
            }
        )
        logging.info(f"Item: {item}")
    except ItemNotFound as e:
        logging.error(f"Item doesn't exist - {e}")
        
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

#### Read items by filter
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/5-read-items-by-filter.py) -->
<!-- The below code snippet is automatically added from ./examples/5-read-items-by-filter.py -->
```py
from LucidDynamodb import DynamoDb
from LucidDynamodb.exceptions import (
    QueryFilterValidationFailed
)
import logging
from boto3.dynamodb.conditions import Key
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    try:
        db = DynamoDb()
        db.create_item(
            table_name="dev_jobs",
            item={
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
        logging.info("Item created successfully")
        items = db.read_items_by_filter(
                        table_name='dev_jobs',
                        key_condition_expression=Key("company_name").eq("Google")
        )
        logging.info(f"Items: {items}")
    except QueryFilterValidationFailed as e:
        logging.error(f"Items doesn't exist - {e}")

"""
dineshsonachalam@macbook examples % python 5-read-items-by-filter.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:Item created successfully
INFO:root:Items: [{
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

#### Update existing attribute in an item
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/6-update-existing-attribute-in-an-item.py) -->
<!-- The below code snippet is automatically added from ./examples/6-update-existing-attribute-in-an-item.py -->
```py
from LucidDynamodb import DynamoDb
from LucidDynamodb.exceptions import (
    UnexpectedError
)
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    try:
        db = DynamoDb()
        db.update_item(
            table_name="dev_jobs",
            key={
                "company_name": "Google",
                "role_id": "111"
            },
            attributes_to_update={
                'role': 'Staff Software Engineer 2'
            }
        )
        logging.info("Update is successful")
        item = db.read_item(
            table_name="dev_jobs",
            key={
                "company_name": "Google",
                "role_id": "111"
            }
        )
        logging.info(f"Item: {item}")
    except UnexpectedError as e:
        logging.error(f"Update failed - {e}")

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
	'yearly_hike_percent': Decimal('8'),
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

#### Add a new attribute in an item
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/7-add-a-new-attribute-in-an-item.py) -->
<!-- The below code snippet is automatically added from ./examples/7-add-a-new-attribute-in-an-item.py -->
```py
from LucidDynamodb import DynamoDb
from LucidDynamodb.exceptions import (
    UnexpectedError
)
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    try:
        db = DynamoDb()
        db.update_item(
            table_name="dev_jobs",
            key={
                "company_name": "Google",
                "role_id": "111"
            },
            attributes_to_update={
                'overall_review.yearly_bonus_percent': 12
            }
        )
        logging.info("Update is successful")
        item = db.read_item(
            table_name="dev_jobs",
            key={
                "company_name": "Google",
                "role_id": "111"
            }
        )
        logging.info(f"Item: {item}")
    except UnexpectedError as e:
        logging.error(f"Update failed - {e}")

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

#### Add an attribute to the list
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/8-add-an-attribute-to-the-list.py) -->
<!-- The below code snippet is automatically added from ./examples/8-add-an-attribute-to-the-list.py -->
```py
from LucidDynamodb import DynamoDb
from LucidDynamodb.exceptions import (
    UnexpectedError
)
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    try:
        db = DynamoDb()
        db.update_item(
            table_name="dev_jobs",
            key={
                "company_name": "Google",
                "role_id": "111"
            },
            attributes_to_update={
                'locations': "Detroit, Michigan"
            },
            operation="ADD_ATTRIBUTE_TO_LIST"
        )
        logging.info("Update is successful")
        item = db.read_item(
            table_name="dev_jobs",
            key={
                "company_name": "Google",
                "role_id": "111"
            }
        )
        logging.info(f"Item: {item}")
    except UnexpectedError as e:
        logging.error(f"Update failed - {e}")

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
	'yearly_hike_percent': Decimal('8'),
	'salary': '$1,50,531',
	'benefits': {
		'Health insurance',
		'Travel reimbursements',
		'Internet, Medical, Edu reimbursements'
	}
}
"""
```
<!-- MARKDOWN-AUTO-DOCS:END -->

#### Add an attribute to the string set
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/9-add-an-attribute-to-the-string-set.py) -->
<!-- The below code snippet is automatically added from ./examples/9-add-an-attribute-to-the-string-set.py -->
```py
from LucidDynamodb import DynamoDb
from LucidDynamodb.exceptions import (
    UnexpectedError
)
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    try:
        db = DynamoDb()
        db.update_item(
            table_name="dev_jobs",
            key={
                "company_name": "Google",
                "role_id": "111"
            },
            attributes_to_update={
                'benefits': "Free Food"
            },
            operation="ADD_ATTRIBUTE_TO_STRING_SET"
        )
        logging.info("Update is successful")
        item = db.read_item(
            table_name="dev_jobs",
            key={
                "company_name": "Google",
                "role_id": "111"
            }
        )
        logging.info(f"Item: {item}")
    except UnexpectedError as e:
        logging.error(f"Update failed - {e}")

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
	'yearly_hike_percent': Decimal('8'),
	'salary': '$1,50,531',
	'benefits': {
		'Travel reimbursements',
		'Free Food',
		'Health insurance',
		'Internet, Medical, Edu reimbursements'
	}
}
"""
```
<!-- MARKDOWN-AUTO-DOCS:END -->

#### Increase an existing attribute value
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/10-increase-an-existing-attribute-value.py) -->
<!-- The below code snippet is automatically added from ./examples/10-increase-an-existing-attribute-value.py -->
```py
from LucidDynamodb import DynamoDb
from LucidDynamodb.exceptions import (
    UnexpectedError
)
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    try:
        db = DynamoDb()
        db.increase_attribute_value(
            table_name='dev_jobs',
            key={
                "company_name": "Google",
                "role_id": "111"
            },
            attribute_name="yearly_hike_percent",
            increment_value=5
        )
        logging.info("Attribute value increment completed")
        item = db.read_item(
            table_name='dev_jobs',
            key={
                "company_name": "Google",
                "role_id": "111"
            }
        )
        logging.info(f"Item: {item}")
    except UnexpectedError as e:
        logging.error(f"Attribute value increment failed - {e}")

"""
dineshsonachalam@macbook examples % python 10-increase-an-existing-attribute-value.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:Attribute value increment completed
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
		'Free Food',
		'Health insurance',
		'Travel reimbursements'
	}
}
"""
```
<!-- MARKDOWN-AUTO-DOCS:END -->

#### Delete an attribute from an item
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/11-delete-an-attribute-from-an-item.py) -->
<!-- The below code snippet is automatically added from ./examples/11-delete-an-attribute-from-an-item.py -->
```py
from LucidDynamodb import DynamoDb
from LucidDynamodb.exceptions import (
    UnexpectedError
)
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    try:
        db = DynamoDb()
        db.delete_attribute(
            table_name="dev_jobs",
            key={"company_name": "Google", "role_id": "111"},
            attribute_name="yearly_hike_percent")
        logging.info("The attribute is deleted successfully")
        item = db.read_item(
            table_name="dev_jobs",
            key={
                "company_name": "Google",
                "role_id": "111"
            }
        )
        logging.info(f"Item: {item}")
    except UnexpectedError as e:
         logging.error(f"The attribute delete operation failed - {e}")

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
		'Travel reimbursements',
		'Free Food',
		'Health insurance',
		'Internet, Medical, Edu reimbursements'
	}
}
"""
```
<!-- MARKDOWN-AUTO-DOCS:END -->

#### Delete an attribute from the string set
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/12-delete-an-attribute-from-the-string-set.py) -->
<!-- The below code snippet is automatically added from ./examples/12-delete-an-attribute-from-the-string-set.py -->
```py
from LucidDynamodb import DynamoDb
from LucidDynamodb.exceptions import (
    UnexpectedError
)
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    try:
        db = DynamoDb()
        db.update_item(
            table_name="dev_jobs",
            key={
                "company_name": "Google",
                "role_id": "111"
            },
            attributes_to_update={
                'benefits': "Free Food"
            },
            operation="DELETE_ATTRIBUTE_FROM_STRING_SET"
        )
        logging.info("Update is successful")
        item = db.read_item(
            table_name="dev_jobs",
            key={
                "company_name": "Google",
                "role_id": "111"
            }
        )
        logging.info(f"Item: {item}")
    except UnexpectedError as e:
        logging.error(f"Update failed - {e}")

"""
dineshsonachalam@macbook examples % python 12-delete-an-attribute-from-the-string-set.py
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

#### Delete an item
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/13-delete-an-item.py) -->
<!-- The below code snippet is automatically added from ./examples/13-delete-an-item.py -->
```py
from LucidDynamodb import DynamoDb
from LucidDynamodb.exceptions import (
    UnexpectedError
)
from boto3.dynamodb.conditions import Key
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    try:
        db = DynamoDb()
        db.delete_item(
            table_name="dev_jobs",
            key={
                "company_name": "Google",
                "role_id": "111"
            }
        )
        logging.info("Item deleted successfully")
        items = db.read_items_by_filter(
                        table_name='dev_jobs',
                        key_condition_expression=Key("company_name").eq("Google")
        )
        logging.info(f"Items: {items}") 
    except UnexpectedError as e:
        logging.warning(f"Item delete operation failed - {e}")
        
"""
dineshsonachalam@macbook examples % python 13-delete-an-item.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:Item deleted successfully
INFO:root:Items: [{
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

#### Delete a table
<!-- MARKDOWN-AUTO-DOCS:START (CODE:src=./examples/14-delete-a-table.py) -->
<!-- The below code snippet is automatically added from ./examples/14-delete-a-table.py -->
```py
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
```
<!-- MARKDOWN-AUTO-DOCS:END -->

## Running Tests

To run tests, run the following command

```bash
pytest -s
```

## License

[MIT](https://choosealicense.com/licenses/mit/) © [dineshsonachalam](https://www.github.com/dineshsonachalam)
