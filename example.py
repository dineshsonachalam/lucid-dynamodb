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

    # item_creation_status = db.create_item(
    #     TableName="dev_jobs", 
    #     Item={
    #         "company_name": "Google",
    #         "role_id": str(uuid.uuid4()),
    #         "role": "Software Architect",
    #         "salary": "$4,80,000",
    #         "locations": ["Mountain View, California"],
    #         "yearly_hike_percent": 13,
    #         "benefits": set(["Internet reimbursements"]),
    #         "overall_review":{
    #             "overall_rating" : "3/5",
    #             "compensation_and_benefits": "4.2/5"
    #         }
    #     }
    # )
    # if(item_creation_status == True):
    #     logging.info("Item created successfully")
    # else:
    #     logging.warning("Item creation failed")
        
    result = db.read_items_by_filter(
                    TableName='dev_jobs', 
                    KeyConditionExpression=Key("company_name").eq("Google") 
    )
    print(result)
    
    # if(len(items)>0):
    #     logging.info("Items: {}".format(items))
    # else:
    #     logging.warning("Items doesn't exist")
        

