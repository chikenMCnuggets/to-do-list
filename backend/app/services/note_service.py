from sqlalchemy.orm import Session
from typing import List
from ..repositories.note_repository import NoteRepository
from ..schemas.notes import CreateNote, NoteResponse, 
from fastapi import HTTPException, status


class NoteService:
    def __init__(self, db: Session):
        repository = NoteRepository(db)
    
    def get_note_by_id(self, note_id: int) -> NoteResponse:
        note = self.repository.get_by_id(note_id)
        return NoteResponse.model_validate(note)
    
    def get_all_notes_by_user_id(self, user_id: int) -> NotesListResponse:
        notes = self.repository.get_by_user(user_id)
        notes_response = [NoteResponse.model_validate(note) for note in notes]
        return NotesListResponse(notes = notes_response, total = len(notes_response))

    def create_note_s(self, note_data: CreateNote) -> NoteResponse:
        new_note = self.repository.create_note(note_data)
        return NoteResponse.model_validate(new_note)
    

#Добавить удаление заметки