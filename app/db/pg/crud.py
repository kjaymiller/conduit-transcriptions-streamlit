from sqlmodel import Session, select
from .schema import Episode, engine

def all_episodes() -> list[Episode]:
    """Get all episodes from the database"""
    with Session(engine) as session:
        return session.exec(select(Episode)).all()
        