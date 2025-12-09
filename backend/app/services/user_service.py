from sqlalchemy.orm import Session
from typing import List
from ..repositories.user_repository import UserRepository
from ..schemas.users import UserResponse, UserCreate
from fastapi import HTTPException, status

class UserServise:
    def __init__(self, db: Session):
        self.repository = UserRepository(db)
    
    def get_all_Users(self) -> List[UserResponse]:
        users = self.repository.get_all()
        return [UserResponse.model_validate(user) for user in users]

    def get_user_by_id(self, user_id: int) -> UserResponse:
        user = self.repository.get_by_id(user_id) 
        if not user:
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND,
                detail = f"User with id {user_id} not found"
            )
        return UserResponse.model_validate(user)
    
    def create_user(self, user_data: UserCreate) -> UserResponse:
        new_user = self.repository.create(user_data)
        return UserResponse.model_validate(new_user)