from pydantic import BaseModel, Field


class NotesBase(BaseModel):
    name: str = Field(..., min_lenght = 2, max_lenght = 20)
    text: str = Field(..., min_lenght = 1, max_lenght = 5000)
    state: bool
    created_at: int
    user_id: int = Field(..., description = "user's id who owns ts")

class CreateNote(NotesBase):
    pass

class UpdateNote(NotesBase):
    pass

class NoteResponse(NotesBase): #Заменить на BaseModel, запросить все необходимые данные
    id: int = Field(..., description = "unique id")

    class config:
        from_attributes = True

class NotesListResponse(BaseModel):
    products: list[NoteResponse]
