class TableAlreadyExists(Exception):
    """Exception is raised when we try to create a table 
       with a table name that already exists in Dynamodb.

    Attributes:
        table_name (str): Table name
        message (str): Explanation of the error
    """
    def __init__(self, table_name, message="Table already exists"):
        self.table_name = table_name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} -> {self.table_name}'
    
class TableNotFound(Exception):
    """Exception is raised when we try to perform a Dynamodb 
       operation in a table that doesn't exist

    Attributes:
        table_name (str): Table name
        message (str): Explanation of the error
    """
    def __init__(self, table_name, message="Table doesn't exist"):
        self.table_name = table_name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} -> {self.table_name}'

class ItemNotFound(Exception):
    """Exception is raised when the item is not available

    Attributes:
        table_name (str): Table name
        key (dict): Partition key,  Sort Key(Optional)
        message (str): Explanation of the error
    """
    def __init__(self, table_name, key, message="Item doesn't exist"):
        self.table_name = table_name
        self.key = key
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} -> Key: {self.key}, Table: {self.table_name}'

class QueryFilterValidationFailed(Exception):
    """Exception is raised when the Query filter is not valid

    Attributes:
        table_name (str): Table name
        message (str): Explanation of the error
    """
    def __init__(self, table_name, message="Item doesn't exist"):
        self.table_name = table_name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} -> Table: {self.table_name}'

class UnexpectedError(Exception):
    """Exception is raised when we perform an unexpected Dynamodb operation.

    Attributes:
        message (str): Explanation of the error
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'Unexpected Dynamodb operation -> {self.message}'