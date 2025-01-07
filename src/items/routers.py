from fastapi import APIRouter, Query

router = APIRouter(prefix="/items", tags=["Items"]) # include_in_schema=False: API 로 호출은 가능하고 swagger 문서에서만 제거

items = [
	{"id": 1, "name": "i-phone 16", "price": 100},
	{"id": 2, "name": "Galaxy 25", "price": 200},
    {"id": 3, "name": "Huawei", "price": 50},
]

# 전체 상품 목록 API
# Query Param: 127.0.0.1:8000/items?min_price=100&max_price=200
# 중복되는 경로 "/items" 를 prefix 에 넣어줌으로써 간략하게 만들 수 있음
@router.get("") # include_in_schema=False: 특정 API 만 문서에서 제거 / deprecated=Treu: 아직 쓸수는 있는데, 다음 버전에서 없어질 API
def items_handler(
    min_price: int | None = None,
    max_price: int | None = None,
    keyword: str | None = Query(None, max_length=5),
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

# 특정 상품 반환 API
@router.get("/{item_id}") # 동적인 path # prefix 덕분에 간략히 표현
def item_handler(
    # item_id: int = Path(..., max_digits=5), # Path 변수를 이용해서도 추가조건을 넣을 수 있음
    item_id: int,   # path 변수
    # max_price: int | None = None,   # query param
    max_price: int = Query(..., ge=10_000, lt=1_000_000), # ... 을 넣으면 Query 를 필수값으로 받는다
    # max_length(최대 길이)
    # max_digits(최대 자릿수)
):
    result = None
    for item in items:
        if item["id"] == item_id:
            result = item
            print(f"max_price: {max_price}")
    return {"item": result}