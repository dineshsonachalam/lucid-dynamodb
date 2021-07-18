from LucidDynamodb import DynamoDb
import logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    db = DynamoDb()
    item = db.read_item(
        table_name="dev_jobs", 
        key={
            "company_name": "Google",
            "role_id": "111"
        }
    )
    try:
        logging.info("Item: {}".format(item))
    except Exception as e:
        logging.warning("Item doesn't exist - {}".format(e))
"""
dineshsonachalam@macbook examples % python 4-read-an-item.py
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:Item: {
    "locations": [
        "Mountain View, California",
        "Austin, Texas",
        "Chicago, IL"
    ],
    "role_id": "111",
    "overall_review": {
        "compensation_and_benefits": "3.9/5",
        "overall_rating": "4/5"
    },
    "company_name": "Google",
    "role": "Software Engineer 1",
    "yearly_hike_percent": "8",
    "salary": "$1,50,531",
    "benefits": [
        "Travel reimbursements",
        "Internet, Medical, Edu reimbursements",
        "Health insurance"
    ]
}
"""