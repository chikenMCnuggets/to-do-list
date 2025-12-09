from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..services.note_service import NoteService
from ..schemas.notes import NoteResponse, CreateNote
from ..services.note_service import 
from pydantic import BAseModel

router = APIRouter(
    prefix = "/api/notes",
    tags = ["notes"]
)

class AddToUserRequest(BaseModel):
    note_id: int


@router.get("/{user_id}", response_model = List[NoteResponse], status_code = status.HTTP_200_OK)
def get_notes_by_user(user_id: int, db: Session = Depends(get_db)):
    service = NoteService(db)
    return service.get_all_notes_by_user_id(user_id)

@router.get("/{note_id}", response_model = NoteResponse, status_code = status.HTTP_200_OK)
def get_note_by_id(note_id: int, db: Session = Depends(get_db)):
    service = NoteService(db)
    return service.get_note_by_id(note_id)

@router.post("/add/{user_id}", status_code = status.HTTP_200_OK)
def add_to_user(request: AddToUserRequest, db: Session = Depends(get_db)):
    service = NoteService(db)
    note = CreateNote(note_id = request.note_id)
    updated_user = service.
# пз нагрузка (JSON)