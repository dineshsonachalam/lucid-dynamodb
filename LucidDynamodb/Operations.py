import boto3
import logging

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
        
    def create_table(self, TableName, KeySchema, AttributeDefinitions, ProvisionedThroughput, GlobalSecondaryIndexes=[]):
        """Create a new table

        Args:
            TableName (str): Table name
            KeySchema (list): A key schema specifies the attributes that make up the Partition key,  Sort Key(Optional)) of a table.
            AttributeDefinitions (list): An array of attributes that describe the key schema for the table.
            ProvisionedThroughput (dict): Provisioned throughput settings for this specified table. 
            GlobalSecondaryIndexes (list, optional): An index with a partition key and a sort key that can be different from those on the base table.

        Returns:
            bool: Table creation is successful or failed
        """
        try:
            if(len(GlobalSecondaryIndexes)>0):
                table = self.db.create_table(
                    TableName=TableName,
                    KeySchema=KeySchema,
                    AttributeDefinitions=AttributeDefinitions,
                    GlobalSecondaryIndexes=GlobalSecondaryIndexes,
                    ProvisionedThroughput=ProvisionedThroughput
                )
            else:
                table = self.db.create_table(
                    TableName=TableName,
                    KeySchema=KeySchema,
                    AttributeDefinitions=AttributeDefinitions,
                    ProvisionedThroughput=ProvisionedThroughput
                )
                # Wait until the table exists.
                table.meta.client.get_waiter('table_exists').wait(TableName=TableName)
            return True
        except Exception as e:
            logging.error(e)
            return False

    def delete_table(self, TableName):
        """Delete a table

        Args:
            TableName (str): Table name

        Returns:
            bool: Table deletion is successful or failed
        """
        try:
            table = self.db.Table(TableName)
            table.delete()
            table.wait_until_not_exists()
            return True
        except Exception as e:
            logging.error(e)
            return False
                
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
        except Exception as e:
            logging.error(e)
            return []

    def create_item(self, TableName ,Item):
        """Create a New Item

        Args:
            TableName (str): Table name
            Item (dict): Item with Partition key,  Sort Key(Optional)

        Returns:
            bool: Item creation is successful or failed
        """
        try:
            table = self.db.Table(TableName)
            table.put_item(Item=Item)
            return True
        except Exception as e:
            logging.error(e)
            return False
        
    def delete_item(self, TableName, Key, ConditionExpression = "", ExpressionAttributeValues={}):
        """Delete an Item

        Args:
            TableName (str): Table name
            Key (dict): Partition key,  Sort Key(Optional)
            ConditionExpression (str, optional): ConditionExpression to prevent the item from being deleted if the condition is not met.
            ExpressionAttributeValues (dict, optional): Expressed attribute values.

        Returns:
            bool: Item deletion is successful or failed
        """
        try:
            table = self.db.Table(TableName)
            if(len(ConditionExpression)>0 and len(ExpressionAttributeValues)>0):
                table.delete_item(
                    Key=Key,
                    ConditionExpression=ConditionExpression,
                    ExpressionAttributeValues=ExpressionAttributeValues
                )
            else:
                table.delete_item(
                    Key=Key
                )
            return True
        except Exception as e:
            logging.error(e)
            return False
        
    def read_item(self, TableName, Key):
        """Read an Item

        Args:
            TableName (str): Table name
            Key (dict): Partition key,  Sort Key(Optional)

        Returns:
            dict: Item
        """
        try:
            table = self.db.Table(TableName)
            response = table.get_item(Key=Key)
            return response.get('Item')
        except Exception as e:
            logging.error(e)
            return {}

    def read_items_by_filter(self, TableName, KeyConditionExpression, GlobalSecondaryIndexName=None):
        """Read items by filter
           The Query operation will return all of the items from the table or index with that partition key value. 

        Args:
            TableName (str): Table name
            KeyConditionExpression (boto3.dynamodb.conditions.Equals): Use the KeyConditionExpression parameter to 
                provide a specific value for the partition key. You can optionally narrow the scope of the Query 
                operation by specifying a sort key value and a comparison operator in KeyConditionExpression. 
            GlobalSecondaryIndexName (str, optional): Name of the GlobalSecondaryIndex. Defaults to None.

        Returns:
            list: Table items
        """
        try:
            table = self.db.Table(TableName)
            if GlobalSecondaryIndexName != None:
                response = table.query(
                    IndexName=GlobalSecondaryIndexName,
                    KeyConditionExpression=KeyConditionExpression
                )
            else:
                response = table.query(
                    KeyConditionExpression=KeyConditionExpression
                )   
            return response.get('Items')
        except Exception as e:
            logging.error(e)
            return []    
        
    def generate_attribute_names(self, attribute_names):
        """Generate attribute names

        Args:
            attribute_names (str): Attribute names

        Returns:
            str: Expression attribute names
        """
        ExpressionAttributeNames = {}
        for attribute_name in attribute_names:
            ExpressionAttributeNames["#{}".format(attribute_name)] = attribute_name
        return ExpressionAttributeNames 
      
    def generate_update_expression(self, AttributesToUpdate, Operation):
        """Generate update expression

        Args:
            AttributesToUpdate (dict): Attributes to update
            Operation (str): Operation category
        
        Returns:       
            UpdateExpression (str): Describes all updates you want to perform on specified item
                Example: SET #domain_name = :value1, #owned_by = :value2
            ExpressionAttributeNames (dict): Attribute name
                Example: {'#domain_name': 'domain_name', '#owned_by': 'owned_by'} 
            ExpressionAttributeValues (dict): Attribute values
                Example: {':value1': 'xbox.com', ':value2': 'Microsoft'}
        """
        UpdateExpression = ""
        ExpressionAttributeNames = {}
        ExpressionAttributeValues = {}
        counter = 1
        for attribute_name, attribute_value in AttributesToUpdate.items():
            ExpressionAttributeNames = self.generate_attribute_names(attribute_name.split('.'))
            attribute_name = attribute_name.replace(".", ".#")
            
            if Operation == "UPDATE_EXISTING_ATTRIBUTE_OR_ADD_NEW_ATTRIBUTE":
                if "SET" not in UpdateExpression: 
                    UpdateExpression = "SET "
                UpdateExpression += "#{} = :value{}, ".format(attribute_name, counter)
            elif Operation == "INCREASE_ATTRIBUTE_VALUE":
                if "SET" not in UpdateExpression: 
                    UpdateExpression = "SET "
                UpdateExpression += "#{} = #{} + :value{}, ".format(attribute_name, attribute_name, counter)                
            elif Operation == "ADD_ATTRIBUTE_TO_LIST":
                if "SET" not in UpdateExpression: 
                    UpdateExpression = "SET "
                UpdateExpression += "#{} = list_append(#{},:value{}), ".format(attribute_name, attribute_name, counter)
            elif Operation == "ADD_ATTRIBUTE_TO_STRING_SET":
                if "ADD" not in UpdateExpression: 
                    UpdateExpression = "ADD "
                UpdateExpression += "#{} :value{}, ".format(attribute_name, counter)
            elif Operation == "DELETE_ATTRIBUTE_FROM_STRING_SET":
                if "DELETE" not in UpdateExpression: 
                    UpdateExpression = "DELETE "
                UpdateExpression += "#{} :value{}, ".format(attribute_name, counter)
            if Operation == "ADD_ATTRIBUTE_TO_LIST":
                ExpressionAttributeValues[":value{}".format(counter)] = [attribute_value]
            elif  Operation == "ADD_ATTRIBUTE_TO_STRING_SET" or Operation == "DELETE_ATTRIBUTE_FROM_STRING_SET":
                ExpressionAttributeValues[":value{}".format(counter)] = set([attribute_value])
            else:
                ExpressionAttributeValues[":value{}".format(counter)] = attribute_value
            counter = counter + 1
        
        UpdateExpression = UpdateExpression.rstrip(", ")
        return UpdateExpression, ExpressionAttributeNames, ExpressionAttributeValues
    
    def update_item(self, TableName, Key, 
                    AttributesToUpdate, Operation="UPDATE_EXISTING_ATTRIBUTE_OR_ADD_NEW_ATTRIBUTE"):
        """Update an item

        Args:
            TableName (str): Table name
            Key (dict): Partition key,  Sort Key(Optional)
            AttributesToUpdate (dict): Attributes data with K:V
            Operation (str, optional): Update operation category
                Defaults to UPDATE_EXISTING_ATTRIBUTE_OR_ADD_NEW_ATTRIBUTE.
        
        Returns:
            bool: Attribute update is successful or failed
        """
        try:
            table = self.db.Table(TableName)
            UpdateExpression, ExpressionAttributeNames, \
            ExpressionAttributeValues = self.generate_update_expression(AttributesToUpdate, Operation)
            if(len(UpdateExpression)>0 and len(ExpressionAttributeNames)>0 \
               and len(ExpressionAttributeValues)>0):
                table.update_item(
                                Key=Key,
                                UpdateExpression=UpdateExpression,
                                ExpressionAttributeNames=ExpressionAttributeNames,
                                ExpressionAttributeValues=ExpressionAttributeValues,
                                ReturnValues="ALL_NEW"
                )
                return True
            else:
                return False
        except Exception as e:
            logging.error(e)
            return False

    def increase_attribute_value(self, TableName, Key, AttributeName, IncrementValue):
        """Increase an existing attribute value

        Args:
            TableName (str): Table name
            Key (dict): Partition key,  Sort Key(Optional)
            AttributeName (str): Name of the attribute
            IncrementValue (int): Increment value for an attribute

        Returns:
            bool: Attribute value is incremented or not
        """
        try:
            table = self.db.Table(TableName)
            AttributesToUpdate = {
                AttributeName: IncrementValue
            }
            Operation = "INCREASE_ATTRIBUTE_VALUE"
            UpdateExpression, ExpressionAttributeNames, \
            ExpressionAttributeValues = self.generate_update_expression(AttributesToUpdate, Operation)
            if(len(UpdateExpression)>0 and len(ExpressionAttributeNames)>0 \
               and len(ExpressionAttributeValues)>0):
                response = table.update_item(
                                Key=Key,
                                UpdateExpression=UpdateExpression,
                                ExpressionAttributeNames=ExpressionAttributeNames,
                                ExpressionAttributeValues=ExpressionAttributeValues,
                                ReturnValues="ALL_NEW"
                )
                return True
            else:
                return False
        except Exception as e:
            logging.error(e)
            return False
    
    def delete_attribute(self, TableName, Key, AttributeName):
        """Delete an attribute from an item

        Args:
            TableName (str): Table name
            Key (dict): Partition key,  Sort Key(Optional)
            AttributeName (str): Name of the Attribute

        Returns:
            bool: Attribute deletion is successful or failed
        """
        try:
            table = self.db.Table(TableName)
            response = table.get_item(Key=Key)

            table.update_item(
                                Key=Key,
                                UpdateExpression="REMOVE {}".format(AttributeName),
                                ReturnValues="ALL_NEW"
            )
            return True
        except Exception as e:
            logging.error(e)
            return False
