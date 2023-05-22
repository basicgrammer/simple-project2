from ninja import Router, Schema

router = Router()


'''
## API 응답 스키마
## API의 응답값을 수정하려면 이곳에서 수정하시면 됩니다.
'''


## Code 200
class Success(Schema) :
    message: dict

## Code 201
class Created(Schema) :
    message: dict

## Code 400
class Error(Schema) :
    message: dict

## Code 500
class ServerError(Schema) :
    message: dict



'''
## API 입력 스키마
## API 입력값을 수정하시려면 이곳에서 수정하시면 됩니다.
'''

class InputData(Schema) :
    name : str
    option_set : list
    tag_set : list


## 상품 리스트 요청 API
@router.get('/products',response={200:Success, 400:Error})
def request_item(request, data:InputData) :

    print(data.dict())

    message = {
        "message": "API 완료"
    }

    return  200, {'message': message}



## 상품 등록 API 
@router.post('/products',response={200:Success, 400:Error})
def create_item(request, data:InputData) :

    print(data.dict())

    message = {
        "message": "API 완료"
    }

    return  200, {'message': message}



## 상품 수정 API
@router.patch('/products',response={200:Success, 400:Error})
def modify_item(request, data:InputData) :

    print(data.dict())

    message = {
        "message": "API 완료"
    }

    return  200, {'message': message}


## 상품 삭제 API
@router.patch('/products',response={200:Success, 400:Error})
def modify_item(request, data:InputData) :

    print(data.dict())

    message = {
        "message": "API 완료"
    }

    return  200, {'message': message}





    



##  상품 추가 / 조회 / 수정 /삭제 API 