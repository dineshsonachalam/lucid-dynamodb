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

    # # # 1. Create a new table
    # table_creation_status = db.create_table(
    #                                 TableName=table_schema.get("TableName"),
    #                                 KeySchema=table_schema.get("KeySchema"),
    #                                 AttributeDefinitions=table_schema.get("AttributeDefinitions"),
    #                                 GlobalSecondaryIndexes=table_schema.get("GlobalSecondaryIndexes"),
    #                                 ProvisionedThroughput=table_schema.get("ProvisionedThroughput")
    # )
    # if(table_creation_status == True):
    #     logging.info("{} table created successfully".format(table_schema.get("TableName")))
    # else:
    #     logging.error("{} table creation failed".format(table_schema.get("TableName")))
        
    # # # Output: INFO:root:dev_jobs table created successfully
    # # # Image: https://i.imgur.com/lBrqUCb.png (Dynamodb table console)    

        
    # # # 2. Get all table names
    # table_names = db.read_all_table_names()
    # logging.info("Table names: {}".format(table_names))
    
    # # # Output: INFO:root:Table names: ['dev_jobs', 'user']
    # # # Image: https://i.imgur.com/q3GG9Ah.png (Dynamodb Tables)  
    
    # # 3. Create a new Item
    # item_creation_status = db.create_item(
    #     TableName=table_schema.get("TableName"), 
    #     Item={
    #         "company_name": "Google",
    #         "role_id": str(uuid.uuid4()),
    #         "role": "Software Engineer 1",
    #         "salary": "$1,50,531",
    #         "locations": ["Mountain View, California", "Austin, Texas", "Chicago, IL"],
    #         "yearly_hike_percent": 8,
    #         "benefits": set(["Internet, Medical, Edu reimbursements", 
    #                          "Health insurance",
    #                          "Travel reimbursements"
    #                          ]),
    #         "overall_review":{
    #             "overall_rating" : "4/5",
    #             "compensation_and_benefits": "3.9/5"
    #         }
    #     }
    # )
    # if(item_creation_status == True):
    #     logging.info("Item created successfully")
    # else:
    #     logging.warning("Item creation failed")

    # # Output: INFO:root:Item created successfully
    # # Image: https://i.imgur.com/ABh9IXt.png
    
    # 4. Read an item
    item = db.read_item(
        TableName=table_schema.get("TableName"), 
        Key={
            "company_name": "Google",
            "role_id": "716e3655-e178-435e-a68e-5dda64c3ec6d"
        })
    if(item != None):
        logging.info("Item: {}".format(item))
    else:
        logging.warning("Item doesn't exist")
    # Output: INFO:root:Item: {'locations': ['Mountain View, California', 'Austin, Texas', 'Chicago, IL'], 'role_id': 'f18685a0-a425-4519-b808-b02899c8bcfd', 'overall_review': {'compensation_and_benefits': '3.9/5', 'overall_rating': '4/5'}, 'company_name': 'Google', 'role': 'Software Engineer 1', 'yearly_hike_percent': '8%', 'salary': '$1,50,531', 'benefits': {'Travel reimbursements', 'Health insurance', 'Internet, Medical, Edu reimbursements'}}

    # 5. Increase an existing attribute value
    print(db.increase_attribute_value(
        TableName='dev_jobs',
        Key={
            "company_name": "Google",
            "role_id": "716e3655-e178-435e-a68e-5dda64c3ec6d"
        },
        AttributeName="yearly_hike_percent",
        IncrementValue=5
    ))
        
    # increase_attribute_status = db.increase_attribute_value(
    #     TableName='dev_jobs',
    #     Key={
    #         "company_name": "Google",
    #         "role_id": "716e3655-e178-435e-a68e-5dda64c3ec6d"
    #     },
    #     AttributeName="yearly_hike_percent",
    #     IncrementValue=5
    # )
    
    # if(increase_attribute_status==True):
    #     logging.info("Attribute value increment completed")
    # else:
    #     logging.warning("Attribute value increment failed")
    

    item = db.read_item(
        TableName=table_schema.get("TableName"), 
        Key={
            "company_name": "Google",
            "role_id": "716e3655-e178-435e-a68e-5dda64c3ec6d"
        })
    if(item != None):
        logging.info("Item: {}".format(item))
    else:
        logging.warning("Item doesn't exist")    
    
    # print(db.increase_attribute_value(
    #     TableName='Test_1',
    #     Key={
    #             "user_id": 0
    #     },
    #     AttributeName="salary",
    #     IncrementValue=5
    # ))

       
    # # X. Read items by filter:
    # items = db.read_items_by_filter(
    #     TableName=table_schema.get("TableName"), 
    #     KeyConditionExpression=Key("company_name").eq("Google"))
    # print(items)
        
#     # 4. Delete an Item
#     item_deletion_status = db.delete_item(
#         TableName=table_schema.get("TableName"), 
#         Key={
#         "user_id": "101"
#         }
#     )
#     if(item_deletion_status == True):
#         logging.info("Item deleted successfully")
#     else:
#         logging.warning("Item deletion failed")
    

#     # 5. Delete a table
#     table_deletion_status = db.delete_table(TableName=table_schema.get("TableName"))
#     if(table_deletion_status == True):
#         logging.info("Table deleted successfully")
#     else:
#         logging.warning("Table deletion failed")
        
# # dineshsonachalam@macbook lucid-dynamodb % python3 examples.py
# # INFO:root:Test_01 table created successfully
# # INFO:root:Table names: ['PrivateNote-tgcb6kzk2zfk5dmf6h7o6l5pcu-dev', 'Task-tgcb6kzk2zfk5dmf6h7o6l5pcu-dev', 'Test_01', 'co-ssl', 'mozhi', 'sslcorps_kms', 'sslcorps_user', 'test_user', 'test_user2', 'testtable10', 'testtable11', 'testtable13', 'testtable4', 'testtable5', 'testtable8', 'testtable9', 'tirumanam']
# # INFO:root:Item created successfully
# # INFO:root:Item deleted successfully
# # INFO:root:Table deleted successfully