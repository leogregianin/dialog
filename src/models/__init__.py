from pgvector.sqlalchemy import Vector
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from .db import engine

Base = declarative_base()


class Chat(Base):
    __tablename__ = "chats"

    uuid = Column(String, primary_key=True)


class CompanyContent(Base):
    __tablename__ = "contents"

    id = Column(Integer, primary_key=True, autoincrement=True)
    question = Column(String)
    content = Column(String)
    embedding = Column(Vector(1536))


# if __name__ == "__main__":
Base.metadata.create_all(engine)