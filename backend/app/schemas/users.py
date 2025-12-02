from pydantic import BaseModel, Field


class UserBase(BaseModel):
    name: str = Field(..., min_lenght = 4, max_lenght = 30, 
        description = "user's name")

class UserCreate(UserBase):
    pass 

class UserResponse(BaseModel):
    id: int = Field(..., description = "unique user's id")

    class Config:
        from_attributes = True

