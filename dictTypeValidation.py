#validation of nested and flat dictionaries

import sys
def validate_mixed_dictionary(data, validation_rules):

    for field, rules in validation_rules.items():
        if field not in data:
            return False

        field_value = data[field]

        if isinstance(field_value, dict):
            nested_validation_result = validate_mixed_dictionary(field_value, rules.get('rules', {}))

            if not nested_validation_result:
                return False
        else:
            if 'type' in rules and not isinstance(field_value, rules['type']):
                print(f"Error: Field '{field}' must be of type {rules['type']}.")
                return False

            if 'min_length' in rules and len(str(field_value)) < rules['min_length']:
                print(f"Error: Field '{field}' must have a minimum length of {rules['min_length']}.")
                return False

            if 'max_length' in rules and len(str(field_value)) > rules['max_length']:
                print(f"Error: Field '{field}' must have a maximum length of {rules['max_length']}.")
                return False

            if 'min_value' in rules and field_value < rules['min_value']:
                print(f"Error: Field '{field}' must have a minimum value of {rules['min_value']}.")
                return False

            if 'max_value' in rules and field_value > rules['max_value']:
                print(f"Error: Field '{field}' must have a maximum value of {rules['max_value']}.")
                return False

    return True

#validate nested dictionary
nested_data = {
    'person': {
        'name': 'Sami',
        'age': 22,
        'address': {
            'city': 'Kathmandu',
            'zip_code': '11011'
        }
    },
    'is_student': True
}

nested_rules = {
    'person': {
        'type': dict,
        'rules': {
            'name': {'type': str, 'min_length': 3, 'max_length': 50},
            'age': {'type': int, 'min_value': 18, 'max_value': 99},
            'address': {
                'type': dict,
                'rules': {
                    'city': {'type': str, 'min_length': 3, 'max_length': 50},
                    'zip_code': {'type': str, 'min_length': 5, 'max_length': 10}
                }
            }
        }
    },
    'is_student': {'type': bool}
}

result_nested = validate_mixed_dictionary(nested_data, nested_rules)
print(f"Nested dictionary validation result: {result_nested}")


#validate normal dictionary
normal_data = {
    'name': 'Anupa',
    'age': 22,
    'is_employee': False
}

normal_rules = {
    'name': {'type': str, 'min_length': 3, 'max_length': 50},
    'age': {'type': int, 'min_value': 18, 'max_value': 99},
    'is_employee': {'type': bool}
}

result_normal = validate_mixed_dictionary(normal_data, normal_rules)
print(f"Non-nested dictionary validation result: {result_normal}")
sys.exit()
