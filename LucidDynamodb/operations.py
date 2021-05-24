import boto3

class DynamoDb:
    def __init__(self, region_name, aws_access_key_id, aws_secret_access_key):
        self.db_client = boto3.client(
            "dynamodb",
            region_name = region_name,
            aws_access_key_id = aws_access_key_id,
            aws_secret_access_key = aws_secret_access_key,
        )
        
    def create_table(self, TableName, KeySchema, AttributeDefinitions, GlobalSecondaryIndexes, ProvisionedThroughput):
        try:
            if(len(GlobalSecondaryIndexes)>0):
                self.db_client.create_table(
                    TableName=TableName,
                    KeySchema=KeySchema,
                    AttributeDefinitions=AttributeDefinitions,
                    GlobalSecondaryIndexes=GlobalSecondaryIndexes,
                    ProvisionedThroughput=ProvisionedThroughput
                )
            else:
                self.db_client.create_table(
                    TableName=TableName,
                    KeySchema=KeySchema,
                    AttributeDefinitions=AttributeDefinitions,
                    ProvisionedThroughput=ProvisionedThroughput
                )
            waiter = self.db_client.get_waiter('table_exists')
            waiter.wait(TableName=TableName)
            return True
        except self.db_client.exceptions.ResourceInUseException:
            return False

    def delete_table(self, TableName):
        try:
            self.db_client.delete_table(TableName=TableName)
            waiter = self.db_client.get_waiter('table_not_exists')
            waiter.wait(TableName=TableName)
            return True
        except Exception as e:
            return False
                
    def read_all_table_names(self):
        pass
    def create_item(self):
        pass
    def read_item(self):
        pass
    def read_all_item(self):
        pass
    def read_items_by_filter(self):
        pass
    def update_item(self):
        pass
    def delete_item(self):
        pass