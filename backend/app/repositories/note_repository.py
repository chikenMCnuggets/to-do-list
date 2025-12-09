from sqlalchemy.orm import Session
from typing import List, Optional 
from ..models.notes import Note
from ..schemas.notes import CreateNote, DeleteNote


class NoteRepository():
    def __init__(self, db: Session):
        self.db = db
    def get_all_notes_from_user(self, user_id: int) -> List(Note):
        return self.db.query(Note).filter(Note.user_id == user_id).all()
    def get_by_id(self, note_id: int) -> Optional[Note]:
        return self.db.query(Note).filter(Note.id == note_id).first()
    def get_by_time(self, note_time: int):
        return self.db.query(Note).filter(Note.created_at == note_time)
    def get_by_user(self, user_id: int) -> List(Note):
        return self.db.query(Note).filter(Note.user_id == user_id).all()
    def create_note(self, note_data: CreateNote) -> Note:
        db_note = Note(**note_data.model_dump())
        self.db.add(db_note)
        self.db.commit()
        self.db.refresh(db_note)
        return db_note
    def delete_note(self, note_data: DeleteNote) -> Note:
        db_note = Note(**note_data.model_dump())
        self.db.delete(db_note)
        self.db.commit()
        self.db.refresh(db_note)
        return None
##### дописать обновление статуса заметки!!!!!!!!!!!!