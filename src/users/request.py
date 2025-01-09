from datetime import date
from pydantic import BaseModel, field_validator, ValidationError

class UserCreateRequestBody(BaseModel):
    name: str
    date_of_birth: date # 생년월일

    @field_validator("date_of_birth")
    def validate_date_of_birth(cls, v):
        age_delta = date.today() - v
        if age_delta.days < 5 * 365:
            raise ValueError("만 6세 이상만 가입할 수 있습니다.")
        return v
        # return v 를 꼭 해줘야하는가?
        # field_validator 를 사용하는 규칙


class UserUpdateRequestBody(BaseModel):
    name: str