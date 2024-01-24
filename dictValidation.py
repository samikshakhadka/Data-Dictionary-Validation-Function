#validation with default rules and user input data dictionaries

def validate_dictionary(data, validation_rules):

    for field, rules in validation_rules.items():
        if field not in data:
            return False

        field_value = data[field]

        if 'type' in rules and not isinstance(field_value, rules['type']):
            print(f"Error: Field '{field}' must be of type {rules['type']}.")
            return False

        if 'min_length' in rules and len(field_value) < rules['min_length']:
            print(f"Error: Field '{field}' must have a minimum length of {rules['min_length']}.")
            return False

        if 'max_length' in rules and len(field_value) > rules['max_length']:
            print(f"Error: Field '{field}' must have a maximum length of {rules['max_length']}.")
            return False

        if 'min_value' in rules and field_value < rules['min_value']:
            print(f"Error: Field '{field}' must have a minimum value of {rules['min_value']}.")
            return False

        if 'max_value' in rules and field_value > rules['max_value']:
            print(f"Error: Field '{field}' must have a maximum value of {rules['max_value']}.")
            return False

    return True


user_data = {
    'name': input("Enter your name: "),
    'age': int(input("Enter your age: ")),
    'submit_assignment': input("Have you submitted your assignments? (True/False): ").lower() == 'true'
}

rules = {
    'name': {'type': str, 'min_length': 3, 'max_length': 50},
    'age': {'type': int, 'min_value': 18, 'max_value': 99},
    'submit_assignment': {'type': bool}
}

result = validate_dictionary(user_data, rules)

if result:
    print("The student is eligible for exam")
else:
    print("The student is not eligible for exam")
