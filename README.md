# Lucid DynamoDB:

A simple python wrapper to AWS DynamoDB.


| S.No | Functions            | Description                      | Status  |
|------|----------------------|----------------------------------|---------|
| 1.   | create_table         | Create a new table if not exists | Done    |
| 2.   | delete_table         | Delete a table                   | Done    |
| 3.   | read_all_table_names | List out all the table names     | Done    |
| 4.   | create_item          | Create a new item                | Done    |
| 5.   | delete_item          | Delete items by filter           | Done    |
| 6.   | read_item            | Read a item                      | Done    |
| 7.   | read_items_by_filter | Read items by filter             | Done    |
| 8.   | update_item          | Update an item by filter         | Backlog |

**Pypi package:** https://pypi.org/project/LucidDynamodb/




**Note:** Add support for Dynamodb streams.

```
python3 -m pip install LucidDynamodb

dineshsonachalam@macbook ~ % python3 -m pip list | grep -i "LucidDynamodb"
LucidDynamodb             1.0.15
```


**Update function should support following functionalities:**

1. UPDATE_KEY
2. ADD_ELEMENT_TO_LIST
3. ADD_ELEMENT_TO_STRING_SET
4. REMOVE_KEY_FROM_DICT
5. REMOVE_ELEMENT_FROM_LIST
6. REMOVE_ELEMENT_FROM_STRING_SET

**Todo:**
1. Complete update_item function.
2. Add integration test to CI/CD.
3. Add proper documentation.
4. Research functionalities of Dynamodb stream.
5. Add support for Dynamodb stream.
6. Integrate Dynamodb stream integration example to CI/CD

