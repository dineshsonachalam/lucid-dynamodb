import boto3
from botocore.exceptions import ClientError
from LucidDynamodb.utils import generate_expression_attribute_values
from LucidDynamodb.exceptions import (
    TableAlreadyExists,
    TableNotFound,
    ItemNotFound,
    QueryFilterValidationFailed,
    UnexpectedError
)

class DynamoDb:
    def __init__(self, region_name=None, aws_access_key_id=None, aws_secret_access_key=None):
        self.region_name = region_name
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        if(self.region_name!=None or self.aws_access_key_id!=None or self.aws_secret_access_key!=None):
            self.db = boto3.resource(
                "dynamodb",
                region_name = region_name,
                aws_access_key_id = aws_access_key_id,
                aws_secret_access_key = aws_secret_access_key,
            )
        else:
            self.db = boto3.resource("dynamodb")

    def create_table(self, table_name, key_schema, attribute_definitions, provisioned_throughput, global_secondary_indexes=None):
        """Create a new table

        Args:
            table_name (str): Table name
            key_schema (list): A key schema specifies the attributes that make up the Partition key,  Sort Key(Optional)) of a table.
            attribute_definitions (list): An array of attributes that describe the key schema for the table.
            global_secondary_indexes (list, optional): An index with a partition key and a sort key that can be different from those on the base table.
            provisioned_throughput (dict): Provisioned throughput settings for this specified table.

        Returns:
            bool: Table creation is successful or failed
        """
        try:
            if(len(global_secondary_indexes)>0):
                table = self.db.create_table(
                    TableName=table_name,
                    KeySchema=key_schema,
                    AttributeDefinitions=attribute_definitions,
                    GlobalSecondaryIndexes=global_secondary_indexes,
                    ProvisionedThroughput=provisioned_throughput
                )
            else:
                table = self.db.create_table(
                    TableName=table_name,
                    KeySchema=key_schema,
                    AttributeDefinitions=attribute_definitions,
                    ProvisionedThroughput=provisioned_throughput
                )
                # Wait until the table exists.
                table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
            return True
        except ClientError as e:
            if e.response['Error']['Code'] == 'ResourceInUseException':
                raise TableAlreadyExists(table_name)
            else:
                raise UnexpectedError(e)

    def delete_table(self, table_name):
        """Delete a table

        Args:
            table_name (str): Table name

        Returns:
            bool: Table deletion is successful or failed
        """
        try:
            table = self.db.Table(table_name)
            table.delete()
            table.wait_until_not_exists()
            return True
        except ClientError as e:
            if e.response['Error']['Code'] == 'ResourceNotFoundException':
                raise TableNotFound(table_name)
            else:
                raise UnexpectedError(e)

    def read_all_table_names(self):
        """Get all table names

        Returns:
            list: List of table names
        """
        try:
            if(self.region_name!=None or self.aws_access_key_id!=None or self.aws_secret_access_key!=None):
                db_client = boto3.client(
                    "dynamodb",
                    region_name = self.region_name,
                    aws_access_key_id = self.aws_access_key_id,
                    aws_secret_access_key = self.aws_secret_access_key,
                )
            else:
                db_client = boto3.client(
                    "dynamodb"
                )
            table_names = db_client.list_tables()['TableNames']
            return table_names
        except ClientError as e:
            raise UnexpectedError(e)

    def create_item(self, table_name ,item):
        """Create a new Item

        Args:
            table_name (str): Table name
            item (dict): Item with Partition key,  Sort Key(Optional)

        Returns:
            bool: Item creation is successful or failed
        """
        try:
            table = self.db.Table(table_name)
            table.put_item(Item=item)
            return True
        except ClientError as e:
            raise UnexpectedError(e)

    def delete_item(self, table_name, key, condition_expression = "", expression_attribute_values=None):
        """Delete an Item

        Args:
            table_name (str): Table name
            key (dict): Partition key,  Sort Key(Optional)
            condition_expression (str, optional): condition_expression to prevent the item from being deleted if the condition is not met.
            expression_attribute_values (dict, optional): Expression attribute values.

        Returns:
            bool: Item deletion is successful or failed
        """
        try:
            table = self.db.Table(table_name)
            if(len(condition_expression)>0 and len(expression_attribute_values)>0):
                table.delete_item(
                    Key=key,
                    ConditionExpression=condition_expression,
                    ExpressionAttributeValues=expression_attribute_values
                )
            else:
                table.delete_item(
                    Key=key
                )
            return True
        except ClientError as e:
            raise UnexpectedError(e)

    def read_item(self, table_name, key):
        """Read an Item

        Args:
            table_name (str): Table name
            key (dict): Partition key,  Sort Key(Optional)

        Returns:
            dict: Item
        """
        try:
            table = self.db.Table(table_name)
            response = table.get_item(Key=key)
            item = response.get('Item')
            if item is not None:
                return item
            else:
                return ItemNotFound(table_name, key)
        except ClientError as e:
            raise UnexpectedError(e)

    def read_items_by_filter(self, table_name, key_condition_expression, global_secondary_index_name=None):
        """Read items by filter
           The Query operation will return all of the items from the table or index with that partition key value.

        Args:
            table_name (str): Table name
            key_condition_expression (boto3.dynamodb.conditions.Equals): Use the KeyConditionExpression parameter to
                provide a specific value for the partition key. You can optionally narrow the scope of the Query
                operation by specifying a sort key value and a comparison operator in KeyConditionExpression.
            global_secondary_index_name (str, optional): Name of the GlobalSecondaryIndex. Defaults to None.

        Returns:
            list: Table items
        """
        try:
            table = self.db.Table(table_name)
            if global_secondary_index_name != None:
                response = table.query(
                    IndexName=global_secondary_index_name,
                    KeyConditionExpression=key_condition_expression
                )
            else:
                response = table.query(
                    KeyConditionExpression=key_condition_expression
                )
            return response.get('Items')
        except ClientError as e:
            if e.response['Error']['Code'] == 'ValidationException':
                raise QueryFilterValidationFailed(table_name)
            else:
                raise UnexpectedError(e)

    def update_item(self, table_name, key,
                    attributes_to_update, operation="UPDATE_EXISTING_ATTRIBUTE_OR_ADD_NEW_ATTRIBUTE"):
        """Update an item
        Args:
            table_name (str): Table name
            key (dict): Partition key,  Sort Key(Optional)
            attributes_to_update (dict): Attributes data with K:V
            operation (str, optional): Update operation category
                Defaults to UPDATE_EXISTING_ATTRIBUTE_OR_ADD_NEW_ATTRIBUTE.
        
        Returns:
            bool: Attribute update is successful or failed
        """
        try:
            table = self.db.Table(table_name)
            update_expression, \
            expression_attribute_names, \
            expression_attribute_values = generate_expression_attribute_values(attributes_to_update, operation)
            if(len(update_expression)>0 and len(expression_attribute_names)>0 \
               and len(expression_attribute_values)>0):
                table.update_item(
                                Key=key,
                                UpdateExpression=update_expression,
                                ExpressionAttributeNames=expression_attribute_names,
                                ExpressionAttributeValues=expression_attribute_values,
                                ReturnValues="ALL_NEW"
                )
                return True
            else:
                return False
        except ClientError as e:
            raise UnexpectedError(e)

    def increase_attribute_value(self, table_name, key, attribute_name, increment_value):
        """Increase an existing attribute value

        Args:
            table_name (str): Table name
            key (dict): Partition key,  Sort Key(Optional)
            attribute_name (str): Name of the attribute
            increment_value (int): Increment value for an attribute

        Returns:
            bool: Attribute value is incremented or not
        """
        try:
            table = self.db.Table(table_name)
            attributes_to_update = {
                attribute_name: increment_value
            }
            operation = "INCREASE_ATTRIBUTE_VALUE"
            update_expression, expression_attribute_names, \
            expression_attribute_values = generate_expression_attribute_values(attributes_to_update, operation)
            if(len(update_expression)>0 and len(expression_attribute_names)>0 \
               and len(expression_attribute_values)>0):
                table.update_item(
                                Key=key,
                                UpdateExpression=update_expression,
                                ExpressionAttributeNames=expression_attribute_names,
                                ExpressionAttributeValues=expression_attribute_values,
                                ReturnValues="ALL_NEW"
                )
                return True
            else:
                return False
        except ClientError as e:
            raise UnexpectedError(e)

    def delete_attribute(self, table_name, key, attribute_name):
        """Delete an attribute from an item

        Args:
            table_name (str): Table name
            key (dict): Partition key,  Sort Key(Optional)
            attribute_name (str): Name of the Attribute

        Returns:
            bool: Attribute deletion is successful or failed
        """
        try:
            table = self.db.Table(table_name)
            table.update_item(
                                Key=key,
                                UpdateExpression=f"REMOVE {attribute_name}",
                                ReturnValues="ALL_NEW"
            )
            return True
        except ClientError as e:
            raise UnexpectedError(e)
