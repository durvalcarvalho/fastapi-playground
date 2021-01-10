import http
from datetime import datetime, time, timedelta
from enum import Enum
from typing import Dict, List, Optional, Set, Union
from uuid import UUID

from fastapi import Body, Cookie, FastAPI, Form, Header, Path, Query, status
from pydantic import BaseModel, EmailStr, Field, HttpUrl


app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.post('/login/')
async def login(username: str = Form(...), password: str = Form(...)):
    return {'username': username}






# class ModelName(str, Enum):
#     alexnet = 'alexnet'
#     resnet = 'resnet'
#     lenet = 'lenet'


# Simple serializer class
# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None


# Nested Serializers
# class Image(BaseModel):
#     url: HttpUrl
#     name: str

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = Field(
#         None, title='The description of the item', max_length=300
#     )
#     price: float = Field(..., gt=0, description='The price must be greater that zero')
#     tax: Optional[float] = None
#     tags: List[str] = []
#     glues: Set[str] = set()
#     image: Optional[Image] = None
#     images: Optional[List[Image]] = None



# class User(BaseModel):
#     username: str
#     full_name: Optional[str] = None



# deeply nested serializers
# class Image(BaseModel):
#     url: HttpUrl
#     name: str


# class Item(BaseModel):
#     name: str = Field(..., example='Foo')
#     description: Optional[str] = Field(None, example='A very nice Item')
#     price: float = Field(..., example=350.4)
#     tax: Optional[float] = Field(None, example=3.2)


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = 10.5
#     tags: Set[str] = set()


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     tags: Set[str] = set()
#     images: Optional[List[Image]] = None

#     # metadata
#     class Config:
#         schema_extra = {
#             # example for docs
#             'example': {
#                 'name': 'Foo',
#                 'description': 'A very nice Item',
#                 'price': 35.4,
#                 'tax': 3.2
#             }
#         }

# class Offer(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     items: List[Item]


# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: Optional[str] = None

# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: Optional[str] = None


# class UserInDB(BaseModel):
#     username: str
#     hashed_password: str
#     email: EmailStr
#     full_name: Optional[str] = None


# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: Optional[str] = None

# class UserIn(UserBase):
#     password: str

# class UserOut(UserBase):
#     pass

# class UserInDB(UserBase):
#     hashed_password: str

# def fake_password_hasher(raw_password: str):
#     return 'supersecret' + raw_password

# def fake_save_user(user_in: UserIn):
#     hashed_password = fake_password_hasher(user_in.password)
#     user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
#     print('User saved! ... just kidding')
#     return user_in_db


# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
#     "baz": {
#         "name": "Baz",
#         "description": "There goes my baz",
#         "price": 50.2,
#         "tax": 10.5,
#     },
# }


# class BaseItem(BaseModel):
#     description: str
#     type: str

# class CarItem(BaseItem):
#     type = 'car'

# class PlaneItem(BaseItem):
#     type = 'plane'
#     size: int


# items = {
#     '1': {"description": "All my friends drive a low rider", "type": "car"},
#     '2': {
#         "description": "Music is my aeroplane, it's my aeroplane",
#         "type": "plane",
#         "size": 5,
#     },
# }


# Union
# @app.get('/items/{item_id}/', response_model=Union[PlaneItem, CarItem])
# async def read_item(item_id: str):
#     return items[item_id]


# @app.post('/items/', status_code=status.HTTP_201_CREATED)
# async def create_item(name: str = Body(..., embed=True)):
#     return {'name': name}



# @app.post('/users/', response_model=UserOut)
# async def create_user(user_in: UserIn):
#     user_saved = fake_save_user(user_in)
#     return user_saved

# # Serializer in != serializer out -> hide info
# @app.post('/users/', response_model=UserOut)
# async def create_user(user: UserIn):
#     return user


# @app.get('/items/{item_id}/name/', response_model=Item, response_model_include={'name', 'description'})
# async def read_item_name(item_id: str):
#     return items[item_id]

# @app.get('/items/{item_id}/public/', response_model=Item, response_model_exclude={'tax'})
# async def read_item_public_data(item_id: str):
#     return items[item_id]


# @app.get('/items/{item_id}/', response_model=Item, response_model_exclude_defaults=True)
# async def read_item(item_id: str):
#     return items[item_id]

# @app.post('/items/', response_model=Item)
# async def create_item(item: Item):
#     return item


# @app.get('/items/')
# async def read_items(x_token: Optional[List[str]] = Header(None)):
#     return {'X-Token values': x_token}

# getting headers parameters -> match variable name
# @app.get('/items/')
# async def read_items(user_agent: Optional[str] = Header(None)):
#     return {'User-Agent': user_agent}


# @app.put('/items/{item_id}/')
# async def read_items(
#     item_id: UUID,
#     start_datetime: Optional[datetime] = Body(...),
#     end_datetime: Optional[datetime] = Body(...),
#     repeat_at: Optional[time] = Body(...),
#     process_after: Optional[timedelta] = Body(...)
# ):
#     start_process = start_datetime + process_after
#     duration = end_datetime - start_process
#     return {
#         'item_id': item_id,
#         'start_datetime': start_datetime,
#         'end_datetime': end_datetime,
#         'repeat_at': repeat_at,
#         'process_after': process_after,
#         'start_process': start_process,
#         'duration': duration
#     }


# @app.post('/index-weights/')
# async def create_index_weights(weights: Dict[int, float]):
#     return weights


# @app.post('/images/multiple/')
# async def create_multiple_images(images: List[Image]):
#     return images

# @app.post('/offers/')
# async def create_offer(offer: Offer):
#     return offer


# @app.put('/items/{item_id}/')
# async def update_item(
#     item_id: int,
#     item: Item = Body(
#         ...,
#         example={
#             'name': 'Foo',
#             'description': 'A very nice Item',
#             'price': 35.8,
#             'tax': 6.99
#         }
#     )
# ):
#     # results = {'item_id': item_id, 'item': item}
#     results = {'item_id': item_id, **item.dict()}
#     return results


# @app.put('/items/{item_id}/')
# async def update_item(item_id: int, item: Item):
#     results = {'item_id': item_id, 'item': item}
#     return results

# explicit body parameters key-value -> { "item": {...} }
# @app.put('/items/{item_id}/')
# async def update_item(item_id: int, item: Item = Body(..., embed=True)):
#     results = {'item_id': item_id, "item": item}
#     return results

# explicit body parameters
# @app.put('/items/{item_id}/')
# async def update_item(
#     item_id: int, 
#     item: Item, 
#     user: User, 
#     importance: int = Body(..., gt=0),
#     q: Optional[str] = None
# ):
#     results = {'item_id': item_id, 'item': item, 'user': user, 'importance': importance}
#     if q:
#         results.update({'q': q})
#     return results

# # multiple body parameters
# @app.put('/items/{item_id}/')
# async def update_item(item_id: int, item: Item, user: User):
#     results = {'item_id': item_id, 'item': item, 'user': user}
#     return results


# @app.put('/items/{item_id}')
# async def update_item(
#     *,
#     item_id: int = Path(..., title='The ID of the item to get', ge=1, le=1000),
#     q: Optional[str] = None,
#     item: Optional[Item] = None
# ):
#     results = {'item_id': item_id}
    
#     if q:
#         results.update({'q': q})

#     if item:
#         results.update({'item': item})
#     return results


# @app.get('/items/')
# async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$")):
#     results = {'items': [{'item_id': "Foo"}, {'item_id': "Bar"}]}

#     if q:
#         results.update({'q': q})
    
#     return results

# Query object optional
# @app.get('/items/')
# async def read_items(q: Optional[str] = Query("fixedquery", min_length=3, max_length=50)):
#     results = {'items': [{'item_id': "Foo"}, {'item_id': "Bar"}]}

#     if q:
#         results.update({'q': q})
    
#     return results


# Query object required (using ellipsis)
# @app.get('/items/')
# async def read_items(q: Optional[str] = Query(..., min_length=3, max_length=50)):
#     results = {'items': [{'item_id': "Foo"}, {'item_id': "Bar"}]}

#     if q:
#         results.update({'q': q})
    
#     return results

# Query object list -> http://localhost:8000/items/?q=foo&q=bar
# @app.get('/items/')
# async def read_items(q: Optional[List[str]] = Query(None)):
#     query_items = {'q': q}
#     return query_items

# Query object list with default values -> http://localhost:8000/items/
# @app.get('/items/')
# async def read_items(q: Optional[List[str]] = Query(['foo', 'bar'])):
#     query_items = {'q': q}
#     return query_items


# metadata
# @app.get('/items/')
# async def read_items(
#     q: Optional[str] = Query(
#         None, 
#         title='Query string', 
#         min_length=3,
#         description='Query string for the items to search in the database that have a good match'
#     )
# ):
#     results = {'items': [{'item_id': "Foo"}, {'item_id': "Bar"}]}
#     if q:
#         results.update({'q': q})
#     return results


# parameter alias -> http://127.0.0.1:8000/items/?item-query=foobaritems
# @app.get('/items/')
# async def read_items(q: Optional[str] = Query(None, alias='item-query')):
#     results = {'items': [{'item_id': "Foo"}, {'item_id': "Bar"}]}
#     if q:
#         results.update({'q': q})
#     return results

# Query parameters definition
# @app.get('/items/')
# async def read_items(
#     q: Optional[str] = Query(
#         None,
#         alias='item-query',
#         title='Query string',
#         description='Query string for the items to search in the database that have a good match',
#         min_length=3,
#         max_length=50,
#         regex='^fixedquery$',
#         deprecated=True
#     )
# ):
#     results = {'items': [{'item_id': "Foo"}, {'item_id': "Bar"}]}
#     if q:
#         results.update({'q': q})
#     return results


# # Path parameters metadata
# @app.get('/items/{item_id}/')
# async def read_items(
#     item_id: int = Path(..., title='The ID of the item to get'),
#     #                   ^^ required parameter
#     q: Optional[str] = Query(None, alias='item-query')
# ):
#     results = {'item_id': item_id}
#     if q:
#         results.update({'q': q})
#     return results

# fastapi loads parameters by name
# @app.get('/items/{item_id}/')
# async def read_items(
#     q: str,
#     item_id: int = Path('...', title='The ID of the item to get'),
# ):
#     results = {'item_id': item_id}
#     if q:
#         results.update({'q': q})
#     return results
    
# key-values parameters
# @app.get('/items/{item_id}/')
# async def read_items(
#     *, item_id: int=Path(..., title='The ID of the item to get'), q: str,
# #  ^^ this tells that all parameters will be called with key-values pairs
# ):
#     results = {'item_id': item_id}
    
#     if q:
#         results.update({'q': q})
        
#     return results

# another constrains on Path parameters -> ge=1 -> greater or equal than 1
# @app.get('/items/{item_id}/')
# async def read_items(
#     *, item_id: int = Path(..., title='The ID of the item to get', ge=1), q: str
# ):
    # results = {'item_id': item_id}
    # if q:
    #     results.update({'q': q})
    # return results

# @app.get('/items/{item_id}')
# async def read_items(*, item_id: int=Path(..., title='The ID of the item to get', gt=0, le=1000), q: str):
#     results = {'item_id': item_id}
#     if q:
#         results.update({'q': q})
#     return results

# @app.get('/items/{item_id}')
# async def read_items(
#     *, 
#     item_id: int=Path(..., title='The ID of the item to get', gt=0, le=1000), 
#     q: str,
#     size: float = Query(..., gt=0, lt=10.5)
# ):
#     results = {'item_id': item_id}
#     if q:
#         results.update({'q': q})
#     return results


# @app.post('/items/{item_id}')
# async def create_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}


# @app.get('/items/')
# async def read_item(skip: int=0, limit: int=10):
#     return fake_items_db[skip : skip+limit]


# @app.get('/files/{file_path:path}')
# async def read_file(file_path: str):
#     return {'file_path': file_path}


# @app.get('/models/{model_name}')
# async def get_model(model_name: ModelName):
#     if model_name == ModelName.alexnet:
#         return {'model_name': model_name, 'message': 'Deep Learning FTW!'}
#     if model_name.value == 'letnet':
#         return {'model_name': model_name, 'message': 'LeCNN all the images'}
#     return {'model_name': model_name, 'message': 'Have some residuals'}


# @app.get('/items/{item_id}')
# async def read_user_item2(item_id: str, needy: str):
#     item = {'item_id': item_id, 'needy': needy}
#     return item


# @app.get('/items/{item_id}/')
# async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
#     item = {'item_id': item_id}

#     if q:
#         item.update({'q': q})
    
#     if not short:
#         item.update({
#             'description': 'This is an amazing item that has a long description'
#         })

#     return item

# @app.get('/users/{user_id}/items/{item_id}')
# async def read_user_item(
#     user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
# ):
#     item = {'item_id': item_id, 'owner_id': user_id}

#     if q:
#         item.update({'q': q})
    
#     if not short:
#         item.update({
#             'description': 'This is an amazing item that has a long description'
#         })

#     return item
