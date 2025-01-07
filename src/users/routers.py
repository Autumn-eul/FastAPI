from fastapi import APIRouter
from datetime import date
from users.request import CreateUserRequestBody

router = APIRouter(tags=["Users"])

users = [
    {"id": 1, "name": "Elon Musk", "date_of_birth": date(1970, 1, 1)},
]

# 전체 유저 목록 조회 API
@router.get("/users")
def get_users_handler():
    return users

# 새로운 유저 생성 API
@router.post("/users")
def create_user_handler(body: CreateUserRequestBody):
    # 1. 사용자로부터 데이터를 받고
    # 2. 받은 데이터의 유효성 검사
    # 3. 새로운 유저 데이터를 유저 목록에 추가
    return