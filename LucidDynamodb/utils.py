def create_attribute_names(attribute_names):
    """Create attribute names
    Args:
        attribute_names (str): Attribute names
    Returns:
        str: Expression attribute names
    """
    expression_attribute_names = {}
    for attribute_name in attribute_names:
        expression_attribute_names[f"#{attribute_name}"] = attribute_name
    return expression_attribute_names

def generate_expression_attribute_values(attributes_to_update, operation):
    """Generate Expression Attribute Values
    Args:
        attributes_to_update (dict): Attributes to update
        operation (str): Operation category
    Returns:
        update_expression (str): Describes all updates you want to perform on specified item
            Example: SET #domain_name = :value1, #owned_by = :value2
        expression_attribute_names (dict): Attribute name
            Example: {'#domain_name': 'domain_name', '#owned_by': 'owned_by'}
        expression_attribute_values (dict): Attribute values
            Example: {':value1': 'xbox.com', ':value2': 'Microsoft'}
    """
    update_expression = ""
    expression_attribute_names = {}
    expression_attribute_values = {}
    counter = 1
    for attribute_name, attribute_value in attributes_to_update.items():
        expression_attribute_names = create_attribute_names(attribute_name.split('.'))
        attribute_name = attribute_name.replace(".", ".#")
        if operation == "UPDATE_EXISTING_ATTRIBUTE_OR_ADD_NEW_ATTRIBUTE":
            if "SET" not in update_expression:
                update_expression = "SET "
            update_expression += f"#{attribute_name} = :value{counter}, "
        elif operation == "INCREASE_ATTRIBUTE_VALUE":
            if "SET" not in update_expression:
                update_expression = "SET "
            update_expression += f"#{attribute_name} = #{attribute_name} + :value{counter}, "
        elif operation == "ADD_ATTRIBUTE_TO_LIST":
            if "SET" not in update_expression:
                update_expression = "SET "
            update_expression += f"#{attribute_name} = list_append(#{attribute_name},:value{counter}), "
        elif operation == "ADD_ATTRIBUTE_TO_STRING_SET":
            if "ADD" not in update_expression:
                update_expression = "ADD "
            update_expression += f"#{attribute_name} :value{counter}, "
        elif operation == "DELETE_ATTRIBUTE_FROM_STRING_SET":
            if "DELETE" not in update_expression:
                update_expression = "DELETE "
            update_expression += f"#{attribute_name} :value{counter}, "
        if operation == "ADD_ATTRIBUTE_TO_LIST":
            expression_attribute_values[f":value{counter}"] = [attribute_value]
        elif operation == "ADD_ATTRIBUTE_TO_STRING_SET" or operation == "DELETE_ATTRIBUTE_FROM_STRING_SET":
            expression_attribute_values[f":value{counter}"] = set([attribute_value])
        else:
            expression_attribute_values[f":value{counter}"] = attribute_value
        counter = counter + 1
    update_expression = update_expression.rstrip(", ")
    return update_expression, expression_attribute_names, expression_attribute_values