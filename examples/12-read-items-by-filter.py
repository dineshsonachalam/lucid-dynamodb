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
    try:
        logging.info("Item created successfully")
    except Exception as e:
        logging.warning("Item creation failed - {}".format(e))
    
    items = db.read_items_by_filter(
                    TableName='dev_jobs', 
                    KeyConditionExpression=Key("company_name").eq("Google") 
    )

    try:
        logging.info("Items: {}".format(items))
    except Exception as e:
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