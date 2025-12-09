from sqlalchemy.orm import Session
from typing import List, Optional 
from ..models.notes import User 
from ..schemas.users import UserCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db 
    def get_all(self) -> List[User]:
        return self.db.query(User).all()
    def get_by_id(self, user_id: int) -> Optional[User]:
        return self.db.query(User).filter(User.id == user_id).first()
    def get_by_name(self, user_name: str) -> Optional[User]:
        return self.db.query(User).filter(User.name == user_name).first()

    def create_user(self, user_data: UserCreate) -> User:
        db_user = User(**user_data.model_dump())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user