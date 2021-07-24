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