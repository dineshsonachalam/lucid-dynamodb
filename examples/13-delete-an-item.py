from LucidDynamodb import DynamoDb
from LucidDynamodb.exceptions import (
    UnexpectedError
)
from boto3.dynamodb.conditions import Key
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    try:
        db = DynamoDb()
        db.delete_item(
            table_name="dev_jobs",
            key={
                "company_name": "Google",
                "role_id": "111"
            }
        )
        logging.info("Item deleted successfully")
        items = db.read_items_by_filter(
                        table_name='dev_jobs',
                        key_condition_expression=Key("company_name").eq("Google")
        )
        logging.info(f"Items: {items}") 
    except UnexpectedError as e:
        logging.warning(f"Item delete operation failed - {e}")
        
"""
dineshsonachalam@macbook examples % python 13-delete-an-item.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:Item deleted successfully
INFO:root:Items: [{
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