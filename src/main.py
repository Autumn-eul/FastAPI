from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check_handler():
    return {"ping": "pong"}

@app.get("/hello")
def hello_handler():
    return {"hello": "world"}

items = [
	{"id": 1, "name": "i-phone 16", "price": 100},
	{"id": 2, "name": "Galaxy 25", "price": 200},
    {"id": 3, "name": "Huawei", "price": 50},
]

"""
# 전체 상품 목록
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

# 특정 상품 반환
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

# 전체 상품 목록
# Query Param: 127.0.0.1:8000/items?min_price=100&max_price=200
@app.get("/items")
def items_handler(
    min_price: int | None = None,
    max_price: int | None = None,
):
    result = items
    if min_price:
        # 가격이 min_price 이상인 상품만 조회
        new_result = []
        for item in result:
            if item["price"] >= min_price:
                new_result.append(item)
                result = new_result

        # result = [item for item in result if item["price"] >= min_price]

    if max_price:
        # 가격이 max_price 이하인 상품만 조회
        result = [item for item in result if item["price"] <= max_price]

    return {"items": result}


# 특정 상품 반환
@app.get("/items/{item_id}") # 동적인 path
def item_handler(
    item_id: int,   # path 변수
    max_price: int | None = None,   # query param
):
    result = None
    for item in items:
        if item["id"] == item_id:
            result = item
            print(f"max_price: {max_price}")
    return {"item": result}

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