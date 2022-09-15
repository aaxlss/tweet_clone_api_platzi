#python
import json
from datetime import date, datetime
from unittest import result
from uuid import UUID
from typing import Optional, List

#Pydantic

from pydantic import BaseModel
from pydantic import EmailStr, Field
#FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body

app = FastAPI()

#Models
class User(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)
    
    
class UserIn(User):
    password: str = Field(..., min_length=8, max_length=50)

class UserOut(User):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    birth_day: Optional[date] = Field(default=None)

class UserRegister(UserOut):
    password: str = Field(..., min_length=8, max_length=50)

class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(..., min_length=1, max_length=256)
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    created_by: UserOut = Field(...)

@app.get(
    path='/',
    tags=["Home"],
    status_code=status.HTTP_200_OK
    )
def home():
    return {
        "Twitter API": "Working"
    }

#Path Operators
## Users
@app.post(
    path='/signup',
    response_model=UserOut,
    status_code= status.HTTP_201_CREATED,
    summary="Register User",
    tags=['Users']
    )
def signup(user: UserRegister = Body(...)):
    """
    Signup

    This path operator register an user in the app

    Parameters:
        -Request body parameter
            -user: UserRegister

    Returns a json with the basic user information
        -user_id: UUID
        -email: Emailstr
        -first_name: str
        -last_name: str
        -birth_day: date
    """
    with open('./users.json', "r+", encoding="utf-8") as f:
        #se obtiene una lista de diccionarios
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict['user_id'] = str(user_dict['user_id'])
        user_dict['birth_day'] = str(user_dict['birth_day'])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))

        return user


@app.post(
    path='/login',
    response_model=UserOut,
    status_code= status.HTTP_200_OK,
    summary="Login User",
    tags=['Users']
    )
def login():
    pass

@app.get(
    path='/users',
    response_model=List[UserOut],
    status_code= status.HTTP_200_OK,
    summary="Show all Users",
    tags=['Users']
    )
def show_all_users():
    """
        This path operation will show all the information of users
        Parameters: 

        Returns a json list with all the users in the app 
            -user_id: UUID
            -email: Emailstr
            -first_name: str
            -last_name: str
            -birth_day: date
    """
    with open('./users.json', 'r', encoding='utf-8') as f:
        results = json.loads(f.read())

        return results

@app.get(
    path='/users/{user_id}',
    response_model=UserOut,
    status_code= status.HTTP_200_OK,
    summary="Show User",
    tags=['Users']
    )
def show_user(user_id: UUID):
    pass

@app.delete(
    path='/users/{user_id}/delete',
    response_model=UserOut,
    status_code= status.HTTP_200_OK,
    summary="Delete User",
    tags=['Users']
    )
def delete_user():
    pass

@app.put(
    path='/users/{user_id}/update',
    response_model=UserOut,
    status_code= status.HTTP_200_OK,
    summary="Update User",
    tags=['Users']
    )
def update_user():
    pass

##Tweets
@app.get(
    path='/tweets',
    response_model=List[Tweet],
    status_code= status.HTTP_200_OK,
    summary="Show all tweets",
    tags=['Tweets']
    )
def show_all_tweets():
    pass

@app.post(
    path='/tweets/post',
    response_model=Tweet,
    status_code= status.HTTP_201_CREATED,
    summary="Post tweet",
    tags=['Tweets']
    )
def post_tweet():
    pass

@app.get(
    path='/tweets/{tweet_id}',
    response_model=Tweet,
    status_code= status.HTTP_200_OK,
    summary="Show tweet",
    tags=['Tweets']
    )
def show_tweet():
    pass

@app.delete(
    path='/tweets/{tweet_id}/delete',
    response_model=Tweet,
    status_code= status.HTTP_200_OK,
    summary="Delete tweet",
    tags=['Tweets']
    )
def delete_tweet():
    pass

@app.put(
    path='/tweets/{tweet_id}/update',
    response_model=Tweet,
    status_code= status.HTTP_200_OK,
    summary="Update tweet",
    tags=['Tweets']
    )
def update_tweet():
    pass