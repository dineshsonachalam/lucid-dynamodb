from LucidDynamodb.Operations import DynamoDb
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    db = DynamoDb()
    item_update_status = db.update_item(
        TableName="dev_jobs", 
        Key={
            "company_name": "Google",
            "role_id": "111"
        },
        AttributesToUpdate={
            'overall_review.yearly_bonus_percent': 12
        }
    )
    if(item_update_status == True):
        logging.info("Update is successful")
    else:
        logging.warning("Update failed")

    item = db.read_item(
        TableName="dev_jobs", 
        Key={
            "company_name": "Google",
            "role_id": "111"
        })
    if(item != None):
        logging.info("Item: {}".format(item))
    else:
        logging.warning("Item doesn't exist")
        
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
	'yearly_hike_percent': Decimal('13'),
	'salary': '$1,50,531',
	'benefits': {
		'Health insurance',
		'Internet, Medical, Edu reimbursements',
		'Travel reimbursements'
	}
}
"""