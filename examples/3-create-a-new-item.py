from LucidDynamodb.Operations import DynamoDb
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