from cerberus import Validator
from datetime import datetime

def date_time_validate(field, value , error):
    try:
        datetime.strptime(value,"%Y-%m-%d %H:%M:%S")
    except ValueError:
        error(field, "Must be in 2002-05-28 15:00:00 format")




user_data_schema = {
    'name': {'type': 'string', 'minlength': 3, 'maxlength': 50},
    'age': {'type': 'integer', 'min': 18, 'max': 99},
    'time': {'validator': date_time_validate, 'nullable': True},
    'is_student': {'type': 'boolean'},
}


user_data_input = {
    'name': input("Enter your name: "),
    'age': int(input("Enter your age: ")),
    'time': input("Enter the time (YYYY-MM-DD HH:MM:SS) or press Enter for None: "),
    'is_student': input("Are you a student? (True/False): ").lower() == 'true'
}


validator = Validator(user_data_schema)
if validator.validate(user_data_input):
    print("Data is valid.")

    if 'time' in user_data_input and user_data_input['time']:
        user_data_input['time'] = datetime.strptime(user_data_input['time'], "%Y-%m-%d %H:%M:%S")
    print("Processed user data:", user_data_input)
else:
    print("Data validation failed. Errors:", validator.errors)
