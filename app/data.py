from pathlib import Path

import arrow
import frontmatter
from sqlalchemy.orm import Session

from schema import Episode, engine

fmt = r"MMMM[\s+]D[\w+,\s+]YYYY"

def episodes_from_path(directory:Path) -> None:
    """Seed the database with episodes from a file"""
    with Session(engine) as session:
        episodes = [from_episode_from_frontmatter(path) for path in directory.iterdir()]
        session.add_all(episodes)
        session.commit()


def from_episode_from_frontmatter(filepath: Path) -> Episode:
    """Create an episode from frontmatter and content"""
    post = frontmatter.loads(filepath.read_text())
    return Episode(
            title=post['title'],
            content=post.content,
            date=arrow.get(post['pub_date'], fmt).date(),
            description=post['description'],
            url=post['url'],
    )

def all_episodes() -> list[Episode]:
    """Get all episodes from the database"""
    with Session(engine) as session:
        return session.query(Episode).all()

if __name__ == "__main__":
    episodes_from_path(Path("../transcripts"))