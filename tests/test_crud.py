from LucidDynamodb import DynamoDb
import os
import logging
import uuid
from boto3.dynamodb.conditions import Key
logging.basicConfig(level=logging.INFO)

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

ITEM1_PARTITION_KEY = str(uuid.uuid4())

table_schema = {
	"TableName": "dev_jobs_test",
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

def test_create_new_table():
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
    assert table_creation_status == True

def test_get_all_table_name():
    db = DynamoDb(region_name="us-east-1", 
                aws_access_key_id=AWS_ACCESS_KEY_ID, 
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    table_names = db.read_all_table_names()
    assert len(table_names)>0

def test_create_new_item():
    db = DynamoDb(region_name="us-east-1", 
                aws_access_key_id=AWS_ACCESS_KEY_ID, 
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    item_creation_status = db.create_item(
        TableName=table_schema.get("TableName"), 
        Item={
            "company_name": "Google",
            "role_id": ITEM1_PARTITION_KEY,
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
    assert item_creation_status == True

def test_read_item():
    db = DynamoDb(region_name="us-east-1", 
                aws_access_key_id=AWS_ACCESS_KEY_ID, 
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    item = db.read_item(
        TableName=table_schema.get("TableName"), 
        Key={
            "company_name": "Google",
            "role_id": ITEM1_PARTITION_KEY
        }
    )
    assert item != None

def test_increase_attribute_value():
    db = DynamoDb(region_name="us-east-1", 
                aws_access_key_id=AWS_ACCESS_KEY_ID, 
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    increase_attribute_status = db.increase_attribute_value(
        TableName=table_schema.get("TableName"),
        Key={
            "company_name": "Google",
            "role_id": ITEM1_PARTITION_KEY
        },
        AttributeName="yearly_hike_percent",
        IncrementValue=5
    )
    assert increase_attribute_status==True

def test_update_existing_attribute():
    db = DynamoDb(region_name="us-east-1", 
                aws_access_key_id=AWS_ACCESS_KEY_ID, 
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    item_update_status = db.update_item(
        TableName=table_schema.get("TableName"), 
        Key={
            "company_name": "Google",
            "role_id": ITEM1_PARTITION_KEY
        },
        AttributesToUpdate={
            'role': 'Staff Software Engineer 2'
        }
    )
    assert item_update_status == True  

def test_add_new_attribute():
    db = DynamoDb(region_name="us-east-1", 
                aws_access_key_id=AWS_ACCESS_KEY_ID, 
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    item_update_status = db.update_item(
        TableName=table_schema.get("TableName"), 
        Key={
            "company_name": "Google",
            "role_id": ITEM1_PARTITION_KEY
        },
        AttributesToUpdate={
            'overall_review.yearly_bonus_percent': 12
        }
    )
    assert item_update_status == True
    
def test_add_attribute_to_list():  
    db = DynamoDb(region_name="us-east-1", 
                aws_access_key_id=AWS_ACCESS_KEY_ID, 
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    item_update_status = db.update_item(
        TableName=table_schema.get("TableName"), 
        Key={
            "company_name": "Google",
            "role_id": ITEM1_PARTITION_KEY
        },
        AttributesToUpdate={
            'locations': "Detroit, Michigan"
        },
        Operation="ADD_ATTRIBUTE_TO_LIST"
    )
    assert item_update_status == True
    
def test_add_attributes_to_string_set():
    db = DynamoDb(region_name="us-east-1", 
                aws_access_key_id=AWS_ACCESS_KEY_ID, 
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    item_update_status = db.update_item(
        TableName=table_schema.get("TableName"), 
        Key={
            "company_name": "Google",
            "role_id": ITEM1_PARTITION_KEY
        },
        AttributesToUpdate={
            'benefits': "Free Food"
        },
        Operation="ADD_ATTRIBUTE_TO_STRING_SET"
    )
    assert item_update_status == True
    
def test_delete_attribute_from_string_set():
    db = DynamoDb(region_name="us-east-1", 
                aws_access_key_id=AWS_ACCESS_KEY_ID, 
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    item_update_status = db.update_item(
        TableName=table_schema.get("TableName"), 
        Key={
            "company_name": "Google",
            "role_id": ITEM1_PARTITION_KEY
        },
        AttributesToUpdate={
            'benefits': "Free Food"
        },
        Operation="DELETE_ATTRIBUTE_FROM_STRING_SET"
    )
    assert item_update_status == True
    
def test_delete_attribute_from_item():
    db = DynamoDb(region_name="us-east-1", 
                aws_access_key_id=AWS_ACCESS_KEY_ID, 
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    attribute_delete_status = db.delete_attribute(
        TableName=table_schema.get("TableName"), 
        Key={
              "company_name": "Google",
              "role_id": ITEM1_PARTITION_KEY
        }, 
        AttributeName="yearly_hike_percent")
    assert attribute_delete_status == True
    
def test_read_items_by_filter():
    db = DynamoDb(region_name="us-east-1", 
                aws_access_key_id=AWS_ACCESS_KEY_ID, 
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    item_creation_status = db.create_item(
        TableName=table_schema.get("TableName"), 
        Item={
            "company_name": "Google",
            "role_id": str(uuid.uuid4()),
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
    assert item_creation_status == True
    items = db.read_items_by_filter(
                    TableName=table_schema.get("TableName"), 
                    KeyConditionExpression=Key("company_name").eq("Google") 
    )
    assert len(items)>0
    
def test_delete_table():
    db = DynamoDb(region_name="us-east-1", 
                aws_access_key_id=AWS_ACCESS_KEY_ID, 
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    delete_table_status = db.delete_table(TableName=table_schema.get("TableName"))
    assert delete_table_status == True