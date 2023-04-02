import json

def switch_key_pairs(obj, fields):
    """
    Recursively switch the key-value pairs of certain fields in a JSON object.

    Args:
        obj (any): A JSON object.
        fields (list): A list of field names whose key-value pairs should be switched.

    Returns:
        The modified JSON object with the specified fields' key-value pairs switched.
    """
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in fields:
                obj[key] = {v: k for k, v in value.items()}
            else:
                obj[key] = switch_key_pairs(value, fields)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            obj[i] = switch_key_pairs(item, fields)
    return obj

# Load the input.json file
with open('config.json', 'r') as f:
    data = json.load(f)

# Define the fields whose key-value pairs should be switched
fields_to_switch = ['replace_file', 'replace_content']

# Switch the key-value pairs of the specified fields
modified_data = switch_key_pairs(data, fields_to_switch)

# Save the modified data to a new file
with open('reversed_config.json', 'w') as f:
    json.dump(modified_data, f)
