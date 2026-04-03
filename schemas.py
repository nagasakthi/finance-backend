from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    username: str
    password: str
    role: str

class UserOut(BaseModel):
    id: int
    username: str
    role: str
    is_active: bool

    class Config:
        orm_mode = True


class RecordCreate(BaseModel):
    amount: float
    type: str
    category: str
    date: date
    notes: str

class RecordOut(RecordCreate):
    id: int

    class Config:
        orm_mode = True

class LoginRequest(BaseModel):
    username: str
    password: str