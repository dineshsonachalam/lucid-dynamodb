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