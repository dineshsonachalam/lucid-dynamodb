from LucidDynamodb import DynamoDb
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    db = DynamoDb()
    
    item_update_status = db.update_item(
        table_name="dev_jobs", 
        key={
            "company_name": "Google",
            "role_id": "111"
        },
        attributes_to_update={
            'locations': "Detroit, Michigan"
        },
        operation="ADD_ATTRIBUTE_TO_LIST"
    )
    try:
        logging.info("Update is successful")
    except Exception as e:
        logging.warning("Update failed - {}".format(e))

    item = db.read_item(
        table_name="dev_jobs", 
        key={
            "company_name": "Google",
            "role_id": "111"
        })
    try:
        logging.info("Item: {}".format(item))
    except Exception as e:
        logging.warning("Item doesn't exist - {}".format(e))
"""
dineshsonachalam@macbook examples % python 8-add-an-attribute-to-the-list.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:Update is successful
INFO:root:Item: {
    "locations": [
        "Mountain View, California",
        "Austin, Texas",
        "Chicago, IL",
        "Detroit, Michigan"
    ],
    "role_id": "111",
    "overall_review": {
        "compensation_and_benefits": "3.9/5",
        "overall_rating": "4/5",
        "yearly_bonus_percent": "12"
    },
    "company_name": "Google",
    "role": "Staff Software Engineer 2",
    "yearly_hike_percent": "13",
    "salary": "$1,50,531",
    "benefits": [
        "Internet, Medical, Edu reimbursements",
        "Travel reimbursements",
        "Health insurance"
    ]
}
"""