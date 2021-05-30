from LucidDynamodb.operations import DynamoDb
import os
import logging
import uuid
from boto3.dynamodb.conditions import Key

logging.basicConfig(level=logging.INFO)
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

if __name__ == "__main__":
    pass