def validate_field(field_value, rules):
    if 'type' in rules and not isinstance(field_value, rules['type']):
        return False
    if 'min_length' in rules and len(str(field_value)) < rules['min_length']:
        return False
    if 'max_length' in rules and len(str(field_value)) > rules['max_length']:
        return False
    if 'min_value' in rules and field_value < rules['min_value']:
        return False
    if 'max_value' in rules and field_value > rules['max_value']:
        return False
    return True

def validate_dictionary(data, validation_rules):
    results = []

    for user_data in data:
        is_valid = all(
            validate_field(user_data.get(field), rules)
            for field, rules in validation_rules.items()
        )
        results.append(is_valid)

    return results

user_data_batch = [
    {'name': 'sami', 'age': 22, 'submit_assignment': False},
    {'age': 22, 'name': 'ramu', 'submit_assignment': True},
    {'name': 100, 'age': 'hahano', 'submit_assignment': False}
]

rules = {
    'name': {'type': str, 'min_length': 3, 'max_length': 50},
    'age': {'type': int, 'min_value': 18, 'max_value': 99},
    'submit_assignment': {'type': bool},
}

results = validate_dictionary(user_data_batch, rules)

for result in results:
    print(result)
