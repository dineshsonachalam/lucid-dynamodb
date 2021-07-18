from LucidDynamodb import DynamoDb
import os
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
db = DynamoDb(region_name="us-east-1",
              aws_access_key_id=AWS_ACCESS_KEY_ID,
              aws_secret_access_key=AWS_SECRET_ACCESS_KEY)