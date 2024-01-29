def validate_dictionary(data, validation_rules):
    eligible_students = []

    for user_data in data:
        is_valid = True
        current_student = {}

        for field, rules in validation_rules.items():
            if field not in user_data:
                is_valid = False
                print(f"Error: Field '{field}' not present in the data.")
                break

            field_value = user_data[field]

            if 'type' in rules and not isinstance(field_value, rules['type']):
                print(f"Error: Field '{field}' must be of type {rules['type']}.")
                is_valid = False
                break

            if 'min_length' in rules and len(field_value) < rules['min_length']:
                print(f"Error: Field '{field}' must have a minimum length of {rules['min_length']}.")
                is_valid = False
                break

            if 'max_length' in rules and len(field_value) > rules['max_length']:
                print(f"Error: Field '{field}' must have a maximum length of {rules['max_length']}.")
                is_valid = False
                break

            if 'min_value' in rules and field_value < rules['min_value']:
                print(f"Error: Field '{field}' must have a minimum value of {rules['min_value']}.")
                is_valid = False
                break

            if 'max_value' in rules and field_value > rules['max_value']:
                print(f"Error: Field '{field}' must have a maximum value of {rules['max_value']}.")
                is_valid = False
                break

            if field == 'submit_assignment' and field_value is not True:
                print(f"Error: Field '{field}' must be 'True' for eligibility.")
                is_valid = False
                break

            current_student[field] = field_value

        if is_valid:
            eligible_students.append(current_student)

    return eligible_students

user_data_batch = [
    {'name': 'Sami', 'age': 10, 'submit_assignment': False},
    {'name': 'Rajan', 'age': 25, 'submit_assignment': False},
    {'name': 'Rohit', 'age': 20, 'submit_assignment': True},
]

rules = {
    'name': {'type': str, 'min_length': 3, 'max_length': 50},
    'age': {'type': int, 'min_value': 18, 'max_value': 99},
    'submit_assignment': {'type': bool},
}

result = validate_dictionary(user_data_batch, rules)

for student in result:
    print(f"{student['name']} ({student['age']} years old) is eligible for the exam.")
