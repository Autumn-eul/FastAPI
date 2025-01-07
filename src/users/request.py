from pydantic import BaseModel
from datetime import date

class CreateUserRequest(BaseModel):
    name: str
    date_of_birth: date # 생일