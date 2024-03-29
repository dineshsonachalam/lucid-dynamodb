from LucidDynamodb import DynamoDb
from LucidDynamodb.exceptions import (
    UnexpectedError
)
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    try:
        db = DynamoDb()
        db.delete_attribute(
            table_name="dev_jobs",
            key={"company_name": "Google", "role_id": "111"},
            attribute_name="yearly_hike_percent")
        logging.info("The attribute is deleted successfully")
        item = db.read_item(
            table_name="dev_jobs",
            key={
                "company_name": "Google",
                "role_id": "111"
            }
        )
        logging.info(f"Item: {item}")
    except UnexpectedError as e:
         logging.error(f"The attribute delete operation failed - {e}")

"""
dineshsonachalam@macbook examples % python 11-delete-an-attribute-from-an-item.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:The attribute is deleted successfully
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
	'salary': '$1,50,531',
	'benefits': {
		'Travel reimbursements',
		'Free Food',
		'Health insurance',
		'Internet, Medical, Edu reimbursements'
	}
}
"""