from sqlalchemy.orm import Session
from typing import List, Optional 
from ..models.notes import Note
from ..schemas.notes import CreateNote


class NoteRepository():
    def __init__(self, db: Session):
        self.db = db
    def get_all_notes_from_user(self, user_id: int) -> List(Note):
        return self.db.query(Note).filter(Note.user_id == user_id).all()
    def get_note(self, note_id: int) -> Optional[Note]:
        return self.db.query(Note).filter(Note.id == note_id).first()
    def get_note_by_time(self, note_time: int):
        return self.db.query(Note).filter(Note.created_at == note_time)

####доделать create