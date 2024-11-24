from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from config import restart_db

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str
    year: int


restart_db()