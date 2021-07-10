from LucidDynamodb.Operations import DynamoDb
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