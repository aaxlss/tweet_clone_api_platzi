#python
from datetime import date
from uuid import UUID
from typing import Optional

#Pydantic

from pydantic import BaseModel
from pydantic import EmailStr, Field
#FastAPI
from fastapi import FastAPI
from fastapi import status

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

class Tweet(BaseModel):
    pass

@app.get(
    path='/',
    tags=["Home"],
    status_code=status.HTTP_200_OK
    )
def home():
    return {
        "Twitter API": "Working"
    }