import boto3, json, os
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError
import pathlib
import logging

logging.basicConfig(filename="../logs/spacex_crud.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)


class Crud:
    def __init__(self, table_name):
        self.table_name = table_name
        self.table_schema = self.table_info(table_name)
        self.db = self.table_schema.get("db")
        self.region_name = self.table_schema.get("region_name")
        self.aws_access_key_id = self.table_schema.get("aws_access_key_id")
        self.aws_secret_access_key = self.table_schema.get("aws_secret_access_key")

        self.dynamodb = boto3.resource(
            self.db,
            region_name= self.region_name,
            aws_access_key_id= self.aws_access_key_id,
            aws_secret_access_key= self.aws_secret_access_key)

        self.dynamodb_client = boto3.client(
            self.db,
            region_name= self.region_name,
            aws_access_key_id= self.aws_access_key_id,
            aws_secret_access_key= self.aws_secret_access_key)

    @staticmethod
    def table_info(table_name):
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, 'table-test-config.json')) as file:
            aws_config = json.load(file)
            db = aws_config["db"]
            region_name = aws_config.get("region_name")
            aws_access_key_id = aws_config.get("AWS_SERVER_PUBLIC_KEY")
            aws_secret_access_key = aws_config.get("AWS_SERVER_SECRET_KEY")
            key_schema = aws_config.get("table_schema").get(table_name).get("key_schema")
            attribute_definition = aws_config.get("table_schema").get(table_name).get("attribute_definition")
            provisioned_throughput = aws_config.get("table_schema").get(table_name).get("provisioned_throughput")
            global_secondary_indexes = aws_config.get("table_schema").get(table_name).get("global_secondary_indexes")


        table_schema = {
            "db": db,
            "region_name": region_name,
            "aws_access_key_id": aws_access_key_id,
            "aws_secret_access_key": aws_secret_access_key,
            "key_schema": key_schema,
            "attribute_definition": attribute_definition,
            "provisioned_throughput": provisioned_throughput,
            "global_secondary_indexes": global_secondary_indexes
        }

        return table_schema

    def table_names(self):
        """Get table_names from DynamoDb

        Returns
        -------
        list
            a list of table_names
        """
        try:
            tables = self.dynamodb_client.list_tables()['TableNames']
            if isinstance(tables, list) and len(tables) > 0:
                logger.info("table_name: Successfully got the table_names")
                return tables
            else:
                logger.warning("table_names: Failed to get table_names")
                return None
        except ClientError as e:
            logger.error("table_names: Failed to get table_names - Exception: {}".format(e))
            return None

    def create_table(self):
        """

        Returns
        -------
        DynamoDB table
        """
        try:
            tables = self.table_names()
            if self.table_name in tables:
                logger.info("{} table already exists!".format(self.table_name))
            else:
                if self.table_schema.get("global_secondary_indexes"):
                    self.dynamodb_client.create_table(
                        TableName=self.table_name,
                        KeySchema=self.table_schema.get("key_schema"),
                        AttributeDefinitions=self.table_schema.get("attribute_definition"),
                        GlobalSecondaryIndexes=self.table_schema.get("global_secondary_indexes"),
                        ProvisionedThroughput=self.table_schema.get("provisioned_throughput")
                    )
                else:
                    self.dynamodb_client.create_table(
                        TableName=self.table_name,
                        KeySchema=self.table_schema.get("key_schema"),
                        AttributeDefinitions=self.table_schema.get("attribute_definition"),
                        ProvisionedThroughput=self.table_schema.get("provisioned_throughput")
                    )

                waiter = self.dynamodb_client.get_waiter('table_exists')
                waiter.wait(TableName=self.table_name)
                logger.info("create_table: Created a new {} table!".format(self.table_name))

            table = self.dynamodb.Table(self.table_name)
            return table
        except ClientError as e:
            logger.error("create_table: Unexpected error: {}".format(e))
            return None


    def delete_table(self):
        try:
            self.dynamodb_client.delete_table(TableName=self.table_name)
            waiter = self.dynamodb_client.get_waiter('table_not_exists')
            waiter.wait(TableName=self.table_name)
            logger.info("Table deleted successfully")
        except ClientError as e:
            logger.error("Unexpected error: {}".format(e))

    def create_item(self, data):
        """Create a new item in DynamoDB table

        Parameters
        ----------
        data  : Dict
            Data that is inserted into the DynamoDB table
        """
        try:
            table = self.dynamodb.Table(self.table_name)
            response = table.put_item(Item=data)
            logger.info("create_item: Item created successfully")
            return {"is_success": True, "message": "create_item: Item created successfully"}
        except ClientError as e:
            logger.error("create_item: Item creation failed - Exception: {}".format(e))
            return {"is_success": False, "message": "create_item: Item creation failed - Exception: {}".format(e)}

    def read_item(self, table_search_key):
        """
        Parameters
        ----------
        table_search_key  : dict
            Unique key associated with an item

        Returns
        -------
        dict
            Get items data in a dictionary
        """
        try:
            table = self.dynamodb.Table(self.table_name)
            response = table.get_item(Key=table_search_key)
            if response.get('Item'):
                logger.info("read_item: Reading the item is completed")
                return {"is_success": True, "message": "read_item: Reading the item is completed" , "item_data": response.get('Item') }
            else:
                logger.warning("read_item: Failed to read the item")
                return {"is_success": False, "message": "read_item: Failed to read the item"}
        except ClientError as e:
            logger.error("read_item: Failed to read the item - Exception: {}".format(e))
            return {"is_success": False, "message": "read_item: Failed to read the item - Exception: {}".format(e)}

    def read_all_item(self, key, value, index_name):
        # Read all the item given a partition key -> It will list out table with sort key + partition key
        # Here key -> Column name
        # Here Value -> Sort Key value.
        # Reference: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.04.html
        try:
            table = self.dynamodb.Table(self.table_name)
            if index_name is not None:
                response = table.query(
                    IndexName=index_name,
                    KeyConditionExpression=Key(key).eq(value)
                )
            else:
                response = table.query(
                    KeyConditionExpression=Key(key).eq(value)
                )
            if response.get('Items'):
                logger.info("read_all: Reading all the item is completed")
                return {"is_success": True, "message": "read_all: Reading all the item is completed", "item_data": response.get('Items')}
            else:
                logger.warning("read_all: Reading all the item failed")
                return {"is_success": False, "message": "read_all: Reading all the item failed"}
        except ClientError as e:
            logger.error("read_all: Reading all the item failed - Exception: {}".format(e))
            return {"is_success": False, "message": "read_all: Reading all the item failed - Exception: {}".format(e)}

    def read_item_multiple_condition(self, key1, value1, key2, value2, index_name):
        try:
            table = self.dynamodb.Table(self.table_name)
            if index_name is not None:
                response = table.query(
                    IndexName=index_name,
                    KeyConditionExpression=Key(key1).eq(value1) & Key(key2).eq(value2)
                )
            else:
                response = table.query(
                    KeyConditionExpression=Key(key1).eq(value1) & Key(key2).eq(value2)
                )
            if response.get('Items'):
                logger.info("read_all: Reading all the item is completed")
                return {"is_success": True, "message": "read_all: Reading all the item is completed", "item_data": response.get('Items')}
            else:
                logger.warning("read_all: Reading all the item failed")
                return {"is_success": False, "message": "read_all: Reading all the item failed"}
        except ClientError as e:
            logger.error("read_all: Reading all the item failed - Exception: {}".format(e))
            return {"is_success": False, "message": "read_all: Reading all the item failed - Exception: {}".format(e)}

    def delete_item(self, table_search_key):
        """Delete an item that is associated with an table_search_key

        Parameters
        ----------
        table_search_key: dict
            Unique key associated with an item
        """
        try:
            table = self.dynamodb.Table(self.table_name)
            result = table.delete_item(
                Key=table_search_key
            )
            logger.info("delete_item: Item is deleted successfully")
            return {"is_success": True, "message": "delete_item: Item is deleted successfully"}
        except ClientError as e:
            logger.error("delete_item: Deleting an item failed")
            return {"is_success": False, "message": "delete_item: Deleting an item failed"}

    @staticmethod
    def get_update_expression(data, operation):
        """
        For Example:
        update_expression: SET #user.#credentials.#api_key = :value
        """
        try:
            expressions = ""
            expression_attibute_names = {}
            expression_attribute_values = {}
            counter = 1
            for key, value in data.items():
                expression_name = ""
                keys = key.split(".")
                expression_attribute_values[":value{}".format(counter)] = value
                for key in keys:
                    key_with_slash = "#{}".format(key)
                    expression_attibute_names[key_with_slash] = key
                    expression_name += key_with_slash + "."
                expression_name = expression_name.rstrip('.')
                if operation == "update_key":
                    expressions += "{} = :value{}, ".format(expression_name, counter)
                elif operation == "list_append":
                    expressions += "{} = list_append({},:value{}), ".format(expression_name, expression_name, counter)
                elif operation == "add_item_to_string_set" or operation == "delete_item_from_string_set":
                    expressions += "{} :value{}, ".format(expression_name, counter)
                elif operation == "delete_key_from_map":
                    expressions += "{}, ".format(expression_name)
                counter = counter + 1
            expressions = (expressions.rstrip()).rstrip(",")
            if operation == "update_key" or operation == "list_append":
                update_expression = "SET {}".format(expressions)
            elif operation == "add_item_to_string_set":
                update_expression = "ADD {}".format(expressions)
            elif operation == "delete_item_from_string_set":
                update_expression = "DELETE {}".format(expressions)
            elif operation == "delete_key_from_map":
                update_expression = "REMOVE {}".format(expressions)
            return update_expression, expression_attibute_names, expression_attribute_values
        except Exception as e:
            logger.error("get_update_expression: Update expression generation failed - Exception: {}".format(e))
            return None,None,None

    def update_item(self,  table_search_key, operation, data):
        """
        Parameters
        ----------
        table_search_key: dict
        operation: str
        data: dict
        """

        try:
            table = self.dynamodb.Table(self.table_name)
            update_expression, expression_attibute_names, expression_attribute_values = \
                self.get_update_expression(data, operation)

            if update_expression is not None and expression_attibute_names is not None and expression_attribute_values is not None:
                if operation == "delete_key_from_map":
                    result = table.update_item(
                                Key=table_search_key,
                                UpdateExpression=update_expression,
                                ExpressionAttributeNames=expression_attibute_names,
                                ReturnValues="ALL_NEW"
                    )
                else:
                    result = table.update_item(
                                Key=table_search_key,
                                UpdateExpression=update_expression,
                                ExpressionAttributeNames=expression_attibute_names,
                                ExpressionAttributeValues=expression_attribute_values,
                                ReturnValues="ALL_NEW"
                    )
                if result is not None:
                    logger.info("update_item: Updating an item is completed")
                    return {"is_success": True, "message": "update_item: Updating an item is completed"}
                else:
                    logger.warning("update_item: Failed to update an item")
                    return {"is_success": False, "message": "update_item: Failed to update an item"}
            else:
                logger.warning("update_item: Failed to update an item - Since update expression is None")
                return {"is_success": False, "message": "update_item: Failed to update an item - Since update expression is None"}
        except ClientError as e:
            logger.error("update_item: Failed to update an item - Exception: {}".format(e))
            return {"is_success": False, "message": "update_item: Failed to update an item - Exception: {}".format(e)}
