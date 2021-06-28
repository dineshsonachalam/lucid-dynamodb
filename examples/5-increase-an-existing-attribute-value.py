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

"""Output

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
"""