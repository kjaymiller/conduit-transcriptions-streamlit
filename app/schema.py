import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped, 
    mapped_column,
    relationship,
)
from sqlalchemy.types import Date

load_dotenv()

class Base(DeclarativeBase):
    pass
    

class Episode(Base):
    __tablename__ = 'conduit_transcripts'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(120))
    content: Mapped[str]
    date: Mapped[Optional[Date]] = mapped_column(Date)
    description: Mapped[str]
    url: Mapped[str] = mapped_column(String(240))
    

engine = create_engine(os.getenv("POSTGRES_SERVICE_URI"))
Base.metadata.create_all(engine)