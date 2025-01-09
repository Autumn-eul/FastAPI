from datetime import datetime
from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from items.routers import router as item_router
from users.routers import router as user_router
app = FastAPI()
app.include_router(item_router)
app.include_router(user_router)

class NowResponse(BaseModel):
    now: datetime


@app.get("/now", response_model=NowResponse) # response_model 을 추가하면 schema 가 추가되고 응답 얘시를 볼수 있음
def get_now_handler():
    # return {"now": datetime.now()} ==
    return NowResponse(now=datetime.now())
    # 사실상 같은건데 왜 이렇게 하나요?
    # NowResponse 가 한번더 검사하고 전달하기 때문에 안정적이다
    # 응답 예시가 문서화 되기때문에 가독성이 증가
    # 다른 필요한 곳에서 재사용 할수 있음
    # 따라서 일반적으로 응답에 pydantic 을 사용하는게 좋음


    # html = f"<html><body><h1>now: {datetime.now()}</h1></body></html>"

    # return HTMLResponse(content=html)
    # == return Response(content=html, media_type="text/html")

    # Python datetime 객채 -> JSON String
    # return {"now": datetime.now()} # fastapi가 알아서 직렬화 / 역직렬화를 해줌

    # return Response(
    #     content=str(datetime.now()), # str로 감싸지 않으면 datetime 객체이기 때문에 인식할 수 없어서 500 에러 발생
    #     media_type="text/plain",
    #     status_code=201, # Response 를 사용하면 상태코드도 변경할 수 있음
    # )


# BaseModel: 우리가 직접 검증할 데이터를 선언해서 사용할 때
# fastapi: Query, Body, Header -> FastAPI 가 미리 만들어놓은 클래스


# @app.get("/")
# def health_check_handler():
#     return {"ping": "pong"}
#
# @app.get("/hello")
# def hello_handler():
#     return {"hello": "world"}


"""
# 전체 상품 목록 API
# Query Param: 127.0.0.1:8000/items?price_lt=10000
@app.get("/items")
def items_handler(price_lt: int | None = None):
    # int | None -> int or None
    # int | str | boolean -> int or str or boolean
    # default 값이 없으면 필수값(required)으로 해석 -> 사용자가 보내지 않으면 에러 발생
    # optional 한 값을 처리하고 싶으면, default
    
    if price_lt:
        # return 가격이 1만원 미만인 상품만 찾아서 반환
        pass
    else:
        # return 전체 상품
        pass

    # return {"Query Param": price_lt}


# 특정 상품 반환 API
@app.get("/items/{item_id}")
def item_handler(item_id: int):
    item_id += 1000
    return {"item_id": item_id}


# lt: less than = 미만
# gt: greater than = 초과
# lte, le: less than or equal to = 이하
# gte, ge: greater than or equal to = 이상

# Path 변수 : path 안에서 동적으로 바뀌는 값
# Query Param : 물음표 뒤에 받아오는 값
"""


# 특정 상품 반환 API
# 1. 일반 & 필수
# max_price: int

# 2. 일반 & 필수 X
# max_price: int = 10
# max_price: int | None = None

# 3. Query Class & 필수
# max_price: int = Query(..., ge=10_000, lt=1_000_000)

# 4. Query Class & 필수 X
# max_price:int | None=Query(None, ge=10_000)
# 추가적인 조건을 지정해주기 위함이다


"""
127.0.0.1:8000/categories/pants?min_price=10000&max_price=50000
-> 카테고리 이름이 pants인 상품에 대해서 가격 1만원 ~ 5만원
"""


"""
/items/3?max_price=100
=> 
3 : path param
max_price : query param
"""


# from typing import Annotated

# type hint + 주석 (설명충)
# python 3.9부터 생긴 최신 문법으로 metadata를 함께 정의할 수 있음
# 메타데이터: 다른 개발자를 위한 문서 역할(주석 대신 사용)
# def say_hello(name: Annotated[str, "출력하고 싶은 이름"] -> str:
#       return f"Hello, {name}"