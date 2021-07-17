class DynamoException(Exception):
    """Base exception for all LucidDynamodb raised exceptions"""

# --- Table exceptions ---
class DynamoTableException(DynamoException):
    """Base exception class for all DynamoTable errors"""

class TableCreationFailed(DynamoTableException):
    """Table creation failed"""

class TableDeletionFailed(DynamoTableException):
    """Table deletion failed"""

class ReadAllTableNamesFailed(DynamoTableException):
    """Fetching all table names failed"""
    
class CreateItemFailed(DynamoTableException):
    """Item creation failed"""
    
class DeleteItemFailed(DynamoTableException):
    """Item deletion failed"""
    
class ReadItemFailed(DynamoTableException):
    """Read item failed"""
    
class ReadItemsByFilterFailed(DynamoTableException):
    """Read items by filter failed"""

class UpdateItemFailed(DynamoTableException):
    """Update item failed"""
    
class IncreaseAttributeValueFailed(DynamoTableException):
    """Increasing an attribute value failed"""

class DeleteAttributeFailed(DynamoTableException):
    """Deleting attributes in a item failed"""
        
    
