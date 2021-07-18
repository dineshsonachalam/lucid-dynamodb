from LucidDynamodb import DynamoDb
import os
import uuid
from boto3.dynamodb.conditions import Key

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
db = DynamoDb(region_name="us-east-1",
              aws_access_key_id=AWS_ACCESS_KEY_ID,
              aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

def test_create_new_table():
    table_creation_status = db.create_table(
                                    table_name=table_schema.get("TableName"),
                                    key_schema=table_schema.get("KeySchema"),
                                    attribute_definitions=table_schema.get("AttributeDefinitions"),
                                    global_secondary_indexes=table_schema.get("GlobalSecondaryIndexes"),
                                    provisioned_throughput=table_schema.get("ProvisionedThroughput")
    )
    assert table_creation_status == True

def test_get_all_table_name():
    table_names = db.read_all_table_names()
    assert len(table_names)>0

def test_create_new_item():
    item_creation_status = db.create_item(
        table_name=table_schema.get("TableName"),
        item={
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
    item = db.read_item(
        table_name=table_schema.get("TableName"),
        key={
            "company_name": "Google",
            "role_id": ITEM1_PARTITION_KEY
        }
    )
    assert item != None

def test_increase_attribute_value():
    increase_attribute_status = db.increase_attribute_value(
        table_name=table_schema.get("TableName"),
        key={
            "company_name": "Google",
            "role_id": ITEM1_PARTITION_KEY
        },
        attribute_name="yearly_hike_percent",
        increment_value=5
    )
    assert increase_attribute_status==True

def test_update_existing_attribute():
    item_update_status = db.update_item(
        table_name=table_schema.get("TableName"),
        key={
            "company_name": "Google",
            "role_id": ITEM1_PARTITION_KEY
        },
        attributes_to_update={
            'role': 'Staff Software Engineer 2'
        }
    )
    assert item_update_status == True

def test_add_new_attribute():
    item_update_status = db.update_item(
        table_name=table_schema.get("TableName"),
        key={
            "company_name": "Google",
            "role_id": ITEM1_PARTITION_KEY
        },
        attributes_to_update={
            'overall_review.yearly_bonus_percent': 12
        }
    )
    assert item_update_status == True

def test_add_attribute_to_list():
    item_update_status = db.update_item(
        table_name=table_schema.get("TableName"),
        key={
            "company_name": "Google",
            "role_id": ITEM1_PARTITION_KEY
        },
        attributes_to_update={
            'locations': "Detroit, Michigan"
        },
        operation="ADD_ATTRIBUTE_TO_LIST"
    )
    assert item_update_status == True

def test_add_attributes_to_string_set():
    item_update_status = db.update_item(
        table_name=table_schema.get("TableName"),
        key={
            "company_name": "Google",
            "role_id": ITEM1_PARTITION_KEY
        },
        attributes_to_update={
            'benefits': "Free Food"
        },
        operation="ADD_ATTRIBUTE_TO_STRING_SET"
    )
    assert item_update_status == True

def test_delete_attribute_from_string_set():
    item_update_status = db.update_item(
        table_name=table_schema.get("TableName"),
        key={
            "company_name": "Google",
            "role_id": ITEM1_PARTITION_KEY
        },
        attributes_to_update={
            'benefits': "Free Food"
        },
        operation="DELETE_ATTRIBUTE_FROM_STRING_SET"
    )
    assert item_update_status == True

def test_delete_attribute_from_item():
    attribute_delete_status = db.delete_attribute(
        table_name=table_schema.get("TableName"),
        key={
              "company_name": "Google",
              "role_id": ITEM1_PARTITION_KEY
        },
        attribute_name="yearly_hike_percent")
    assert attribute_delete_status == True

def test_read_items_by_filter():
    item_creation_status = db.create_item(
        table_name=table_schema.get("TableName"),
        item={
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
                    table_name=table_schema.get("TableName"),
                    key_condition_expression=Key("company_name").eq("Google")
    )
    assert len(items)>0

def test_delete_table():
    delete_table_status = db.delete_table(table_name=table_schema.get("TableName"))
    assert delete_table_status == True