from pydantic import BaseModel, Field
from datetime import datetime

class UserData(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., ge=18, le=99)
    time: datetime | None  # datetime as a type for validation
    is_student: bool




user_data_input = {
    'name': input("Enter your name: "),
    'age': int(input("Enter your age: ")),
    'time': datetime.strptime(input("Enter the time (YYYY-MM-DD HH:MM:SS): "), "%Y-%m-%d %H:%M:%S"),
    'is_student': input("Are you a student? (True/False): ").lower() == 'true'
}


try:
    user_data = UserData(**user_data_input)
    print("Data is valid.")
except Exception as e:
    print(f"Data validation failed. Error: {e}")
