from LucidDynamodb import DynamoDb
from LucidDynamodb.exceptions import (
    UnexpectedError
)
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    try:
        db = DynamoDb()
        db.update_item(
            table_name="dev_jobs",
            key={
                "company_name": "Google",
                "role_id": "111"
            },
            attributes_to_update={
                'overall_review.yearly_bonus_percent': 12
            }
        )
        logging.info("Update is successful")
        item = db.read_item(
            table_name="dev_jobs",
            key={
                "company_name": "Google",
                "role_id": "111"
            }
        )
        logging.info(f"Item: {item}")
    except UnexpectedError as e:
        logging.error(f"Update failed - {e}")

"""
dineshsonachalam@macbook examples % python 7-add-a-new-attribute-in-an-item.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:Update is successful
INFO:root:Item: {
	'locations': ['Mountain View, California', 'Austin, Texas', 'Chicago, IL'],
	'role_id': '111',
	'overall_review': {
		'compensation_and_benefits': '3.9/5',
		'overall_rating': '4/5',
		'yearly_bonus_percent': Decimal('12')
	},
	'company_name': 'Google',
	'role': 'Staff Software Engineer 2',
	'yearly_hike_percent': Decimal('8'),
	'salary': '$1,50,531',
	'benefits': {
		'Travel reimbursements',
		'Internet, Medical, Edu reimbursements',
		'Health insurance'
	}
}
"""